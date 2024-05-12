#!/usr/bin/env bash
# configures web servers for application deployment

# update and upgrade
apt update && apt upgrade -y

web_static="/data/web_static"
test_dir="$web_static/releases/test"
shared="$web_static/shared"
html_file="$test_dir/index.html"
nginx_config="/etc/nginx/sites-available/default"

# create necessary folders
mkdir -p "$test_dir" "$shared"

# create html test file
html_content="<!DOCTYPE html>
<html>
	<head></head>
	<body>
		<p>Holberton school</p>
	</body>
</html>"
touch "$html_file"
echo "$html_content" > "$html_file"

# link /data/web_static/current to  /data/web_static/releases/test
if [ -L "/data/web_static/current" ]; then
	rm "/data/web_static/current"
	ln -s "$test_dir" "/data/web_static/current"
else
	ln -s "$test_dir" "/data/web_static/current"
fi

# give ownership of /data to ubuntu
chown -R ubuntu:ubuntu /data/

if grep "location /hbnb_static" "$nginx_config" > /dev/null; then
	echo "" > /dev/null
else
	# add hbnb location rules 
	sed -i \
		'/error_page/i \\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}\n' \
		/etc/nginx/sites-available/default
fi

# restart nginx
service nginx restart
