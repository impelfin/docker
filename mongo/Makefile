build:
	docker build -t mongo .
run : 
	docker run -d -p 27017:27017 -v /Users/lune/Documents/GitHub/docker/mongo:/db --restart always --name=mongo mongo --auth 
exec :
	docker exec -it mongo /bin/bash
ps :
	docker ps -a
img :
	docker images
