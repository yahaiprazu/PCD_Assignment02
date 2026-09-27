"""PCD Assignment 02 - Image Enhancement

Reusable implementation of image enhancement methods used in the notebook.
"""
from pathlib import Path
import cv2
import numpy as np


def load_grayscale(path: str | Path) -> np.ndarray:
    image = cv2.imread(str(path), cv2.IMREAD_GRAYSCALE)
    if image is None:
        raise FileNotFoundError(f"Could not read image: {path}")
    return image


def create_dark_low_contrast(image: np.ndarray, alpha: float = 0.55, beta: float = -35) -> np.ndarray:
    """Reduce contrast and brightness to create a controlled enhancement input."""
    return cv2.convertScaleAbs(image, alpha=alpha, beta=beta)


def gamma_correction(image: np.ndarray, gamma: float = 1.8) -> np.ndarray:
    """Brighten a dark image using gamma < 1 or darken using gamma > 1."""
    if gamma <= 0:
        raise ValueError("gamma must be greater than 0")
    inv = 1.0 / gamma
    table = np.array([((i / 255.0) ** inv) * 255 for i in np.arange(256)]).astype("uint8")
    return cv2.LUT(image, table)


def histogram_equalization(image: np.ndarray) -> np.ndarray:
    return cv2.equalizeHist(image)


def clahe_enhancement(image: np.ndarray, clip_limit: float = 2.0, tile_grid_size=(8, 8)) -> np.ndarray:
    clahe = cv2.createCLAHE(clipLimit=clip_limit, tileGridSize=tile_grid_size)
    return clahe.apply(image)


def statistics(image: np.ndarray) -> dict:
    return {
        "min": int(image.min()),
        "max": int(image.max()),
        "mean": float(image.mean()),
        "std": float(image.std()),
    }


def enhance_image(image: np.ndarray) -> dict[str, np.ndarray]:
    """Run all enhancement methods and return named results."""
    return {
        "Gamma Correction": gamma_correction(image, gamma=1.8),
        "Histogram Equalization": histogram_equalization(image),
        "CLAHE": clahe_enhancement(image, clip_limit=2.0, tile_grid_size=(8, 8)),
    }
