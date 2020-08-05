#Configuration File

file { 'holberton_server':
    ensure  => file,
    path => '/etc/ssh/ssh_config',
    content => 'Host holberton_server
    HostName 34.73.118.163
    User ubuntu
    IdentityFile ~/.ssh/holberton
    PasswordAuthentication no',
}

