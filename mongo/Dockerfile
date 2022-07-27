# Step1 : Base images
FROM mongo

# Step2 : Package install
RUN apt -y update && apt -y upgrade && apt -y install git net-tools vim

# Step3 : Copy conf file
COPY ./db/mongod.conf /etc/mongod.conf

# Step4 : config file copy
RUN systemctl restart mongod
