install:
	docker build -t python .
run : 
	docker run -d -it --name python -p 8000:8000 -v /Users/lune/Documents/GitHub/python:/app python
exec :
	docker exec -it python /bin/bash
ps :
	docker ps -a
img :
	docker images
