# PCD Assignment 02 — Image Enhancement

**Course:** Pengolahan Citra Digital (PCD)  
**Student:** Yasyfin Haidar Pranaja Zuhri  
**Assignment:** Image Enhancement

## Overview

This project implements image enhancement techniques on a basketball photograph. To create a clear enhancement case from the selected photograph, the notebook first produces a controlled **dark and low-contrast version** of the original image. Three enhancement methods are then compared:

1. **Gamma Correction** — improves brightness through a nonlinear intensity transformation.
2. **Histogram Equalization** — improves global contrast by redistributing grayscale intensities.
3. **CLAHE** — performs local contrast enhancement while limiting excessive amplification.

The experiment combines visual comparison, intensity histograms, and simple numerical statistics such as mean intensity and standard deviation.

## Repository Structure

```text
PCD_Assignment02/
├── PCD_Assignment02.ipynb
├── README.md
├── REPORT.md
├── requirements.txt
├── images/
│   └── original.jpg
├── results/
│   ├── comparison.png
│   ├── input_dark_low_contrast.png
│   ├── gamma_correction.png
│   ├── histogram_equalization.png
│   └── clahe.png
└── src/
    └── enhance.py
```

## How to Run

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Open the notebook

```bash
jupyter notebook PCD_Assignment02.ipynb
```

Run all cells from top to bottom. The notebook automatically reads `images/original.jpg`, creates the enhancement input, processes it, displays the comparisons, and saves the results into `results/`.

## Methods

### Gamma Correction

Gamma correction applies a nonlinear mapping to pixel intensities. It is useful when an image is too dark because it can expand darker intensity values and make hidden details easier to see.

### Histogram Equalization

Histogram equalization is a global contrast-enhancement method. It redistributes grayscale intensities so that the available intensity range is used more effectively. It can improve overall contrast but may also make noise or already-bright regions more noticeable.

### CLAHE

Contrast Limited Adaptive Histogram Equalization (CLAHE) divides the image into local tiles and enhances contrast independently within those regions. A contrast limit helps reduce excessive amplification, making CLAHE useful for images with uneven illumination.

## Results

The generated result images are stored in `results/`. The notebook also contains the full visual and quantitative comparison.

## Conclusion

The experiment demonstrates that different enhancement methods address different image problems. Gamma correction primarily addresses brightness, histogram equalization improves global contrast, and CLAHE focuses on local contrast while controlling amplification. The final choice should be based on both visual quality and numerical evidence rather than a single statistic.
