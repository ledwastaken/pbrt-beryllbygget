import sys
import math

# Get frame index from command line
frame = int(sys.argv[1])
total_frames = 30 * 30
radius = 150

# Compute angle of rotation (full 360° over total frames)
angle = 2 * math.pi * frame / total_frames
cam_x = radius * math.cos(angle)
cam_z = radius * math.sin(angle)

# PBRT scene header
scene = f"""
Integrator "volpath"

# Use "halton" for higher sampling rates
Sampler "zsobol"
    "integer pixelsamples" [ 64 ]

Film "rgb"
    "string filename" [ "output.png" ]
    "integer xresolution" [ 800 ]
    "integer yresolution" [ 600 ]

Scale -1 1 1
LookAt {cam_x} {cam_z} 15  0 0 25  0 0 1
Camera "perspective"
    "float fov" [ 45 ]

WorldBegin

Include "light.pbrt"
Include "geometry.pbrt"
"""

print(scene)
