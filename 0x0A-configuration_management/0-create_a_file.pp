# A puppet manifest that creates a file school in /tmp
# The school file has permission 0744
# Belongs to user www-data
# Belongs to group www-data
file { '/tmp/school':
  ensure  => present,
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet',
}

