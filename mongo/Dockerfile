# Step1 : Base images
FROM mongo

# Step2 : Package install
RUN apt -y update && apt -y upgrade && apt -y install git net-tools vim

# Step3 : Specify a working directory
WORKDIR '/root'

# Step3 : Copy mongod.conf file
COPY ./db/mongod.conf /etc/mongod.conf
COPY ./.bashrc .
COPY ./.exec .
