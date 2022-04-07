FROM python:3.8-slim-buster AS base

# set a directory for the app
WORKDIR /flatfile-demo/

# copy everything
COPY . /flatfile-demo

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# define the port number the container should expose
EXPOSE 5000

# set up db
 RUN python3 manage.py migrate