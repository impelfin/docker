# Step1 : Base images
FROM fedora

# Step2 : Package install
RUN yum -y update && yum -y install git net-tools vim

# Step3 : Specify a working directory
WORKDIR '/root'

# Step4 : Config file copy
COPY ./.bashrc .
COPY ./.exrc .
