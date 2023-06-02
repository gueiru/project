package com.example.myapplication;

import androidx.appcompat.app.AppCompatActivity;

import android.annotation.SuppressLint;
import android.location.Address;
import android.location.Geocoder;
import android.Manifest;
import android.app.AlertDialog;
import android.content.Intent;
import android.content.pm.PackageManager;
import android.location.Criteria;
import android.location.Location;
import android.location.LocationListener;
import android.location.LocationManager;
import android.os.Build;
import android.os.Bundle;
import android.provider.Settings;
import android.util.Log;
import android.view.View;
import android.widget.TextView;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.io.IOException;

import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.Response;


public class MainActivity extends AppCompatActivity implements LocationListener{
    private static final int PERMISSIONS_REQUEST_GPS = 101;
    private TextView output;
    private LocationManager lc;
    private String date;

    String str = new String();

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        output = (TextView) findViewById(R.id.lblOutput);
        lc = (LocationManager)getSystemService(LOCATION_SERVICE);  //取得定位服務的LocationManager物件
        if(!lc.isProviderEnabled(LocationManager.GPS_PROVIDER)){
            AlertDialog.Builder builder = new AlertDialog.Builder(this);
            builder.setTitle("定位管理").setMessage("GPS權限尚未取得.\n請先啟用GPS?").setPositiveButton("確定",null).show();
        }
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.M && checkSelfPermission(Manifest.permission.ACCESS_FINE_LOCATION) != PackageManager.PERMISSION_GRANTED){
            requestPermissions(new String[]{Manifest.permission.ACCESS_FINE_LOCATION}, PERMISSIONS_REQUEST_GPS);
        }
    }
    @Override
    public void onRequestPermissionsResult(int requestCode, String[] permissions,
                                           int[] grantResults) {
        super.onRequestPermissionsResult(requestCode, permissions, grantResults);
        if (requestCode == PERMISSIONS_REQUEST_GPS) {
            if (grantResults[0] == PackageManager.PERMISSION_GRANTED) {
                // 已經取得權限
                output.setText("取得權限取得GPS資訊");
            } else {
                output.setText("直到取得權限, 否則無法取得GPS資訊");
            }
        }
    }
    @Override
    protected void onResume() {
        super.onResume();
        int minTime = 1000; // 毫秒
        float minDistance = 1; // 公尺
        try {  // 取得最佳的定位者
            String best = lc.getBestProvider(new Criteria(), true);
            if (best != null) {   // 註冊更新的傾聽者物件
                lc.requestLocationUpdates(best, minTime, minDistance, this);
            }
            else
                output.setText("請確認開啟GPS");
        }
        catch(SecurityException sex) {
            Log.e("定位經緯度", "GPS權限失敗..." + sex.getMessage());
        }
    }
    @Override
    protected void onPause() {
        super.onPause();
        try {  // 取消註冊更新的傾聽者物件
            lc.removeUpdates(this);
        }
        catch(SecurityException sex) {
            Log.e("定位經緯度", "GPS權限失敗..." + sex.getMessage());

        }
    }
    private final int MAX = 5;
    @SuppressLint("SetTextI18n")
    @Override
    public void onLocationChanged(Location location) {
        double lat, lng;
        if (location != null) {
            // 取得經緯度
            lat = location.getLatitude();
            lng = location.getLongitude();
            String p = "定位位置：\n緯度: " + lat + "  經度: " + lng + "\n\n";
            output.setText(p);
            String mapurl  = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=" + lat + "," + lng + "&radius=50&language=zh-TW&key=AIzaSyAThITj4VJjfIUrknta6HdlLZaySkz_e1M";
            okhttpdata(mapurl);
            new Thread(new Runnable() {
                @Override
                public void run() {
                    try {
                        Thread.sleep(1000);
                    } catch (InterruptedException e) {
                        throw new RuntimeException(e);
                    }
                }
            }).start();
            System.out.println(str);
        }
    }
    @Override
    public void onStatusChanged(String s, int i, Bundle bundle) {  }
    @Override
    public void onProviderEnabled(String s) {  }
    @Override
    public void onProviderDisabled(String s) {  }
    // 啟動設定程式來更改GPS設定
    public void button_Click(View view) {
        // 使用Intent物件啟動設定程式來更改GPS設定
        Intent i = new Intent(Settings.ACTION_LOCATION_SOURCE_SETTINGS);
        startActivity(i);
    }
    private void okhttpdata(String mapurl){
        Log.i("TAG","--OK--");
        new Thread(new Runnable() {
            @Override
            public void run() {
                OkHttpClient client =new OkHttpClient();
                Request request = new Request.Builder().url(mapurl).build();
                try {
                    Response response = client.newCall(request).execute();
                    date = response.body().string();
                    jsonJXDate(date);
                } catch (IOException e){
                    e.printStackTrace();
                }
            }
        }).start();

    }
    private void jsonJXDate(String date){
        if(date != null){
            try {
                JSONObject jsonObject = new JSONObject(date);
                JSONArray jsonArray = jsonObject.getJSONArray("results");
                for(int i = 0;i< jsonArray.length();i++){
                    str += jsonArray.getJSONObject(i).getString("name");
                }
            } catch (JSONException  e){
                e.printStackTrace();
            }
        }

    }

}