package com.example.brett.Robot_Control;

import android.os.Bundle;
import android.os.Handler;
import android.os.Looper;
import android.os.Message;
import java.net.Socket;

/**
 * Created by Brett on 3/28/2018.
 */

public class Network implements Runnable{
    TTS tts;
    Socket s;
    Send send;
    Receive r;
    Handler h;

    public Network(TTS tts) {
        this.tts = tts;
    }

    @Override
    public void run(){
        try{
            s = new Socket("10.152.171.167", 9999);
        }catch(Exception e){
            e.printStackTrace();
        }

        r = new Receive(s, tts);
        Thread rt = new Thread(r);
        rt.start();

        send = new Send(s);
        Thread st = new Thread(send);
        st.start();

        Looper.prepare();
        h = new Handler() {
            public void handleMessage(Message msg) {
                String msg_send = msg.getData().getString("N");
                Message m = send.h.obtainMessage();
                Bundle b = new Bundle();
                b.putString("S", msg_send);
                m.setData(b);
                send.h.sendMessage(m);
            }
        };
        Looper.loop();

    }
}
