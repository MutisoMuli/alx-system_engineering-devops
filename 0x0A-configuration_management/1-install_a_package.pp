# A puppet manifest installing flask v2.1.0 a package of pip3
# Version to install is specified using the ensure attribute
package { 'flask':
  ensure   => '2.1.0',
  provider => pip3,
}
