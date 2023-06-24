package com.example.myapplication;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.DividerItemDecoration;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import android.app.ProgressDialog;
import android.os.Bundle;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URL;
import java.util.ArrayList;
import java.util.HashMap;

public class MainActivity extends AppCompatActivity {
    String TAG = MainActivity.class.getSimpleName()+"My";
    ArrayList<HashMap<String,String>> arrayList = new ArrayList<>();

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        catchData();
    }
    private void catchData(){
        String catchData = "https://odws.hccg.gov.tw/001/Upload/25/opendataback/9059/870/8bfb5f8a-2748-44da-a188-6e568987676b.json";
        ProgressDialog dialog = ProgressDialog.show(this,"讀取中","請稍候",true);
        new Thread(()->{
            try {
                URL url = new URL(catchData);
                HttpURLConnection connection = (HttpURLConnection) url.openConnection();
                InputStream is = connection.getInputStream();
                BufferedReader in = new BufferedReader(new InputStreamReader(is));
                String line = in.readLine();
                StringBuffer json = new StringBuffer();
                while (line != null) {
                    json.append(line);
                    line = in.readLine();
                }
                JSONArray jsonArray= new JSONArray(String.valueOf(json));
                for (int i =0;i<jsonArray.length();i++){
                    JSONObject jsonObject = jsonArray.getJSONObject(i);
                    String IDNum = jsonObject.getString("農會漁會別");
                    String branch_type = jsonObject.getString("總部分支機構別");
                    String Code = jsonObject.getString("金融代號");
                    String Postal_code = jsonObject.getString("郵遞區號");
                    String County = jsonObject.getString("所在縣市");
                    String address = jsonObject.getString("住址");
                    String Telephone = jsonObject.getString("電話");


                    HashMap<String,String> hashMap = new HashMap<>();
                    hashMap.put("IDNum",IDNum);
                    hashMap.put("branch_type",branch_type);
                    hashMap.put("Code",Code);
                    hashMap.put("Postal_code",Postal_code);
                    hashMap.put("County",County);
                    hashMap.put("address",address);
                    hashMap.put("Telephone",Telephone);

                    arrayList.add(hashMap);
                }
                Log.d(TAG,""+json);

                runOnUiThread(()->{
                    dialog.dismiss();
                    RecyclerView recyclerView;
                    MyAdapter myAdapter;
                    recyclerView = findViewById(R.id.recyclerView);
                    recyclerView.setLayoutManager(new LinearLayoutManager(this));
                    recyclerView.addItemDecoration(new DividerItemDecoration(this,DividerItemDecoration.VERTICAL));
                    myAdapter = new MyAdapter();
                    recyclerView.setAdapter(myAdapter);

                });
            } catch (MalformedURLException e) {
                e.printStackTrace();
            } catch (IOException e) {
                e.printStackTrace();
            } catch (JSONException e) {
                e.printStackTrace();
            }

        }).start();
    }
    private class MyAdapter extends RecyclerView.Adapter<MyAdapter.ViewHolder>{
        public class ViewHolder extends RecyclerView.ViewHolder {

            TextView tvIDNum,tvbranch_type,tvCode,tvPostal_code,tvCounty,tvaddress,tvTelephone;
            public ViewHolder(@NonNull View itemView) {
                super(itemView);
                tvIDNum = itemView.findViewById(R.id.textView_IDNum);
                tvbranch_type = itemView.findViewById(R.id.textView_branch_type);
                tvCode = itemView.findViewById(R.id.textView_Code);
                tvPostal_code = itemView.findViewById(R.id.textView_Postal_code);
                tvCounty = itemView.findViewById(R.id.textView_County);
                tvaddress = itemView.findViewById(R.id.textView_address);
                tvTelephone = itemView.findViewById(R.id.textView_Telephone);
            }
        }

        @NonNull
        @Override
        public ViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
            View view = LayoutInflater.from(parent.getContext())
                    .inflate(R.layout.recyclerview_item,parent,false);
            return new ViewHolder(view);
        }

        @Override
        public void onBindViewHolder(@NonNull ViewHolder holder, int position) {
            holder.tvIDNum.setText(arrayList.get(position).get("IDNum"));
            holder.tvbranch_type.setText("分支機構別："+arrayList.get(position).get("branch_type"));
            holder.tvCode.setText("金融代號："+arrayList.get(position).get("Code"));
            holder.tvPostal_code.setText("郵遞區號："+arrayList.get(position).get("Postal_code"));
            holder.tvCounty.setText("郵遞區號："+arrayList.get(position).get("County"));
            holder.tvaddress.setText("住址："+arrayList.get(position).get("address"));
            holder.tvTelephone.setText("住址："+arrayList.get(position).get("Telephone"));

        }

        @Override
        public int getItemCount() {
            return arrayList.size();
        }
    }
}