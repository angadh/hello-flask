#!/bin/bash

# Start Gunicorn
gunicorn -w 2 -b 127.0.0.1:5000 app:app &

# Start NGINX
nginx -g 'daemon off;'
