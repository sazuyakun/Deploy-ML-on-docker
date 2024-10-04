# Deploying ML model using Docker

To run this program on your local device

```bash
  docker pull sazuyakun/simple-docker-ml-model:latest
  docker run -p 5000:5000 sazuyakun/simple-docker-ml-model
```

or

```bash
  git clone https://github.com/sazuyakun/Deploy-ML-on-docker
```

then

```bash
  python app/model.py
```

and then finally

```bash
  python app/api.py
```
