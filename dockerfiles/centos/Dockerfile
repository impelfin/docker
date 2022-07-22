# Step1 : base images
FROM dokken:centos-8 

# Step2 : package install 
RUN yum -y update && yum -y install git net-tools vim

# Step3 : Specify a working directory 
WORKDIR '/root'

# Step4 : config file copy
RUN git clone http://github.com/impelfin/docker
RUN cp docker/dockerfiles/centos/.exrc .
RUN cp docker/dockerfiles/centos/.bashrc .
RUN rm -rf docker 
