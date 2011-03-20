package landvis.technique;

import java.util.ArrayList;

import javax.media.opengl.GL;

import landvis.model.Area;
import landvis.model.TemporalSelectionModel.Granularity;
import landvis.util.RenderingContext;

public abstract class Icon3D extends Technique implements RenderableIcon{

	protected RenderingContext rc;

	protected int level = -1;

	protected int[] diagnosisIds = new int[] {};

	protected int periodBeginId = -1;

	protected int periodEndId = -1;

	protected Granularity granularity = Granularity.Day;

	private int resize = 15;

	@Override
	public boolean isSelectable() {
		return true;
	}

	public void setRenderingContext(RenderingContext rc) {
		this.rc = rc;
	}

	public RenderingContext getRenderingContext() {
		return rc;
	}

	public void setResize(int r) {
		this.resize = r;
	}

	public int getResize() {
		return resize;
	}

	public void drawIcons() {
		ArrayList<Area> areasToDraw = (getMapView().getSpatialSelection().getSelectedAreas(getMapView().getSpatialSelection().getLevel()));

		getMapView().getFadingManager().updateAreaSelection(areasToDraw, this);

		// TODO: Sort areas to draw such that transparent icons are rendered back to front

		for (Area a : areasToDraw) {
			// Store current model view matrix
			rc.gl.glMatrixMode(GL.GL_MODELVIEW);
			rc.gl.glPushMatrix();
			rc.gl.glLoadIdentity();
			getMapView().lookAt();

			drawIcon(a);

			// Restore model view matrix
			rc.gl.glMatrixMode(GL.GL_MODELVIEW);
			rc.gl.glPopMatrix();
		}

		// Restore model view matrix

	}

	protected abstract void drawIcon(Area a);

}
