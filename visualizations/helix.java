package landvis.technique;

import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.HashMap;

import javax.media.opengl.GL;
import javax.swing.Box;
import javax.swing.BoxLayout;
import javax.swing.JComponent;
import javax.swing.JPanel;
import javax.swing.event.ChangeEvent;
import javax.swing.event.ChangeListener;
import javax.swing.event.ListSelectionEvent;

import landvis.model.Area;
import landvis.model.DiagnosisSelectionModel;
import landvis.model.SpatialSelectionChangeEvent;
import landvis.model.SpatialSelectionModel;
import landvis.model.TemporalSelectionChangeEvent;
import landvis.model.TemporalSelectionModel;
import landvis.model.TemporalSelectionModel.Granularity;
import landvis.util.Colors;
import landvis.util.DB;
import landvis.util.RenderingContext;
import landvis.util.SliderSpinner;
import landvis.util.SwingWorkerEx;
import landvis.util.SwingWorkerScheduler;
import color.ColorScale;

public class Helix extends Icon3D {

	private final static String TITLE = "Helix";
	
	private final static ColorScale[] colorScales = new ColorScale[] {
//		ColorScale.fromColors(ColorScale.IDENTIFY_COLORS[0]),
//		ColorScale.fromColors(ColorScale.IDENTIFY_COLORS[1]),
//		ColorScale.fromColors(ColorScale.IDENTIFY_COLORS[2])
		ColorScale.fromColors(Colors.colorSchemes[0]),
		ColorScale.fromColors(Colors.colorSchemes[1]),
		ColorScale.fromColors(Colors.colorSchemes[2])
	};

	private final static int PRECISION = 30; // How detailed should the approximation of the helix be

	private final HashMap<Area, DataFetcher> dataFetchers = new HashMap<Area, DataFetcher>();

	private JPanel settings = null;

	private float rotationAngle = 0;

	private float height = 700f;

	private float perimeter = 80f;

	private float ribbonScale = 0.8f;

	private float subRibbonScale = 1f;

	private int timeStepsPerCycle = 7;

	boolean spacialChange = false;

	boolean temporalChange = false;

	boolean diagChange = false;

	@Override
	public JComponent getControlComponent() {
		final SliderSpinner rotationAdjuster = new SliderSpinner("Rotation", 0, 360, (int) rotationAngle);
		rotationAdjuster.addChangeListener(new ChangeListener() {
			@Override
			public void stateChanged(ChangeEvent e) {
				rotationAngle = rotationAdjuster.getValue();
				getMapView().repaint();
			}
		});

		final SliderSpinner heightAdjuster = new SliderSpinner("Height", 0, 999, (int) height);
		heightAdjuster.addChangeListener(new ChangeListener() {
			@Override
			public void stateChanged(ChangeEvent e) {
				height = heightAdjuster.getValue();
				getMapView().repaint();
			}
		});

		final SliderSpinner perimeterAdjuster = new SliderSpinner("Perimeter", 0, 499, (int) perimeter);
		perimeterAdjuster.addChangeListener(new ChangeListener() {
			@Override
			public void stateChanged(ChangeEvent e) {
				perimeter = perimeterAdjuster.getValue();
				getMapView().repaint();
			}
		});

		final SliderSpinner ribbonScaleAdjuster = new SliderSpinner("Ribbon Scale", 0, 100, (int) (ribbonScale * 100));
		ribbonScaleAdjuster.addChangeListener(new ChangeListener() {
			@Override
			public void stateChanged(ChangeEvent e) {
				ribbonScale = ribbonScaleAdjuster.getValue() / 100f;
				getMapView().repaint();
			}
		});

		final SliderSpinner subRibbonScaleAdjuster = new SliderSpinner("Sub-Ribbon Scale", 0, 100, (int) (subRibbonScale * 100));
		subRibbonScaleAdjuster.addChangeListener(new ChangeListener() {
			@Override
			public void stateChanged(ChangeEvent e) {
				subRibbonScale = subRibbonScaleAdjuster.getValue() / 100f;
				getMapView().repaint();
			}
		});

		final SliderSpinner timeStepsPerCycleAdjuster = new SliderSpinner("Time Steps per Helix Cycle", 1, 999, timeStepsPerCycle);
		timeStepsPerCycleAdjuster.addChangeListener(new ChangeListener() {
			@Override
			public void stateChanged(ChangeEvent e) {
				timeStepsPerCycle = timeStepsPerCycleAdjuster.getValue();
				getMapView().repaint();
			}
		});

		if (settings == null) {
			settings = new JPanel();
			settings.setLayout(new BoxLayout(getControlComponent(), BoxLayout.Y_AXIS));
			settings.add(rotationAdjuster);
			settings.add(heightAdjuster);
			settings.add(perimeterAdjuster);
			settings.add(ribbonScaleAdjuster);
			settings.add(subRibbonScaleAdjuster);
			settings.add(timeStepsPerCycleAdjuster);
			settings.add(Box.createVerticalGlue());
		}

		return settings;
	}

	@Override
	public String getTitle() {
		return TITLE;
	}

	@Override
	public void spatialSelectionChanged(SpatialSelectionChangeEvent e) {
		// Check if spatial selection change requires a data update
		if (e.hasActiveAreaChanged()) return;

		boolean doUpdate = false;
		SpatialSelectionModel ssm = (SpatialSelectionModel) e.getSource();
		for (Area a : ssm.getSelectedAreas()) {
			if ((a.getLevel() == ssm.getLevel()) && (!a.hasData(this))) {
				doUpdate = true;
				break;
			}
		}

		if (e.hasLevelChanged()) {
			level = ssm.getLevel();
			clearData();
			doUpdate = true;
			spacialChange = true;
		}

		if (doUpdate) {
			update();
		}
	}

	@Override
	public void temporalSelectionChanged(TemporalSelectionChangeEvent e) {
		// Check if temporal selection change requires a data update
		boolean doUpdate = false;
		int newPeriodBegin = ((TemporalSelectionModel) e.getSource()).getBeginPeriodNumber();
		if (periodBeginId != newPeriodBegin) {
			periodBeginId = newPeriodBegin;
			doUpdate = true;
		}

		int newPeriodEnd = ((TemporalSelectionModel) e.getSource()).getEndPeriodNumber();
		if (periodEndId != newPeriodEnd) {
			periodEndId = newPeriodEnd;
			doUpdate = true;
		}

		Granularity newGranularity = ((TemporalSelectionModel) e.getSource()).getGranularity();
		if (!granularity.equals(newGranularity)) {
			granularity = newGranularity;
			doUpdate = true;
		}

		if (doUpdate) {
			clearData();
			temporalChange = true;
			update();
		}
	}

	@Override
	public void valueChanged(ListSelectionEvent e) {
		// Check if diagnosis selection change requires a data update
		diagnosisIds = ((DiagnosisSelectionModel) e.getSource()).getSelectedDiagnoses();
		clearData();
		diagChange = true;
		update();
	}

	@Override
	protected void updateSelection() {
		level = getMapView().getSpatialSelection().getLevel();
		periodBeginId = getMapView().getTemporalSelection().getBeginPeriodNumber();
		periodEndId = getMapView().getTemporalSelection().getEndPeriodNumber();
		granularity = getMapView().getTemporalSelection().getGranularity();
		diagnosisIds = getMapView().getDiagnosisSelection().getSelectedDiagnoses();
	}

	@Override
	public void update() {

		SpatialSelectionModel ssm = getMapView().getSpatialSelection();
		for (Area a : ssm.getSelectedAreas(level)) {
			synchronized (SynchroLock) {
				if (!a.hasData(this) && !dataFetchers.containsKey(a) && (getMapView().getActiveIcon() == this)) {
					dataFetchers.put(a, new DataFetcher(a, diagnosisIds, periodBeginId, periodEndId, granularity));
					SwingWorkerScheduler.getInstance().enqueueTask(dataFetchers.get(a));
				}
			}
		}
		if (diagChange || temporalChange || spacialChange) {
			getMapView().getFadingManager().setFadeOutAll();
			getMapView().getFadingManager().setNeedUpdateAll();
			diagChange = false;
			temporalChange = false;
			spacialChange = false;
		}
	}

	private void clearData() {
		for (Area a : getMapView().getMap().getAreas()) {
			synchronized (SynchroLock) {
				if (dataFetchers.containsKey(a)) {
					dataFetchers.remove(a).cancel(false);
				}
				a.deleteData(this);
			}
		}
	}

	@Override
	protected void drawIcon(Area a) {

		synchronized (SynchroLock) {
			RenderingContext rc = getRenderingContext();
			// Draw Helix
			rc.gl.glEnable(GL.GL_BLEND);
			rc.gl.glEnable(GL.GL_DEPTH_TEST);
			rc.gl.glTranslated(a.getBounds().getCenterX(), a.getBounds().getCenterY(), 0);

			rc.gl.glScalef(perimeter, perimeter, 1);
			rc.gl.glRotatef(rotationAngle, 0, 0, 1);

			int data[][] = a.getData(this);
			if (data == null) return;
			int timeStepCount = data.length;
			int diagnosesCount = data[0].length;

			float[] maxPerDiagnosis = new float[diagnosesCount];
			for (int d = 0; d < diagnosesCount; d++) {
				for (int i = 0; i < timeStepCount; i++) {
					if (data[i][d] > maxPerDiagnosis[d]) maxPerDiagnosis[d] = data[i][d];
				}
			}

			int quadsPerTimeStep = 1 + PRECISION / timeStepsPerCycle; // At least one quad per time step
			int quadsPerCycle = quadsPerTimeStep * timeStepsPerCycle;

			float cycleCount = (float) timeStepCount / timeStepsPerCycle;
			float transparency = getMapView().getFadingManager().getTransparency(a);
			float ribbonHeight = height / (1 + cycleCount);
			float subRibbonHeight = ribbonHeight * ribbonScale / diagnosesCount;

			// h = hs * ts * qt + rh
			// h - rh = hs * ts * qt
			// (h - rh)
			// ------ = hs
			// (ts * qt)
			float heightStepPerQuad = (height - ribbonHeight) / (timeStepCount * quadsPerTimeStep);
			float angleStepPerQuad = 360f / quadsPerCycle;
			float sin = (float) Math.sin(angleStepPerQuad * Math.PI / 180);
			float cos = (float) (-1 * Math.cos(angleStepPerQuad * Math.PI / 180));

			rc.gl.glMatrixMode(GL.GL_MODELVIEW);
			for (int i = 0; i < timeStepCount; i++) {
				for (int j = 0; j < quadsPerTimeStep; j++) {
					rc.gl.glPushMatrix();
					for (int d = 0; d < diagnosesCount; d++) {
						float t = data[i][d] / maxPerDiagnosis[d];
						colorScales[d % colorScales.length].getColor(t).getColorComponents(rc.c);
						rc.c[3] = transparency;
						rc.gl.glColor4fv(rc.c, 0);

						rc.gl.glBegin(GL.GL_QUADS);
						rc.gl.glVertex3f(0, -1, 0);
						rc.gl.glVertex3f(0, -1, subRibbonHeight * subRibbonScale);
						rc.gl.glVertex3f(sin, cos, subRibbonHeight * subRibbonScale + heightStepPerQuad);
						rc.gl.glVertex3f(sin, cos, heightStepPerQuad);
						rc.gl.glEnd();

						rc.gl.glTranslatef(0, 0, subRibbonHeight);
					}
					rc.gl.glPopMatrix();
					rc.gl.glRotatef(angleStepPerQuad, 0, 0, 1);
					rc.gl.glTranslatef(0, 0, heightStepPerQuad);
				}
			}
		}
	}

	class DataFetcher extends SwingWorkerEx<int[][], int[][]> {

		int[][] data;

		final Area area;

		final int[] diagnosisIds;

		final int periodBeginId;

		final int periodEndId;

		final Granularity granularity;

		public DataFetcher(Area a, int[] d, int b, int e, Granularity g) {
			area = a;
			diagnosisIds = d;
			periodBeginId = b;
			periodEndId = e;
			granularity = g;
		}

		@Override
		protected int[][] doInBackground() throws Exception {
			System.out.println("Helix Data Update Requested for Area " + area.getId());

			setProgressEx(0);
			setMessage("Querying data for area " + area.getId() + "...");

			int timeStepCount = DB.getPeriodCountForInterval(granularity, periodBeginId, periodEndId);
			int diagnosisCount = diagnosisIds.length;

			data = new int[timeStepCount][diagnosisCount];

			Statement stmt;
			String query;
			ResultSet res;

			try {
				stmt = DB.getConnection().createStatement();

				int di = 0;

				for (int diagnosisId : diagnosisIds) {

					query = " SELECT c.count " + " FROM cases c" + " WHERE c.period = '" + granularity + "' " + " AND c.diagnosisId = " + diagnosisId + " AND c.periodId >= " + periodBeginId + " AND c.periodId <= " + periodEndId + " AND c.areaId = " + area.getCode() + " ORDER BY c.periodId";
					// System.out.println(query);
					res = stmt.executeQuery(query);
					int pi = 0;
					while (res.next()) {
						int count = res.getInt(1);
						data[pi][di] = count;
						pi++;
					}

					di++;
				}
			}
			catch (SQLException e) {
				e.printStackTrace();
				return null;
			}

			return data;
		}

		@Override
		protected void done() {
			super.done();
			synchronized (SynchroLock) {
				try {
					if (!isCancelled()) {
						final int[][] data = this.get();
						if (data != null) {
							area.setData(Helix.this, data);
						}
					}
				}
				catch (Exception ex) {
					ex.printStackTrace();
				}
				finally {
					dataFetchers.remove(area);
				}
			}
			getMapView().repaint();
		}
	}

}
