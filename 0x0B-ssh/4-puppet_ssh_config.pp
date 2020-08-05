#Configuration File

file { 'holberton_server':
    ensur => file,
    content => 'Host holberton_server
                    HostName 34.73.118.163
                    User ubuntu
                    IdentityFile ~/.ssh/holberton
                    PasswordAuthentication no',
}

