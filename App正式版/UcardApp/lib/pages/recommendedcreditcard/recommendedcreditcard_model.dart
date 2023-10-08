import '/flutter_flow/flutter_flow_icon_button.dart';
import '/flutter_flow/flutter_flow_theme.dart';
import '/flutter_flow/flutter_flow_util.dart';
import '/flutter_flow/flutter_flow_widgets.dart';
import 'recommendedcreditcard_widget.dart' show RecommendedcreditcardWidget;
import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:provider/provider.dart';

class RecommendedcreditcardModel
    extends FlutterFlowModel<RecommendedcreditcardWidget> {
  ///  State fields for stateful widgets in this page.

  // State field(s) for Estimated widget.
  TextEditingController? estimatedController;
  String? Function(BuildContext, String?)? estimatedControllerValidator;

  /// Initialization and disposal methods.

  void initState(BuildContext context) {}

  void dispose() {
    estimatedController?.dispose();
  }

  /// Action blocks are added here.

  /// Additional helper methods are added here.
}
