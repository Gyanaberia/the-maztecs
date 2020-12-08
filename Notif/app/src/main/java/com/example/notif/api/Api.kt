package com.example.notif.api

import com.example.notif.model.CourseInfo
import com.example.notif.model.StudentInfo
import retrofit2.Call
import retrofit2.http.Body
import retrofit2.http.POST

interface Api {

    @POST("api/users")
    fun checkCourse(@Body userData: CourseInfo) :Call<CourseInfo>

    @POST("student")
    fun addStudent(@Body studentData:StudentInfo) : Call<StudentInfo>
}