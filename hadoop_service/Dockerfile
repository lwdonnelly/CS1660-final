FROM ubuntu
RUN apt-get update && apt-get -y install sudo
RUN sudo apt-get -y install git
RUN sudo apt-get -y install python3.8
RUN sudo apt-get -y install xterm
RUN sudo apt-get install -y wget
ENV LD_LIBRARY_PATH /usr/lib

RUN wget https://apache.claz.org/hadoop/common/hadoop-3.3.0/hadoop-3.3.0.tar.gz
RUN tar zxvf hadoop-3.3.0.tar.gz
RUN export HADOOP_HOME=/usr/hadoop/hadoop-3.3.0
RUN export HADOOP_CONF_DIR=$HADOOP_HOME/etc/hadoop
RUN export PATH=$HADOOP_HOME/bin:$PATH
RUN mkdir -p /usr/hadoop
COPY ./hadoop_service/src /usr/hadoop
COPY ./display.py /usr/hadoop
WORKDIR /usr/hadoop
CMD ["python3","app.py"]