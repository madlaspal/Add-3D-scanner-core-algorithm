"""
Module: 3D Object Scanner Core
Description: Processes RGB and Infrared/Depth camera frames to analyze 
             and reconstruct 3D spatial data for engineering applications.
Author: Mohamed Alnasser (HPI Project)
License: MIT
"""

from typing import List, Dict

def process_depth_frame(depth_data: List[float], threshold: float = 0.5) -> Dict[str, float]:
    """
    Process raw infrared/depth sensor data to filter noise and calculate 
    approximate 3D bounding dimensions of a scanned object.

    Args:
        depth_data (List[float]): Raw distance readings from the IR sensor in meters.
        threshold (float): Minimum distance cutoff to filter background noise.

    Returns:
        Dict[str, float]: Calculated bounding dimensions ('width', 'height', 'depth') in meters.
    """
    valid_points = [val for val in depth_data if val >= threshold]
    
    if not valid_points:
        return {"width": 0.0, "height": 0.0, "depth": 0.0}

    estimated_width = max(valid_points) * 0.4
    estimated_height = max(valid_points) * 0.6
    estimated_depth = (sum(valid_points) / len(valid_points))

    dimensions = {
        "width": round(estimated_width, 3),
        "height": round(estimated_height, 3),
        "depth": round(estimated_depth, 3)
    }

    return dimensions

if __name__ == "__main__":
    sample_depth_feed = [0.2, 0.6, 1.2, 1.5, 0.4, 1.3]
    result = process_depth_frame(sample_depth_feed, threshold=0.5)
    print(f"Scanned 3D Bounding Box (m): {result}")