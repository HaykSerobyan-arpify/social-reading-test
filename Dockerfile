# Dockerfile

FROM python:3.9-buster

# install nginx
# RUN apt-get update && apt-get install nginx vim -y --no-install-recommends
# COPY nginx.default /etc/nginx/sites-available/default
# RUN ln -sf /dev/stdout /var/log/nginx/access.log && ln -sf /dev/stderr /var/log/nginx/error.log

# copy source and install dependencies
RUN pip install --upgrade pip

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./app /app

WORKDIR /app

COPY ./entrypoint.sh /
ENTRYPOINT ["sh", "/entrypoint.sh"]

