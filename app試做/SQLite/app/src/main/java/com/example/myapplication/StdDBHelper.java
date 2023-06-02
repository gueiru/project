package com.example.myapplication;

import android.content.Context;
import android.database.sqlite.SQLiteDatabase;
import android.database.sqlite.SQLiteOpenHelper;

public class StdDBHelper extends SQLiteOpenHelper {
    private static final String DATABASE_NAME = "Bank";
    private static final int DATABASE_VERSION = 1;
    public StdDBHelper(Context context) {
        super(context, DATABASE_NAME, null, DATABASE_VERSION);
    }
    @Override
    public void onCreate(SQLiteDatabase db) {
        db.execSQL("CREATE TABLE list_of_banks " + "(bank_id integer primary key Autoincrement," + " credits integer no null," + " checkout_date int no null," + " payment_deadline integer no null)");
    }
    @Override
    public void onUpgrade(SQLiteDatabase db, int oldVersion, int newVersion) {
        db.execSQL("DROP TABLE IF EXISTS list_of_banks");
        onCreate(db);
    }
}
