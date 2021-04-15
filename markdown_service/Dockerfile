FROM ubuntu
RUN apt-get update && apt-get -y install sudo
RUN sudo apt-get -y install git
RUN sudo apt-get -y install python3.8
RUN sudo apt-get -y install xterm
RUN sudo apt-get -y install python3-pip
ENV LD_LIBRARY_PATH /usr/lib
RUN mkdir -p /usr/markdown
COPY ./markdown_service/src /usr/markdown
COPY ./display.py /usr/markdown
WORKDIR /usr/markdown
CMD ["python3","app.py"]