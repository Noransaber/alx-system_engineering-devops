exec { 'fix-wordpress':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => ['/bin', '/usr/bin', '/usr/sbin'],
  onlyif  => "test -f /var/www/html/wp-settings.php",  # Add this line to check if the file exists
}
