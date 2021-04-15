FROM ubuntu
RUN apt-get update && apt-get -y install sudo
RUN sudo apt-get -y install python3.8
RUN sudo apt-get install -y firefox
RUN mkdir -p /usr/ibm_sas
COPY ./ibm_sas_service/src /usr/ibm_sas
COPY ./display.py /usr/ibm_sas
WORKDIR /usr/ibm_sas
CMD ["python3","app.py"]