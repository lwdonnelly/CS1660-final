FROM ubuntu
RUN apt-get update && apt-get -y install sudo
RUN sudo apt-get -y install python3.8
RUN sudo apt-get install -y firefox
RUN mkdir -p /usr/tableau
COPY ./tableau_service/src /usr/tableau
COPY ./display.py /usr/tableau
WORKDIR /usr/tableau
CMD ["python3","app.py"]