FROM ubuntu
RUN apt-get update && apt-get -y install sudo
RUN sudo apt-get -y install python3.8
RUN sudo apt-get -y install python3-pip
RUN pip3 install --user --upgrade tensorflow
RUN mkdir -p /usr/tensorflow
COPY ./tensorflow_service/src /usr/tensorflow
COPY ./display.py /usr/tensorflow
WORKDIR /usr/tensorflow
CMD ["python3","app.py"]