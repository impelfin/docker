# Step1 : Base images
FROM fedora

# Step2 : Package install
RUN yum -y update && yum -y install git net-tools vim

# Step3 : Specify a working directory
WORKDIR '/root'

# Step4 : Config file copy
RUN git clone http://github.com/impelfin/docker
RUN cp docker/fedora/.exrc .
RUN cp docker/fedora/.bashrc .
RUN rm -rf docker
