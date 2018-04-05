package com.example.brett.Robot_Control;

import android.content.Context;
import android.os.Build;
import android.os.Handler;
import android.os.Looper;
import android.os.Message;
import android.speech.tts.TextToSpeech;
import android.util.Log;
import android.widget.Toast;

import java.util.Locale;

/**
 * Created by Brett on 3/27/2018.
 * With help from Johnny
 */

public class TTS extends Thread implements TextToSpeech.OnInitListener {
    private static final String TAG = "TTS";

    private TextToSpeech tts;
    private Context context;
    public Handler h;
    private String last;

    TTS(Context con) {
        context = con;
        last = "";
        tts = new TextToSpeech(context, this);
    }

    public void onInit(int i) {
        if (i == TextToSpeech.SUCCESS) {
            // set language to U.S. English
            tts.setLanguage(Locale.US);
        } else if (i == TextToSpeech.ERROR) {
            Toast.makeText(context, "Text to Speech failed.", Toast.LENGTH_LONG).show();
        }
    }

    public void run() {
        Looper.prepare();
        h = new Handler() {
            public void handleMessage(Message msg) {
                String msg_data = msg.getData().getString("TT");
                String[] msg_parts = msg_data.split(":");
                float pitch = Float.parseFloat(msg_parts[0])/(float)10.0;
                float speed = Float.parseFloat(msg_parts[1])/(float)10.0;
                tts.setPitch(pitch);
                tts.setSpeechRate(speed);
                String msg_out = msg_parts[2];
                Log.d(TAG, msg_data);
                speak(msg_out);
            }
        };
        Looper.loop();
    }

    public void speak(String words) {
        if (last != words) {
            last = words;
            if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.LOLLIPOP) {
                tts.speak(words, TextToSpeech.QUEUE_FLUSH, null, null);
            } else {
                tts.speak(words, TextToSpeech.QUEUE_FLUSH, null);
            }

            while (tts.isSpeaking()) {
                try {
                    Thread.sleep(200);
                } catch (Exception e) {
                    Log.e(TAG,e.toString());
                }
            }
        }
    }
}
