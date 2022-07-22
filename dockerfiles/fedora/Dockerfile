# Step1 : base images
FROM fedora 

# Step2 : package install 
RUN yum -y update && yum -y install git net-tools vim

# Step3 : Specify a working directory 
WORKDIR '/root'

# Step4 : config file copy
RUN git clone http://github.com/impelfin/docker
RUN cp docker/dockerfiles/fedora/.exrc .
RUN cp docker/dockerfiles/fedora/.bashrc .
RUN rm -rf docker 
