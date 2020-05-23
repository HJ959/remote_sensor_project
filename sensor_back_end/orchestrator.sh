#!/bin/bash

# this shell script acts as the orchestrator
# automating the various processes involved
# 
# Read sensor data
# store sensor data
# record audio and video
# process audio and video
# push to github for processing in front-end

# check for repo updates (handy if wanting to edit script remotely)
git pull

now="$(date | cut -d ' ' -f 3,4,5 | tr ' ' _ | tr ':' '-')"
output_mp4="output_$now.mp4"
output_png="out%d_$now.png"

if [ ! -f "sensor_data.json" ]
then
	echo '{"example_json": {"temp": "25", "moisture": "670"}}' > sensor_data.json
fi

python3 read_post_data.py

git add --all
git commit -m "Backend sensor upload - $now"
git push -u origin master

