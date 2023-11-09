#!/bin/bash

# Install Nginx if not already installed
if ! command -v nginx &> /dev/null; then
    sudo apt-get update
    sudo apt-get -y install nginx
fi

# Create necessary folders
sudo mkdir -p /data/web_static/{releases/test,shared}

# Create a fake HTML file
echo "<html><head></head><body>Test Page</body></html>" | sudo tee /data/web_static/releases/test/index.html > /dev/null

# Create symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership to ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration
config_block="
    location /hbnb_static {
        alias /data/web_static/current/;
        index index.html;
    }
"
sudo sed -i "/server {/a $config_block" /etc/nginx/sites-available/default

# Restart Nginx
sudo service nginx restart

exit 0
