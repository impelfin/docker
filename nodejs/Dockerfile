# Step1 : Base images
FROM node:14.16.1

# Step2 : Package install
RUN apt -y update && apt -y upgrade && apt -y install git net-tools vim

# Step3 : Specify a working directory
WORKDIR '/root'

# Step4 : Config file copy
RUN git clone http://github.com/impelfin/docker
RUN cp docker/nodejs/.exrc .
RUN cp docker/nodejs/.bashrc .
RUN rm -rf docker
