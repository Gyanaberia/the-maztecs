package com.example.notif

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import com.pusher.pushnotifications.PushNotifications;

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        PushNotifications.start(getApplicationContext(), "e5e2e6cd-9f3b-449e-a850-3931a46fedc0")
        PushNotifications.addDeviceInterest("hello")
    }
}