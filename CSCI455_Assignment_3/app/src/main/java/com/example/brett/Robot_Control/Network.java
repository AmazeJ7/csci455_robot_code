package com.example.brett.Robot_Control;

import android.os.Bundle;
import android.os.Message;
import android.util.Log;
import android.widget.EditText;

import java.io.BufferedReader;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;

/**
 * Created by Brett on 3/28/2018.
 */

public class Network extends Thread{
    TTS tts;

    public Network(TTS tts) {
        this.tts = tts;
    }

    @Override
    public void run(){
        try{
            Socket s = new Socket("192.168.1.214", 9999);
            BufferedReader input = new BufferedReader(new InputStreamReader(s.getInputStream()));
            PrintWriter output = new PrintWriter(s.getOutputStream(), true);
            while(true) {
                String in = input.readLine();
                if (in != null) {
                    Message rec = tts.handler.obtainMessage();
                    Bundle b = new Bundle();
                    b.putString("TT", in);
                    rec.setData(b);
                    tts.handler.sendMessage(rec);
                }
                output.print("asdfasdf");
                output.flush();
            }
        }catch(Exception e){
            e.printStackTrace();
        }
    }
}
