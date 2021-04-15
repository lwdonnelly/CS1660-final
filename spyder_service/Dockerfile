FROM ubuntu
RUN apt-get update && apt-get -y install sudo
RUN sudo apt-get -y install python3.8
RUN sudo apt-get install -y firefox
RUN mkdir -p /usr/spyder
COPY ./spyder_service/src /usr/spyder
COPY ./display.py /usr/spyder
WORKDIR /usr/spyder
CMD ["python3","app.py"]