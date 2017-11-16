FROM ubuntu:trusty

RUN apt-get -qq update --fix-missing
RUN locale-gen en_US en_US.UTF-8
RUN dpkg-reconfigure locales

RUN apt-get install -y bash mpd

#ADD mpd.conf /etc/mpd.conf
ADD mpd-install.sh /home/mpd/mpd-install.sh 

RUN mkdir -p /home/mpd/pids
RUN mkdir -p /home/mpd/logs
RUN chown -R mpd /home/mpd
#RUN chmod +x /home/mpd/start.sh

EXPOSE 6601 
EXPOSE 6602 

COPY ../dist/config/mpd-stream1.conf /home/config/mpd-stream1.conf
COPY ../dist/config/mpd-stream2.conf /home/config/mpd-stream2.conf

RUN chmod +x /home/mpd/mpd-install.sh

RUN mkdir -p /home/mpd/playlist/stream1
RUN mkdir -p /home/mpd/playlist/stream2

RUN mkdir -p /home/mpd/mpdstate-stream1
RUN mkdir -p /home/mpd/mpdstate-stream2

RUN mkdir -p /home/mpd/music
COPY music /home/mpd/music/

# ENTRYPOINT /home/mpd/start.sh
CMD ["bash","/home/mpd/mpd-install.sh"]