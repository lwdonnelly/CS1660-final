FROM ubuntu
RUN apt-get update && apt-get -y install sudo
RUN sudo apt-get -y install python3.8
RUN sudo apt-get install -y firefox
RUN mkdir -p /usr/jupyter
COPY ./jupyter_service/src /usr/jupyter
COPY ./display.py /usr/jupyter
WORKDIR /usr/jupyter
CMD ["python3","app.py"]