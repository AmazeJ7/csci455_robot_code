package com.example.brett.Robot_Control;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.Socket;
import android.os.Bundle;
import android.os.Message;

/**
 * Created by Johnny on 4/4/2018.
 */

public class Receive implements Runnable{
    Socket s;
    BufferedReader b;
    TTS tts;
    MainActivity m;

    public Receive(Socket s, TTS tts, MainActivity m) {this.tts = tts; this.s = s; this.m = m;}

    @Override
    public void run() {
        try {
            b = new BufferedReader(new InputStreamReader(s.getInputStream()));
            while(true) {
                String rec = b.readLine();
                System.out.println("pad"+rec+"pad");
                if (rec.equals("get speech")) {
                    m.h.sendEmptyMessage(0);
                } else if (rec != null) {
                    Message msg = Message.obtain(tts.h);
                    Bundle b = new Bundle();
                    b.putString("TT", "10:10:" + rec);
                    msg.setData(b);
                    tts.h.sendMessage(msg);
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
