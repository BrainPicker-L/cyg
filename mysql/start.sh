#!/usr/bin/env bash
echo "create a mysql container.."
docker run -d --name mysql \
-p 3307:3306 \
-v /data/mysql:/var/lib/mysql \
-e MYSQL_ALLOW_EMPTY_PASSWORD=yes \
-e MYSQL_DATABASE="cyg" \
-default-authentication-plugin=mysql_native_password \
mysql:8.0