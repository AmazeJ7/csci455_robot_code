
package com.example.brett.Robot_Control;

import android.content.ActivityNotFoundException;
import android.os.Handler;
import android.os.Message;
import android.speech.tts.TextToSpeech;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ImageButton;
import android.content.Intent;
import android.speech.RecognizerIntent;
import java.util.ArrayList;
import java.util.Locale;


public class MainActivity extends AppCompatActivity implements View.OnClickListener {

    private static final String TAG = "Robot Control";
    TTS tts;
    Network n;
    Handler h;
    private static final int MY_DATA_CHECK_CODE = 0; // check user data for TTS
    private static final int REQ_CODE_SPEECH_INPUT = 1;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // Buttons
        Button connectBtn = (Button) findViewById(R.id.connect);
        connectBtn.setOnClickListener(this);
        ImageButton micBtn = (ImageButton) findViewById(R.id.micBtn);
        micBtn.setOnClickListener(this);

        // create intent for TTS
        Intent checkTTSIntent = new Intent();
        // set intent action to check TTS data
        checkTTSIntent.setAction(TextToSpeech.Engine.ACTION_CHECK_TTS_DATA);
        // start above action, passing in check data variable
        startActivityForResult(checkTTSIntent, MY_DATA_CHECK_CODE);

        tts = new TTS(this);
        tts.start();

        h = new Handler() {
            public void handleMessage(Message msg) {
                startVoiceInput();
            }
        };
    }

    public void onClick(View v) {
        switch (v.getId()){
            case R.id.connect:
                EditText ip_text = findViewById(R.id.textBox);
                String ip = ip_text.getText().toString();
                n = new Network(ip, tts, this);
                Thread net = new Thread(n);
                net.start();
                break;
            case R.id.micBtn:
                Log.d(TAG,"mic button pressed");
                startVoiceInput();
                break;
        }
    }

    public void startVoiceInput() {
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

    public void sendOnNetwork(String msg) {
        Message toClient = n.h.obtainMessage();
        Bundle b = new Bundle();
        b.putString("N", msg);
        toClient.setData(b);
        n.h.sendMessage(toClient);
    }

    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        super.onActivityResult(requestCode, resultCode, data);

        switch (requestCode) {
            case REQ_CODE_SPEECH_INPUT: {
                Log.d(TAG, "voice recieved");
                if (resultCode == RESULT_OK && null != data) {
                    ArrayList<String> result = data.getStringArrayListExtra(RecognizerIntent.EXTRA_RESULTS);
                    sendOnNetwork(result.get(0));
                }
                break;
            }
        }
    }
}
