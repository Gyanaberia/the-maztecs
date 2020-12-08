package com.example.notif.services

import android.util.Log
import com.example.notif.model.DataBaseHandler
import com.example.notif.model.Notification
import com.google.firebase.messaging.RemoteMessage
import com.pusher.pushnotifications.fcm.MessagingService

class NotificationsMessagingService : MessagingService() {
    override fun onMessageReceived(remoteMessage: RemoteMessage) {
        Log.d("Message received",
            "Message received: " +
                    "Title: \"${remoteMessage.notification?.title}\"" +
                    "Body \"${remoteMessage.notification}\""
        )
        val notify=Notification(null,null,null,null,null)
        notify.date=remoteMessage.data["date"]
        notify.title=remoteMessage.notification?.title
        notify.body=remoteMessage.notification?.body
        notify.course=remoteMessage.data["course"]

        var db=DataBaseHandler(this)//context maybe null
        db.insertData(notify,notify.course)
        /*val notificationLayout = RemoteViews(packageName, R.layout.notification_small)
        val customNotification = NotificationCompat.Builder(this ,"hello")
            .setSmallIcon(R.drawable.notification_icon)
            .setStyle(NotificationCompat.DecoratedCustomViewStyle())
            .setCustomContentView(notificationLayout)
            .setContentTitle(title)
            .setContentText(body)
            .setAutoCancel(true)
            .setContentIntent(PendingIntent?)
            .build()*/

    }
    // This method is only for integrating with other 3rd party services.
    // For most use cases you can omit it.
}