# To start the Grobid Server in docker

```
docker run --rm --init --ulimit core=0 -p 8070:8070 lfoppiano/grobid:0.8.0
```

run `main.py` to extract the text from pdf file

run `getting_metadata.py` to extract the metadata from grobid
