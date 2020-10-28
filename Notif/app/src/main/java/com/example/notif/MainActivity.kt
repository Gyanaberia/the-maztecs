package com.example.notif

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import com.pusher.pushnotifications.PushNotifications;

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        PushNotifications.start(getApplicationContext(), "12b1d692-e909-4c13-ab01-9aa733055d56");
        PushNotifications.addDeviceInterest("hello");
    }
}