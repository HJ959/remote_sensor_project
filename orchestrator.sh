#!/bin/bash

# this shell script acts as the orchestrator
# automating the various processes involved
# 
# Read sensor data
# store sensor data
# record audio and video
# process audio and video
# push to github for processing in front-end

# path
git_dir="/home/pi/remote_sensor_project"

# check for repo updates (handy if wanting to edit script remotely)
git --git-dir $git_dir/.git pull

now="$(date | cut -d ' ' -f 3,4,5 | tr ' ' _ | tr ':' '-')"
output_mp4="output_$now.mp4"
output_png="out%d_$now.png"

if [ ! -f "$git_dir/sensor_back_end/sensor_data.json" ]
then
	echo '{"example_json": {"temp": "25", "moisture": "670"}}' > $git_dir/sensor_back_end/sensor_data.json
fi

python3 $git_dir/sensor_back_end/read_post_data.py

git --git-dir $git_dir/.git add $git_dir/sensor_back_end
git --git-dir $git_dir/.git commit -m "Backend sensor upload - $now"
git --git-dir $git_dir/.git push -u origin master

