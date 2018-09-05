import javax.swing.*;
import java.awt.*;

public class MyFrame {
    public static void main(String[] args){
        EventQueue.invokeLater(()->{
//            AlgoFrame frame = new AlgoFrame("welcome", 500, 500);
            AlgoFrame frame = new AlgoFrame("welcome");
        });

    }
}
