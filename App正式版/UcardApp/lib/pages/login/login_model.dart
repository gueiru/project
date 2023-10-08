import '/auth/firebase_auth/auth_util.dart';
import '/flutter_flow/flutter_flow_animations.dart';
import '/flutter_flow/flutter_flow_button_tabbar.dart';
import '/flutter_flow/flutter_flow_theme.dart';
import '/flutter_flow/flutter_flow_util.dart';
import '/flutter_flow/flutter_flow_widgets.dart';
import 'login_widget.dart' show LoginWidget;
import 'package:flutter/material.dart';
import 'package:flutter/scheduler.dart';
import 'package:flutter_animate/flutter_animate.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:provider/provider.dart';

class LoginModel extends FlutterFlowModel<LoginWidget> {
  ///  State fields for stateful widgets in this page.

  // State field(s) for TabBar widget.
  TabController? tabBarController;
  int get tabBarCurrentIndex =>
      tabBarController != null ? tabBarController!.index : 0;

  // State field(s) for emailAddress widget.
  TextEditingController? emailAddressController;
  //String? Function(BuildContext, String?)? emailAddressControllerValidator;
  String? emailAddressControllerValidator(BuildContext context, String? emailAddressController) {
    if (emailAddressController == null || emailAddressController.isEmpty) {
      return '請輸入電子郵件地址';
    } else if (!emailAddressController.contains('@')) {
      return '電子郵件地址格式不正確';
    } else {
      return null;
    }
  }
  // State field(s) for password widget.
  TextEditingController? passwordController;
  late bool passwordVisibility;
  String? Function(BuildContext, String?)? passwordControllerValidator;
  // State field(s) for emailAddress_Create widget.
  TextEditingController? emailAddressCreateController;
  String? Function(BuildContext, String?)?
      emailAddressCreateControllerValidator;
  // State field(s) for password_create widget.
  TextEditingController? passwordCreateController1;
  late bool passwordCreateVisibility1;
  String? Function(BuildContext, String?)? passwordCreateController1Validator;
  // State field(s) for password_create widget.
  TextEditingController? passwordCreateController2;
  late bool passwordCreateVisibility2;
  String? Function(BuildContext, String?)? passwordCreateController2Validator;

  /// Initialization and disposal methods.

  void initState(BuildContext context) {
    passwordVisibility = false;
    passwordCreateVisibility1 = false;
    passwordCreateVisibility2 = false;
  }

  void dispose() {
    tabBarController?.dispose();
    emailAddressController?.dispose();
    passwordController?.dispose();
    emailAddressCreateController?.dispose();
    passwordCreateController1?.dispose();
    passwordCreateController2?.dispose();
  }

  /// Action blocks are added here.

  /// Additional helper methods are added here.
}
