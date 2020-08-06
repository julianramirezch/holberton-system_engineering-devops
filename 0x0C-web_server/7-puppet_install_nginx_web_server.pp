# Puppet configuration

exec { 'update':
    command => '/usr/bin/apt -y update',
}

package { 'nginx':
    ensure => installed,
}

exec { 'update':
    command => '/usr/bin/echo "Holberton School" | sudo tee /var/www/html/index.html',
    command => '/usr/bin/sed -i "/server_name _;/ a\\\trewrite ^/redirect_me http://www.millonarios.com.co permanent;" /etc/nginx/sites-available/default',
    command => '/usr/sbin/service nginx start',
}
