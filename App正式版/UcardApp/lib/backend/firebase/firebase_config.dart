import 'package:firebase_core/firebase_core.dart';
import 'package:flutter/foundation.dart';

Future initFirebase() async {
  if (kIsWeb) {
    await Firebase.initializeApp(
        options: FirebaseOptions(
            apiKey: "AIzaSyAqftDB7hpld6KU-nCVqWJa_44bT_sBleE",
            authDomain: "appucard-4d609.firebaseapp.com",
            projectId: "appucard-4d609",
            storageBucket: "appucard-4d609.appspot.com",
            messagingSenderId: "145685092238",
            appId: "1:145685092238:web:3c24f80758fb7a9f4176df",
            measurementId: "G-9242SN5R8Q"));
  } else {
    await Firebase.initializeApp();
  }
}
