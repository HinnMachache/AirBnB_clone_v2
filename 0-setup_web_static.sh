#!/usr/bin/env bash
# Script that sets up servers for web-static

sudo apt-get update
sudo apt-get -y install nginx

mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/current/

echo "Hello world from Web Static" | sudo tee /data/web_static/releases/test/index.html

ln -sf /data/web_static/releases/test/ /data/web_static/current/

echo -e "<html>\n  <head>\n  </head>\n  <body>\n    Holberton School\n  </body>\n</html>" | sudo tee /data/web_static/current/index.html

sudo chown -R ubuntu:ubuntu /data/

echo "server {
        listen      80 default_server;
        listen      [::]:80 default_server;

        root            /var/www/html;
        index           index.html index.htm index.nginx-debian.html;

        add_header X-Served-By $HOSTNAME;

        location /hbnb_static{
            alias /data/web_static/current/;
            autoindex off;
        }

         location /redirect_me {
                return 301 https://www.youtube.com/watch?v=TfgBHC5gvTI;
        }

        error_page 404 /404.html;
        location /404 {
                root /var/www/html/;
                internal;
        }

}
" >/etc/nginx/sites-available/default

sudo -t nginx

sudo service nginx restart