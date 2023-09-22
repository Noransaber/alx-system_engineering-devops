# Create a file in /tmp

file {'/tmp/school':,
mode => '0644',
owner => 'www-data',
group => 'www-data',
content => 'I love Puppet'
}


