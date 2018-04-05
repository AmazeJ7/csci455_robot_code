package com.example.brett.Robot_Control;

import android.app.Activity;
import android.content.ActivityNotFoundException;
import android.content.Context;
import android.content.Intent;
import android.os.Bundle;
import android.os.Handler;
import android.os.Looper;
import android.os.Message;
import android.speech.RecognizerIntent;
import android.util.Log;

import java.util.ArrayList;
import java.util.Locale;

import static android.app.Activity.RESULT_OK;

/**
 * Created by Brett on 4/5/2018.
 */

public class STT extends Activity implements Runnable{
    private static final int REQ_CODE_SPEECH_INPUT = 1;
    TTS tts;
    Context context;
    private static final String TAG = "STT";
    Network network;
    Handler h;

    STT(Context context, TTS tts){
        this.tts = tts;
        this.context = context;
        network = new Network(tts);
        Thread net = new Thread(network);
        net.start();
    }


    @Override
    public void run() {
        Looper.prepare();
        h = new Handler() {
            public void handleMessage(Message msg) {
                startVoiceInput();
            }
            };
        Looper.loop();
    }

    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        super.onActivityResult(requestCode, resultCode, data);
        switch (requestCode) {
            case REQ_CODE_SPEECH_INPUT: {
                Log.d(TAG, "voice recieved");
                if (resultCode == RESULT_OK && null != data) {
                    ArrayList<String> result = data.getStringArrayListExtra(RecognizerIntent.EXTRA_RESULTS);
                    sendOnNetwork(result.get(0));
                    //TODO: send back to MainActivity
                }
                break;
            }
        }
    }

    public void sendOnNetwork(String msg) {
        Message toClient = network.h.obtainMessage();
        Bundle n = new Bundle();
        n.putString("N", msg);
        toClient.setData(n);
        network.h.sendMessage(toClient);
    }


    private void startVoiceInput() {
        Intent intent = new Intent(RecognizerIntent.ACTION_RECOGNIZE_SPEECH);
        intent.putExtra(RecognizerIntent.EXTRA_LANGUAGE_MODEL, RecognizerIntent.LANGUAGE_MODEL_FREE_FORM);
        intent.putExtra(RecognizerIntent.EXTRA_LANGUAGE, Locale.getDefault());
        intent.putExtra(RecognizerIntent.EXTRA_PROMPT, "Say a command");
        //intent.putExtra(RecognizerIntent.EXTRA_SPEECH_INPUT_COMPLETE_SILENCE_LENGTH_MILLIS, 1000);
        try {
            startActivityForResult(intent, REQ_CODE_SPEECH_INPUT);
        } catch (ActivityNotFoundException e) {
            e.printStackTrace();
        }
    }


}
