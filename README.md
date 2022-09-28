# Sam Gross' nogil benchmark

## Cryptofeed

### 1. Installation

```
make docker_nogil_build INSTALLTION="requirements_cryptofeed.txt"
```

### 2. Run benchmark

```
docker run -v $(pwd):/usr/src/app/output python-gil python -u /usr/src/app/output/cryptofeed_test/basic.py
```
