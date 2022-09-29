# Sam Gross' nogil benchmark

## Prerequisite

All the benchmark results are run under docker images, so please install [docker](https://docs.docker.com/engine/install/) into your benchmark machine.


## Cryptofeed

### 1. Installation

```
make docker_nogil_build INSTALLTION="requirements_cryptofeed.txt"
```

### 2. Run benchmark

```
docker run -v $(pwd):/usr/src/app/output python-gil python -u /usr/src/app/output/cryptofeed_test/basic.py
```

## Webserver

### 1. Installation

```
make docker_nogil_build INSTALLTION="requirements_webserver.txt"
```

### 2. Run server

```
docker run -v $(pwd):/usr/src/app/output -e FLASK_APP=output.webserver_test.flask_benchmark -p 8000:8000 python-gil python -m flask run -h 0.0.0.0 -p 8000
```

### 3. Run benchmark

```
wrk --duration 20s --threads 1 --connections 100 http://127.0.0.1:8000/ping
```
