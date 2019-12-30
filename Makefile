install:
	sudo install -d /var/www/localhost
	sudo install -d /var/www/localhost/cgi-bin
	sudo install -d /var/www/localhost/data
	sudo install -m 755 counter.cgi /var/www/localhost/cgi-bin/counter.cgi
	sudo touch /var/www/localhost/data/counter.dat
	sudo chown www-data:www-data /var/www/localhost/data/counter.dat

