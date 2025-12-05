# FaceMesh & OCR (AI WITHOUT ML)

## Project Overview

This project demonstrates real-time **facial landmark detection** using **MediaPipe Face Mesh** along with **Optical Character Recognition (OCR)** capabilities via Tesseract. It uses a webcam feed to visualize facial landmarks and extract text from selected images or regions of interest (RoI).

The project allows you to:

- Detect and visualize facial landmarks in real-time.
- Highlight eyes, lips, nose, nostrils, and iris with different colors.
- Capture images for OCR text extraction.
- Use Python and OpenCV for webcam capture and image preprocessing.

> Recommended Python version: **3.12.7** (MediaPipe has compatibility issues with Python 3.13+).

---

## Features

### MediaPipe Face Mesh

- Detects up to 10 faces in real-time.
- Highlights facial features in distinct colors:
  - **Magenta**: Full face mesh
  - **Green**: Eye contours
  - **Red**: Lips
  - **Cyan**: Nose contour
  - **Orange**: Nostril circles
  - **Yellow**: Iris circles
- Refined landmarks for high accuracy.
- Works with live webcam feed.

### OCR (Optional)

- Uses Tesseract OCR for text extraction.
- Can process images captured via webcam.
- Supports image preprocessing for better OCR accuracy (grayscale, blur, thresholding).
- Saves text to files with timestamps.

---

## Technologies Used

- **Python 3.12.7**
- **OpenCV** – Webcam capture and image preprocessing.
- **MediaPipe** – Real-time facial landmark detection.
- **Tesseract OCR** – Extracting text from images.
- **NumPy** – Array manipulation for image processing.
- **protobuf, attrs, matplotlib** – Required dependencies for MediaPipe.

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Mchiir/Webcam-OCR-FaceMesh.git
cd Webcam-OCR-FaceMesh/FaceMesh-MediaPipe-LBPH
```

2. Create and activate a virtual environment with Python 3.12.7:

```bash
# Windows
python -m venv .venv
.venv\Scripts\activate
```

3. Install the required dependencies:

```bash
pip install --upgrade pip
pip install --upgrade --no-deps --force-reinstall opencv-python mediapipe pytesseract numpy protobuf attrs matplotlib
```

4. Make sure Tesseract OCR is installed on your system and its path is properly set.

## Usage

1. Run the main script:

```bash
(.venv) cd Webcam-OCR-FaceMesh
(.venv) python main.py
```

## Notes

- Make sure **Tesseract OCR** is installed on your system and its path is set in your environment variables if using OCR.
- Always run the script inside the **Python 3.12.7 virtual environment** to avoid dependency issues.
- Adjust `cap = cv2.VideoCapture(1)` if your primary webcam is at a different index (0 for default).

## License

This project is licensed under the **MIT License**.