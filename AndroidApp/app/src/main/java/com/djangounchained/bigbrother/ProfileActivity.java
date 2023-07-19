package com.djangounchained.bigbrother;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;

public class ProfileActivity extends BaseActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

    }

    @Override
    int getLayoutId() {
        return R.layout.activity_profile;
    }

    @Override
    int getBottomNavigationMenuItemId() {
        return R.id.action_profile;
    }
}