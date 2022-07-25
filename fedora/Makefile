install:
	docker build -t fedora .
run : 
	docker run -d -it --name fedora -p 8000:8000 -v /Users/lune/Documents/GitHub/docker/fedora:/app fedora
exec :
	docker exec -it fedora /bin/bash
ps :
	docker ps -a
img :
	docker images
