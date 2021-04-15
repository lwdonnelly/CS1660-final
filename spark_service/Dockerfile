FROM ubuntu
RUN apt-get update && apt-get -y install sudo
RUN sudo apt-get -y install python3.8
RUN sudo apt-get -y install python3-pip
RUN pip3 install PySpark
RUN mkdir -p /usr/spark
COPY ./spark_service/src /usr/spark
COPY ./display.py /usr/spark
WORKDIR /usr/spark
CMD ["python3","app.py"]