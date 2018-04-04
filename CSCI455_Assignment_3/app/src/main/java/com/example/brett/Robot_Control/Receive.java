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

    public Receive(Socket s, TTS tts) {this.tts = tts; this.s = s;}

    @Override
    public void run() {
        try {
            b = new BufferedReader(new InputStreamReader(s.getInputStream()));
            while(true) {
                String rec = b.readLine();
                System.out.println("Received " + rec);


                if (rec != null) {
                    Message msg = tts.handler.obtainMessage();
                    Bundle b = new Bundle();
                    b.putString("TT", rec);
                    msg.setData(b);
                    tts.handler.sendMessage(msg);
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
