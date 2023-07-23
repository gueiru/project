package com.ntubimd.a7ucard

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import com.ntubimd.a7ucard.databinding.ActivityMainBinding
import android.content.Intent


class MainActivity : AppCompatActivity() {
    private lateinit var binding: ActivityMainBinding
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(R.layout.activity_main)
        binding.login.setOnClickListener {
            val intent = Intent(this@MainActivity, SecondActivity::class.java)
            startActivity(intent)
        }
    }
}