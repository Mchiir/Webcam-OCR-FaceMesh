# AI Without ML: OCR, FaceMesh & More

## Project Overview

This project is a comprehensive Python-based toolkit that leverages **advanced computer vision** and **image processing technologies** to enable powerful real-time applications—all **without training custom machine learning models**.

It brings together multiple capabilities, including:

- **Facial landmark detection** with MediaPipe Face Mesh.
- **Real-time text extraction** using OCR (Tesseract).
- **Image processing and visualization** with OpenCV and Matplotlib.
- **Face recognition** and pattern matching with LBPH (Local Binary Patterns Histogram).

This framework demonstrates how modern Python libraries can achieve AI-level functionalities efficiently and reliably on standard hardware.

---

## Key Features

### Real-Time Facial Landmark Detection

- Detects facial landmarks for multiple faces simultaneously.
- Highlights features such as eyes, lips, nose, nostrils, and iris.
- Provides accurate, refined landmarks for applications like augmented reality, emotion detection, and more.

### Optical Character Recognition (OCR)

- Extracts text from live webcam feeds or captured images.
- Allows Region-of-Interest (RoI) selection for precise extraction.
- Supports image preprocessing techniques (grayscale, thresholding, blur) for better accuracy.
- Saves extracted content in organized, timestamped files.

### Face Recognition and Pattern Matching (LBPH)

- Identifies and recognizes faces using local binary patterns.
- Enables secure authentication or identity verification applications.
- Works in real-time with webcam input.

### Visualization and Analysis

- Provides interactive visualization of facial landmarks and detected text.
- Uses **Matplotlib** for plotting and analyzing images.
- Enhances understanding of facial structure and OCR results through clear visual feedback.

---

## Technologies Highlight

- **Python 3.12.7** – Core programming language, stable for MediaPipe compatibility.
- **OpenCV** – Captures and processes webcam images efficiently.
- **MediaPipe** – State-of-the-art facial landmark detection framework.
- **Tesseract OCR** – Reliable text extraction from images.
- **LBPH (Local Binary Patterns Histogram)** – Lightweight face recognition and matching.
- **NumPy** – Fast numerical computations for image arrays.
- **Matplotlib** – Advanced data and image visualization.
- **protobuf, attrs** – Required by MediaPipe for efficient operations.

---

## Why This Project Matters

This project demonstrates that **AI-level capabilities can be achieved without training complex models**, making it accessible, fast, and easy to deploy. It is suitable for:

- Developers exploring computer vision.
- Educational purposes for learning AI concepts.
- Prototyping real-time applications involving faces and text.
- Research experiments in image and facial analytics.

---

## License

This project is licensed under the **MIT License**.
