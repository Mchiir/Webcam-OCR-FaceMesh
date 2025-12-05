# FaceMesh with MediaPipe (AI WITHOUT ML)

## Project Overview

This project demonstrates real-time **facial landmark detection** using **MediaPipe Face Mesh**. It uses a webcam feed to visualize facial landmarks and highlight facial features.

The project allows you to:

- Detect and visualize facial landmarks in real-time.
- Highlight eyes, lips, nose, nostrils, and iris with different colors.
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

---

## Technologies Used

- **Python 3.12.7**
- **OpenCV** – Webcam capture and image preprocessing.
- **MediaPipe** – Real-time facial landmark detection.
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

## Usage

1. Run the main script:

```bash
(.venv) cd FaceMesh-MediaPipe
(.venv) python main.py
```

## Notes

- Always run the script inside the **Python 3.12.7 virtual environment** to avoid dependency issues.
- Adjust `cap = cv2.VideoCapture(1)` if your primary webcam is at a different index (0 for default).

## License

This project is licensed under the **MIT License**.
