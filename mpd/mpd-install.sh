#!/bin/bash

#apt-get -y update && \
#apt-get -y install mpd sonata && \

#adduser mpd && \
#mkdir -p /home/mpd/music && \
#mkdir -p /home/mpd/playlist/stream{1,2} 




mkdir -p /opt/music/.mpd
mkdir -p /opt/music/.mpd/playlists
chown -R mpd /opt/music/.mpd

#mpd --no-daemon --stdout -v /etc/mpd.conf

mpd --no-daemon --stdout -v /home/config/mpd-stream1.conf && \
mpd --no-daemon --stdout -v /home/config/mpd-stream2.conf 