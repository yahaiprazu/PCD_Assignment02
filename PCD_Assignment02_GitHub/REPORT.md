# Report Analysis — PCD Assignment 02

## 1. Introduction

Image enhancement is an important part of digital image processing because the quality of an acquired image is not always sufficient for human observation or further computer vision tasks. An image may be too dark, too bright, blurred, or have weak contrast. Enhancement techniques attempt to make useful visual information more apparent without changing the fundamental content of the scene.

For this assignment, a basketball photograph is selected as the main image. The original photograph has a wide range of meaningful visual structures, including the players, basketball, indoor court, background, and lighting. To create a controlled enhancement problem, the grayscale image is transformed into a darker and lower-contrast version. This allows the enhancement methods to be compared under a clear and reproducible condition.

The experiment evaluates three methods: Gamma Correction, Histogram Equalization, and Contrast Limited Adaptive Histogram Equalization (CLAHE). The comparison is performed using the displayed images, grayscale histograms, and basic intensity statistics.

## 2. Methodology

### 2.1 Input Preparation

The original image is first converted to grayscale. A dark and low-contrast input is then produced using a linear intensity transformation. The transformation reduces the contrast range and shifts the brightness downward. This simulated degradation is useful because it gives the experiment a consistent starting point while preserving the same scene content.

### 2.2 Gamma Correction

Gamma correction applies a nonlinear transformation to the pixel intensities. For a dark image, an appropriate gamma setting can expand the darker part of the intensity range and make details easier to observe. Unlike histogram equalization, gamma correction does not attempt to flatten or redistribute the entire histogram. Its main role in this experiment is brightness recovery.

### 2.3 Histogram Equalization

Histogram Equalization is a global contrast-enhancement method. It calculates the cumulative distribution of grayscale intensities and maps the original values to a wider intensity range. As a result, the separation between some neighboring intensity levels can increase. This can reveal details that were difficult to distinguish in the low-contrast input.

However, because the transformation is global, it does not treat different regions independently. If some areas are already sufficiently bright, they may become excessively bright after enhancement. Noise can also become more visible when the contrast is strongly expanded.

### 2.4 CLAHE

CLAHE is a local version of histogram equalization with a contrast limit. The image is divided into small tiles, and contrast enhancement is calculated separately in each region. The clipping mechanism prevents a small number of intense pixels from dominating the local histogram.

This makes CLAHE particularly useful when illumination is not uniform. In the selected basketball photograph, different parts of the scene contain different lighting conditions, so local enhancement can potentially reveal details without applying one identical transformation to every region.

## 3. Results and Analysis

The visual comparison should be interpreted together with the histograms. The dark low-contrast input is expected to contain a relatively concentrated intensity distribution. This concentration corresponds to the limited range of grayscale values and explains why some structures can appear less distinct.

Gamma Correction should increase the visibility of darker regions while keeping the transformation relatively smooth. Its histogram is expected to shift toward brighter intensity values. This makes it particularly suitable for recovering visibility from an image whose main problem is insufficient brightness.

Histogram Equalization should spread the intensity distribution over a larger portion of the available grayscale range. This generally increases global contrast. In the basketball scene, stronger separation between the players, ball, clothing, and background can make edges and structures easier to distinguish. The trade-off is that some bright areas may become more intense, and image noise may also be amplified.

CLAHE should produce a more locally adaptive result. Because the transformation is calculated over smaller regions, details in darker portions of the scene can receive more attention without forcing the same global adjustment on the entire image. The contrast limit also helps prevent extremely strong local amplification. For scenes with uneven illumination, this behavior can make CLAHE visually more balanced than global histogram equalization.

The numerical statistics provide supporting evidence. Mean intensity indicates the average brightness of each result, while standard deviation describes how widely the grayscale values are distributed. A larger standard deviation can indicate stronger intensity separation, but it should not automatically be interpreted as better image quality. An enhancement result is useful only when the increased contrast also preserves meaningful details and avoids distracting artifacts.

## 4. Comparison

The three methods solve slightly different problems. Gamma Correction is primarily a brightness adjustment and is straightforward to control. Histogram Equalization is effective when the entire image suffers from weak global contrast. CLAHE is more adaptive because it works locally and limits contrast amplification.

For this experiment, the methods should therefore be evaluated according to the characteristics of the selected input rather than by assuming that one technique is universally superior. If the major problem is darkness, gamma correction can provide a direct brightness improvement. If the major problem is globally compressed contrast, histogram equalization can expand the intensity distribution. If illumination varies substantially across the scene, CLAHE can provide a more localized correction.

## 5. Conclusion

This experiment demonstrates the implementation and comparison of three image enhancement techniques using a basketball photograph: Gamma Correction, Histogram Equalization, and CLAHE. The original image is converted into a controlled dark and low-contrast input so that the effects of enhancement can be observed clearly.

The experiment shows that image enhancement is not simply a matter of making an image brighter. Different algorithms modify the intensity distribution in different ways. Gamma Correction changes brightness through a nonlinear mapping, Histogram Equalization improves global contrast, and CLAHE improves local contrast while limiting excessive amplification. Visual inspection, histograms, and numerical statistics together provide a more complete basis for analyzing the results.
