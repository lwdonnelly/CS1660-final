FROM ubuntu
RUN apt-get update && apt-get -y install sudo
RUN sudo apt-get -y install python3.8
RUN sudo apt-get install -y markdown
RUN sudo apt-get install -y xterm
RUN mkdir -p /usr/markdown
COPY ./markdown_service/src /usr/markdown
COPY ./display.py /usr/markdown
WORKDIR /usr/markdown
CMD ["python3","app.py"]