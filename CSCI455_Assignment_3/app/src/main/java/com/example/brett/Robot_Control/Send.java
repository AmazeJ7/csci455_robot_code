package com.example.brett.Robot_Control;

import android.os.Looper;
import java.io.IOException;
import java.io.OutputStream;
import java.io.PrintWriter;
import java.net.Socket;
import android.os.Handler;
import android.os.Message;

/**
 * Created by Johnny on 4/4/2018.
 */

public class Send implements Runnable{
    Socket s;
    PrintWriter pw;
    Handler h;

    public Send(Socket s) {this.s = s;}

    public void run() {
        try {
            pw = new PrintWriter(s.getOutputStream(), true);
        } catch (IOException e) {
            e.printStackTrace();
        }

        Looper.prepare();
        h = new Handler() {
            public void handleMessage(Message msg) {
                String send = msg.getData().getString("S");
                pw.print(send);
                pw.flush();
            }
        };
        Looper.loop();
    }
}
