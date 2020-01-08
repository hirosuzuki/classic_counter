install:
	sudo apt install apache2
	sudo install -d /var/www/classic-counter.hirosuzuki.net
	sudo install -d /var/www/classic-counter.hirosuzuki.net/html
	sudo install -d /var/www/classic-counter.hirosuzuki.net/cgi-bin
	sudo install -d /var/www/classic-counter.hirosuzuki.net/data
	sudo install -m 755 counter.cgi /var/www/classic-counter.hirosuzuki.net/cgi-bin/counter.cgi
	sudo install -m 644 index.html /var/www/classic-counter.hirosuzuki.net/html/index.html
	sudo touch /var/www/classic-counter.hirosuzuki.net/data/counter.dat
	sudo chown www-data:www-data /var/www/classic-counter.hirosuzuki.net/data/counter.dat
	sudo install -m 644 classic-counter.hirosuzuki.net.conf /etc/apache2/sites-enabled/
	sudo a2enmod cgi
	sudo apachectl configtest && sudo apachectl restart
