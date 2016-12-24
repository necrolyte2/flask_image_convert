# Silly simple image converter app to learn kubernetes

I forgot the kubectl commands for initial deployment but then you can do this to redeploy

docker build -t flask-app:latest .

kubectl set image deployment/flask-app flask-app=flask-app:latest
