package com.djangounchained.bigbrother;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;

public class RegistrationActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_registration);
        //getSupportActionBar().setTitle("Registration Form");
    }



    public void registrationFunction(View view) {

        Intent intent = new Intent(this,ClassesActivity.class);
        startActivity(intent);
    }

    public void loginPortal(View view) {

        Intent intent = new Intent(this,LoginActivity.class);
        startActivity(intent);
    }
}