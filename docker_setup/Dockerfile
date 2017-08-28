FROM python:3.5

#Create volume to mount program directory
VOLUME /data

WORKDIR /data

#Install vim
RUN apt-get -y update && apt-get -y install vim

#set up python auto indent and coloring
RUN echo "syntax on" >> ~/.vimrc
RUN echo "filetype indent plugin on" >> ~/.vimrc
RUN echo "set background=dark"
