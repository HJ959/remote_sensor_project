#!/bin/bash

# this shell script acts as the orchestrator
# automating the various processes involved
# 
# Read sensor data
# store sensor data
# record audio and video
# process audio and video
# push to github for processing in front-end

now="$(date | cut -d ' ' -f 3,4,5 | tr ' ' _ | tr ':' '-')"
output_mp4="output_$now.mp4"
output_png="out%d_$now.png"

if [ ! -f "sensor_data.json" ]
then
	echo '{"example_json": {"temp": "25", "moisture": "670"}}' > sensor_data.json
fi

python3 read_post_data.py

#ffmpeg -y -f v4l2 -framerate 1 -video_size 640x480 -i /dev/video0 -t 1 $output_mp4

#ffmpeg -i $output_mp4 -vf fps=1 out%d.png
