FROM ubuntu
RUN apt-get update && apt-get -y install sudo
RUN sudo apt-get -y install python3.8
RUN sudo apt-get install -y firefox
RUN mkdir -p /usr/rstudio
COPY ./rstudio_service/src /usr/rstudio
COPY ./display.py /usr/rstudio
WORKDIR /usr/rstudio
CMD ["python3","app.py"]