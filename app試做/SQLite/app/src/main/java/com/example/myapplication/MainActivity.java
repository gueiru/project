package com.example.myapplication;

import androidx.appcompat.app.AppCompatActivity;

import android.content.ContentValues;
import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;
import android.os.Bundle;
import android.view.View;
import android.widget.EditText;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {
    private static String DATABASE_TABLE = "Bank";
    private SQLiteDatabase db;
    private StdDBHelper dbHelper;
    private EditText bank_id,credits,checkout_date,payment_deadline;
    private TextView output;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        dbHelper = new StdDBHelper(this);
        db = dbHelper.getWritableDatabase();
        output = (TextView)findViewById(R.id.lblOutput);
        credits = (EditText)findViewById(R.id.credits);
        checkout_date = (EditText)findViewById(R.id.checkout_date);
        payment_deadline = (EditText)findViewById(R.id.payment_deadline);
    }
    @Override
    public void onStop(){
        super.onStop();
        db.close();
    }
    //新增
    public void button_Click1(View view){
        long id;
        ContentValues cv = new ContentValues();
        cv.put("credits",Integer.parseInt(credits.getText().toString()));
        cv.put("checkout_date",Integer.parseInt(checkout_date.getText().toString()));
        cv.put("payment_deadline",Integer.parseInt(payment_deadline.getText().toString()));
        id = db.insert(DATABASE_TABLE, null, cv);
        output.setText("新增記錄成功: " + id);
    }
    //刪除
    public void button_Click2(View view){
        int count;
        int id = Integer.parseInt(bank_id.getText().toString());
        count = db.delete(DATABASE_TABLE, "bank_id=" + id, null);
        output.setText("刪除記錄成功: " + count);
    }
    //查詢
    public void button_Click3(View view){
        SqlQuery("SELECT * FROM " + DATABASE_TABLE);
    }

    public void SqlQuery(String sql) {
        String[] colNames;
        String str = "";
        Cursor c = db.rawQuery(sql, null);
        colNames = c.getColumnNames();
        // 顯示欄位名稱
        for (int i = 0; i < colNames.length; i++)
            str += colNames[i] + "\t\t";
        str += "\n";
        c.moveToFirst();  // 第1筆
        // 顯示欄位值
        for (int i = 0; i < c.getCount(); i++) {
            str += c.getString(0) + "\t\t";
            str += c.getString(1) + "\t\t";
            str += c.getString(2) + "\n";
            c.moveToNext();  // 下一筆
        }
        output.setText(str.toString());
    }
}

