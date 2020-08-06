# Puppet configuration

exec { 'update':
    command => '/usr/bin/apt -y update',
}

package { 'nginx':
    ensure => installed,
}

exec { 'configuration':
    command => 'sudo echo "Holberton School" | sudo tee /var/www/html/index.html; sudo sed -i "/server_name _;/ a\\\trewrite ^/redirect_me http://www.millonarios.com.co permanent;" /etc/nginx/sites-available/default; sudo service nginx start',
}
