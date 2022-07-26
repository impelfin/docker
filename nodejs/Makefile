build:
	docker build -t node .
run : 
	docker run -d -it --name node -p 3000:3000 -v /Users/lune/Documents/GitHub/nodejs:/app node
exec :
	docker exec -it node /bin/bash
ps :
	docker ps -a
img :
	docker images
