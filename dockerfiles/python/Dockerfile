# Step1 : base images
FROM python:latest

# Step2 : package install 
RUN apt -y update && apt -y upgrade && apt -y install git net-tools vim

# Step3 : Specify a working directory 
WORKDIR '/root'

# Step4 : config file copy
RUN git clone http://github.com/impelfin/docker
RUN cp docker/dockerfiles/python/.exrc .
RUN cp docker/dockerfiles/python/.bashrc .
RUN rm -rf docker 
