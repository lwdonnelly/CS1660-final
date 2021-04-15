FROM ubuntu
RUN apt-get update && apt-get -y install sudo
RUN sudo apt-get -y install python3.8
RUN sudo apt-get install -y firefox
RUN mkdir -p /usr/sonarcloud
COPY ./sonarcloud_service/src /usr/sonarcloud
COPY ./display.py /usr/sonarcloud
WORKDIR /usr/sonarcloud
CMD ["python3","app.py"]