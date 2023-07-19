package com.djangounchained.bigbrother;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;

public class ClassroomActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_classroom);
    }

    public void pdfListFunction(View view) {

        Intent intent = new Intent(this,PdflistActivity.class);
        startActivity(intent);
    }
}