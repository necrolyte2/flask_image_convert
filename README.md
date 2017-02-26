# Silly simple image converter app to learn kubernetes

# Use

1. Build the image

   ```
   docker build -t tyghe/flask_image_convert:latest .
   ```

1. Run the image

   ```
   docker run --rm -it -p 5000:5000 tyghe/flask_image_convert:latest
   ```

1. Browse to http://localhost:5000

## Helm Chart

1. Install minikube

   https://github.com/kubernetes/minikube

1. Install helm

   https://github.com/kubernetes/helm

1. Init helm

   ```
   helm init
   ```
