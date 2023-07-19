package com.djangounchained.bigbrother;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;

public class MainActivity extends BaseActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);


    }

    public void loginPortal(View view) {

        Intent intent = new Intent(this,LoginActivity.class);
        startActivity(intent);
    }


    public void registrationPortal(View view) {

        Intent intent = new Intent(this,RegistrationActivity.class);
        startActivity(intent);
    }
    @Override
    int getLayoutId() {
        return R.layout.activity_main;
    }

    @Override
    int getBottomNavigationMenuItemId() {
        return R.id.action_main;
    }
}