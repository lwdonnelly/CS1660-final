FROM ubuntu
RUN apt-get update && apt-get -y install sudo
RUN sudo apt-get -y install python3.8
RUN sudo apt-get -y install python3-pip
RUN pip3 install orange3

ENV LD_LIBRARY_PATH /usr/lib
RUN mkdir -p /usr/orange
COPY ./orange_service/src /usr/orange
COPY ./display.py /usr/orange
WORKDIR /usr/orange
CMD ["python3","app.py"]