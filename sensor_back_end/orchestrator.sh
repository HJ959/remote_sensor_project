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
cd /home/pi/remote_sensor_project

# find the scripts and files
json_file=$(find $HOME -name "sensor_data.json")
python_script=$(find $HOME -name "read_post_data.py")
spy_cam_dir=$(find $HOME -name "spy_cam")
audio_dir=$(find $HOME -name "spy_audio_dir")

# check for repo updates (handy if wanting to edit script remotely)
git pull

# get the date
now="$(date | cut -d ' ' -f 3,4,5 | tr ' ' _ | tr ':' '-')"

if [ ! -f "$json_file" ]
then
	echo '{"example_json": {"temp": "25", "moisture": "670"}}' > sensor_back_end/sensor_data.json
fi

python3 $python_script $json_file $spy_cam_dir $now

audio_file=$audio_dir/audio_$now.mp3
ffmpeg -y -f alsa -ac 1 -ar 44100 -i default:CARD=E1 -t 2 $audio_file
ffmpeg -y -i $audio_file -filter:a "volume=2.0" $audio_file

git add --all
git commit -m "Backend sensor upload - $now"
git push -u origin master

