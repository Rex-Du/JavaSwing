import javax.swing.*;
import java.awt.*;
import java.awt.geom.Ellipse2D;

public class AlgoFrame extends JFrame {
    private int canvasWidth;
    private int canvasHight;

    public AlgoFrame(String title, int canvasWidth, int canvasHeight){
        super(title);
        this.canvasWidth = canvasWidth;
        this.canvasHight = canvasHeight;

        AlgoCanvas canvas = new AlgoCanvas();
//        canvas.setPreferredSize(new Dimension(canvasWidth, canvasHeight));
        setContentPane(canvas);
        pack(); //使窗口的大小等于画布的大小
        //        setSize(canvasWidth, canvasHeight);
        setResizable(false);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setVisible(true);
    }

    public AlgoFrame(String title){
        this(title, 1024, 768);
    }

    public int getCanvasWidth(){return this.canvasWidth;}
    public int getCanvasHight(){return this.canvasHight;}

    private class AlgoCanvas extends JPanel{
        @Override
        public void paintComponent(Graphics g){
            super.paintComponent(g);
//            g.drawOval(50,50,300,300);
            Graphics2D g2d = (Graphics2D) g;
            //抗锯齿
            RenderingHints hints = new RenderingHints(RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_ON);
            g2d.addRenderingHints(hints);

            AlgoVisHelper.setStrokeWidth(g2d,5);

            AlgoVisHelper.setColor(g2d,Color.red);
            AlgoVisHelper.fillCircle(g2d, 200,200, 140);

            AlgoVisHelper.setColor(g2d,Color.blue);
            AlgoVisHelper.strokeCircle(g2d, 200,200, 150);

        }
        @Override
        public Dimension getPreferredSize(){
            return new Dimension(canvasWidth,canvasHight);
        }
    }
}
