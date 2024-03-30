# isolate-drums

## Build docker image and run

```bash
docker build -t isolate-drums .
docker run --rm -v $(pwd)/output:/output isolate-drums <youtube-url>
```
