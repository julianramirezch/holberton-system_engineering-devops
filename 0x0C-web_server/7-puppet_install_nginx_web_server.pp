# Puppet configuration

exec { 'update':
    command => '/usr/bin/apt -y update',
}

package { 'nginx':
    ensure => installed,
}

exec {'/usr/bin/env echo "Holberton School" > /var/www/html/index.nginx-debian.html':}
exec {'/usr/bin/env sed -i "/server_name _;/ a\\\trewrite ^/redirect_me http://www.millonarios.com.co permanent;" /etc/nginx/sites-available/default':}
exec {'/usr/bin/env service nginx start':}
