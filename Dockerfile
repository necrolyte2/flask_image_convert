FROM python:2-alpine
MAINTAINER Tyghe Vallard "vallardt@gmail.com"
RUN apk add --no-cache --update imagemagick-dev imagemagick
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENV MAGICK_HOME /usr
ENTRYPOINT ["python"]
CMD ["app.py"]
