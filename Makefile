INSTALLATION="requirements_pyperformance.txt"


docker_gil_build:
	@docker build . --file Dockerfile_gil --tag python-gil --build-arg REQUIREMENTS_FILE=${INSTALLATION}

docker_nogil_build:
	@docker build . --file Dockerfile_nogil --tag python-nogil --build-arg REQUIREMENTS_FILE=${INSTALLATION}
