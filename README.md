# Silly simple image converter app to learn kubernetes

docker build -t flask-app:latest .
kubectl set image deployment/flask-app flask-app=flask-app:latest
