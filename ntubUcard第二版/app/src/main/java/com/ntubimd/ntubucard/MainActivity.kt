package com.ntubimd.ntubucard

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import androidx.fragment.app.Fragment
import com.ntubimd.ntubucard.databinding.ActivityMainBinding

class MainActivity : AppCompatActivity() {
    private lateinit var binding: ActivityMainBinding
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding =  ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)
        replaceFragment(home())
        binding.bottomNavigationView.setOnItemReselectedListener {
            when(it.itemId){
                R.id.home -> replaceFragment(home())
                R.id.details -> replaceFragment(details())
                R.id.profilecircle -> replaceFragment(profilecircle())
                else ->{
                }
            }
            true
        }
        }
        private fun replaceFragment(fragment : Fragment){

            val fragmentManager = supportFragmentManager
            val  fragmentTransition = fragmentManager.beginTransaction()
            fragmentTransition.replace(R.id.frame_layout,fragment)
            fragmentTransition.commit()

    }
}