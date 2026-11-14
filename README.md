# HPI 3D Scanner Core

A lightweight Python-based depth data processor designed to analyze sensor frames and calculate approximate 3D spatial bounding dimensions for engineering applications.

## Overview
Developed as part of the **Habilidades Profesionales para Ingenieros (HPI)** course project at ULPGC. This module processes raw infrared or depth sensor readings, filters out background noise using configurable thresholds, and outputs structured volumetric dimensions.

## Features
- **Depth Data Processing:** Filters out invalid readings and background noise.
- **Volumetric Estimation:** Calculates approximate width, height, and depth bounding dimensions.
- **Clean Structure:** Uses Python type hinting, docstrings, and clean dictionary outputs.

## Code Structure
The core function `process_depth_frame` handles the data pipeline:
```python
def process_depth_frame(depth_data: List[float], threshold: float = 0.5) -> Dict[str, float]:
    """
    Process raw infrared/depth sensor data to filter noise and calculate 
    approximate 3D bounding dimensions of a scanned object.
    """
