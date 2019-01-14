# Silly simple image converter app to easily convert pdf -> jpg/png

# Use

## Use Dockerhub Image

```
docker run --rm -it -p 5000:5000 tyghe/flask_image_convert
```

## Build locally

1. Build the image

   ```
   docker build -t tyghe/flask_image_convert:latest .
   ```

1. Run the image

   ```
   docker run --rm -it -p 5000:5000 tyghe/flask_image_convert:latest
   ```

1. Browse to http://localhost:5000
