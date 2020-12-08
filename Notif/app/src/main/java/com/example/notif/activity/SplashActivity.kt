package com.example.notif.activity

import android.content.Intent
import android.os.Bundle
import android.os.Handler
import androidx.appcompat.app.AppCompatActivity
import com.example.notif.R

class SplashActivity:AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.splash)

        supportActionBar!!.hide()

        // we used the postDelayed(Runnable, time) method
        // to send a message with a delayed time.
        Handler().postDelayed({
            var sp=getSharedPreferences("login", MODE_PRIVATE)
            if(sp.getBoolean("logged",false)){
                val intent = Intent(this, MainActivity::class.java)
                startActivity(intent)
                //finish()
            }
            else{
                val intent = Intent(this, LoginActivity::class.java)
                startActivity(intent)
            }
        }, 2000) // 2000 is the delayed time in milliseconds.


    }
}