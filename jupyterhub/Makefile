clone:
	git clone https://github.com/impelfin/the-littlest-jupyterhub.git
build:
	docker build -t tljh-systemd . -f ./the-littlest-jupyterhub/integration-tests/Dockerfile
run:
	docker run --privileged --detach --name=tljh-dev --publish 8000:80 -v $$(pwd):/srv/src tljh-systemd 
exec: 
	docker exec tljh-dev sh -c "python3 /srv/src/the-littlest-jupyterhub/bootstrap/bootstrap.py --admin admin"
	rm -rf the-littlest-jupyterhub
stop:
	docker stop tljh-dev
start:
	docker start tljh-dev
logs:
	docker logs tljh-dev 
ps:
	docker ps -a
img:
	docker images
rm:
	docker rm -f $$(docker ps -aq)
rmi:
	docker rmi $$(docker images -q)
