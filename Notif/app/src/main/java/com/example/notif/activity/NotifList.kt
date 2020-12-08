package com.example.notif.activity

import android.os.Bundle
import android.util.Log
import com.google.android.material.appbar.CollapsingToolbarLayout
import com.google.android.material.floatingactionbutton.FloatingActionButton
import com.google.android.material.snackbar.Snackbar
import androidx.appcompat.app.AppCompatActivity
import com.example.notif.R
import com.example.notif.model.DataBaseHandler

class NotifList : AppCompatActivity() {
    var db:DataBaseHandler?=null
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_notif_list)
        setSupportActionBar(findViewById(R.id.toolbar))
        val course_title=intent.getStringExtra("course_name")
        findViewById<CollapsingToolbarLayout>(R.id.toolbar_layout).title =course_title
        Log.d("notifList",course_title!!)
    }
    fun addNotif(){
        var db=DataBaseHandler(this)
        

    }

}