# YOLO & Flutter Mobile App

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Flutter](https://img.shields.io/badge/Flutter-%2302569B.svg?logo=flutter&logoColor=white)
![Python](https://img.shields.io/badge/Python-3670A0?logo=python&logoColor=ffdd54)
![YOLOv8](https://img.shields.io/badge/YOLOv8-Object--Detection-orange)

## 📌 Overview

This project is a cross-platform mobile application developed with **Flutter** for front-end cross-device performance, coupled with **YOLOv8** object detection models for real-time and attire-only analysis. 

Originally developed under the **"YOLOv8 Flutter for Military Applications"** initiative, this project leverages Python and REST APIs alongside TFLite integration to deliver optimized performance on mobile architectures (Android & iOS).

---

## ✨ Key Features

- **Cross-Platform Compatibility**: Single codebase powered by Flutter for seamless performance across Android and iOS devices.
- **YOLOv8 Integration**: High-precision object detection for specialized detection tasks (including attire-only detection).
- **TFLite Mobile Inference**: Optimized on-device execution using TensorFlow Lite helpers (`tflite_flutter_helper.dart`).
- **REST API & Python Backend**: Flexible architecture separating lightweight client-side requests from high-performance model processing.

---

## 🛠️ Tech Stack & Languages

- **Frontend**: Flutter / Dart
- **Android Native**: Kotlin / Gradle
- **Backend & ML**: Python, YOLOv8, TensorFlow Lite

| Language / Framework | Purpose |
| :--- | :--- |
| **Python** | Model training, attire-only detection (`attire_only_detection.py`), backend APIs |
| **Dart / Flutter** | Cross-platform UI and TFLite model execution |
| **Kotlin** | Native Android integration (`MainActivity.kt`) |

---

## 📁 Repository Structure

```text
.
├── MainActivity.kt               # Native Android entry point
├── attire_only_detection.py      # Python script for attire-specific YOLO detection
├── convert_i_model.py            # Model conversion/export script (e.g., YOLO to TFLite/ONNX)
├── tflite_flutter_helper.dart    # Helper class for Flutter TFLite integration
├── final_yolo_flutter_android.zip# Compressed Android project build/assets
├── pubspec.yaml                  # Flutter project dependencies
├── build.gradle                  # Android build configuration
├── gradle-wrapper.properties     # Gradle wrapper properties
└── styles.xml                    # Android styling configurations
