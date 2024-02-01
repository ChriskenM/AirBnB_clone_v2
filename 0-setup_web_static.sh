#!/usr/bin/env bash
#sets up your web servers for the deployment

sudo apt-get update
sudo apt-get install -y nginx

sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
echo "<html><head></head><body>Holberton School</body></html>" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu /data/
sudo chgrp -R ubuntu /data/

echo "server {
  listen 80 default_server;
  listen [::]:80 default_server;
  add_header X-Served-By \$HOSTNAME;
  root /var/www/html;
  index index.html index.htm;

  location /hbnb_static {
    alias /data/web_static/current;
    index index.html index.htm;
  }

  location /redirect_me {
    return 301 http://github.com/;
  }

  error_page 404 /404.html;
  location /404 {
  root /var/www/html;
  internal;
  }
}" | sudo tee /etc/nginx/sites-available/default

sudo service nginx restart
