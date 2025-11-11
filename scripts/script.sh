#!/bin/sh

mkdir output
seq 0 900 | parallel -j 8 '
    i={};
    python scripts/script.py $i > scenes/frame_$(printf "%03d" $i).pbrt &&
    ./pbrt scenes/frame_$(printf "%03d" $i).pbrt --outfile output/frame_$(printf "%03d" $i).png &&
    rm scenes/frame_$(printf "%03d" $i).pbrt
'

ffmpeg -framerate 30 -i output/frame_%03d.png -c:v libx264 -pix_fmt yuv420p output.mp4
