# Step1 : Base images
FROM ubuntu:latest

# Step2 : Package install
RUN apt -y update && apt -y upgrade && apt -y install git net-tools vim

# Step3 : Specify a working directory
WORKDIR '/root'

# Step4 : Config file copy
RUN git clone http://github.com/impelfin/docker
RUN cp docker/ubuntu/.exrc .
RUN cp docker/ubuntu/.bashrc .
RUN rm -rf docker
