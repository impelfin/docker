install:
	docker build -t mysql .
run : 
	docker run -d -p 3306:3306 -e MYSQL_ROOT_PASSWORD=1234 -v /Users/lune/Documents/GitHub/docker/mysql:/app --name=mysql mysql
exec :
	docker exec -it mysql /bin/bash
ps :
	docker ps -a
img :
	docker images
