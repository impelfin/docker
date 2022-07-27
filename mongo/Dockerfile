# Step1 : Base images
FROM mongo

# Step2 : Package install
RUN apt -y update && apt -y upgrade && apt -y install git net-tools vim

# Step3 : Copy conf file
COPY ./db/mongod.conf /etc/mongod.conf

# Step4 : Specify a working directory
WORKDIR '/root'

# Step5 : Config file copy
RUN git clone http://github.com/impelfin/docker
RUN cp docker/mongo/.exrc .
RUN cp docker/mongo/.bashrc .
RUN rm -rf docker
