FROM ubuntu
RUN apt-get update && apt-get -y install sudo
RUN sudo apt-get -y install git
RUN sudo apt-get -y install python3.8
RUN sudo apt-get -y install xterm
RUN sudo apt-get -y install python3-pip
ENV LD_LIBRARY_PATH /usr/lib
RUN mkdir -p /usr/git
COPY ./git_service/src /usr/git
COPY ./display.py /usr/git
WORKDIR /usr/git
CMD ["python3","app.py"]