import java.applet.*;
import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

public class  AppletInOut8 extends JApplet
{
	JTextField in = new JTextField(10);
	JButton btn = new JButton("��ƽ����");
	JLabel out = new JLabel("������ʾ����ı�ǩ");

	public void init()
	{
		setLayout( new FlowLayout() );
		add( in );
		add( btn );
		add( out );
		btn.addActionListener( e->{
			String s = in.getText();
			double d = Double.parseDouble( s );
			double sq = Math.sqrt(d);
			out.setText( d + "��ƽ�����ǣ�" + sq );
		});
	}
}
