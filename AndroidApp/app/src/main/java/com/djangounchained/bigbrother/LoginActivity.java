package com.djangounchained.bigbrother;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;

public class LoginActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login);
    }

    public void loginFunction(View view) {

        Intent intent = new Intent(this,ClassesActivity.class);
        startActivity(intent);
    }

    public void registrationPortal(View view) {

        Intent intent = new Intent(this,RegistrationActivity.class);
        startActivity(intent);
    }
}