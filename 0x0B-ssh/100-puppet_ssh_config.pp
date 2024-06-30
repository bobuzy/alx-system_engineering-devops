# Use puppet to make changes to config file
file { '/etc/ssh/ssh_config':
content => "
HostName 54.90.1.38
User ubuntu
IdentityFile ~/.ssh/school
PasswordAuthentication no",
}
