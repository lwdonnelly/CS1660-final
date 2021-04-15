FROM ubuntu
RUN apt-get update && apt-get -y install sudo
RUN sudo apt-get -y install libxext6
RUN sudo apt-get -y install libxrender1 libxtst6 libxi6
RUN sudo apt-get -y install fontconfig

RUN sudo apt-get -y install python3.8 python3-tk
RUN sudo apt-get -y install python3-pip
RUN pip3 install docker
RUN sudo apt-get install -y apt-transport-https ca-certificates curl gnupg lsb-release
RUN curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
RUN echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
RUN ln -s /usr/lib/libfontconfig.so.1 /usr/lib/libfontconfig.so && \
    ln -s /lib/libuuid.so.1 /usr/lib/libuuid.so.1 && \
    ln -s /lib/libc.musl-x86_64.so.1 /usr/lib/libc.musl-x86_64.so.1
ENV LD_LIBRARY_PATH /usr/lib
RUN mkdir -p /usr/main
COPY ./main_service/src /usr/main
COPY ./display.py /usr/main
WORKDIR /usr/main
CMD ["python3","MainService.py"]