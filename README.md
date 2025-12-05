# OCR-MediaPipe Face Mesh

## Project Overview

This project is a Python-based tool that combines **OCR (Optical Character Recognition)** with **MediaPipe Face Mesh** to provide real-time text extraction and facial feature detection using a webcam.

The project allows users to:

- Capture live images using a webcam.
- Select a Region of Interest (RoI) from the captured image.
- Extract text from the selected area using Tesseract OCR.
- Visualize facial landmarks, including eyes, lips, nose, nostrils, and iris using MediaPipe Face Mesh.

## Features

### OCR Functionality

- Real-time capture of images via webcam.
- Region-of-Interest (RoI) selection for precise text extraction.
- Image preprocessing to enhance OCR accuracy (grayscale, blur, thresholding).
- Saves extracted text to uniquely timestamped text files.

### MediaPipe Face Mesh

- Real-time facial landmark detection using webcam feed.
- Highlights facial features in different colors:

  - Full face mesh (magenta)
  - Eye contours (green)
  - Lips (red)
  - Nose contour (cyan)
  - Nostril circles (orange)
  - Iris circles (yellow)

- Supports multiple faces in the frame.

### Technologies Used

- **Python 3.x**
- **OpenCV**: Capturing webcam feed and image preprocessing.
- **MediaPipe**: Real-time facial landmark detection and visualization.
- **Tesseract OCR**: Extracting text from images.
- **NumPy**: Efficient image array manipulations.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/OCR-MediaPipe-face-mesh.git
cd OCR-MediaPipe-face-mesh
```

2. Install the required dependencies:

```bash
pip install opencv-python mediapipe pytesseract numpy
```

3. Make sure Tesseract OCR is installed on your system and its path is properly set.

## Usage

1. Run the main script:

```bash
python main.py
```

2. Follow on-screen instructions:

- Press **'C'** to capture an image.
- Select the **Region of Interest (RoI)**.
- View extracted text and press:

  - **'S'** to save
  - **'R'** to retake
  - **'Q'** to quit

3. For face mesh visualization:

- The webcam will display real-time face mesh and facial landmarks.
- Press **'Q'** to exit.

## License

This project is licensed under the MIT License.
