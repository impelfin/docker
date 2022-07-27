build:
	docker build -t mongo .
run :
	docker run -d -p 27017:27017 -v /Users/lune/Documents/GitHub/docker/mongo/data:/data/db --name=mongo mongo
exec :
	docker exec -it mongo /bin/bash
ps :
	docker ps -a
img :
	docker images
