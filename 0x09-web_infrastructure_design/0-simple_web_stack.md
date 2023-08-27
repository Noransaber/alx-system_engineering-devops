# steps:

## DNS:

1- the user sends a request to his internet service provider(ISP) asking to reach ***www.foobar.com***

2- the ISP which has a resolver server searches for the required url in this resolver if it's available it sends bach the ip address of the requested URL

3- if the URL is not available in the resolver server the resolver asks the root server

4- root will send back the address of the TLD server (the server responsible for all the domains of .com) to the resolver

5- resolver then sends a request to the TLD server
which will return the right name after removing the www. (using either cname or a records) and the address of the authoritative name server

6- the resolver then sends a request with the url to the authoritative name server which knows everything about the requested url including the ip address of the server having it

7- the authoritative name server returns back the ip address of the requested server to the resolver server

8- finally the resolver sends back the this ip to the client which will send the request to access to site

## accessing the site:

**after returning the ip to the client the client then sends a http of a https request to the server with the right ip address which is 8.8.8.8**

9- this server is the server which has the web server software(Nginx) and searches for the data wanted in it's static database and sends back an HTTP response if the data is found there.

**NOTE: data requested by http is usually some html, css, JS, images, files..etc.**

10- the web server sends some code(request) to the application server which in return handle the dynamic content of this site and then manages the application logic, data manipulation, and user requests separate from the web server.

**NOTE: web server primary role is to handle the http requests from the clients maybe the static content**
