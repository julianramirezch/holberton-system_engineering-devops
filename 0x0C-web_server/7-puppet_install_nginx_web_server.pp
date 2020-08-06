# Puppet configuration

exec { 'update':
    command => '/usr/bin/apt -y update',
}

package { 'nginx':
    ensure => installed,
}

file { 'index.html':
    ensure  => file,
    path    => '/etc/var/www/index.html',
    content => 'Holberton School',
}

exec { 'sed':
    command => '/usr/bin/sed -i "/server_name _;/ a\\\trewrite ^/redirect_me http://www.millonarios.com.co permanent;" /etc/nginx/sites-available/default',
}
