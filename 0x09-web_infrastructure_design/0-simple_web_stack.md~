the design: https://imgur.com/a/6i8LG94

# steps:

## DNS:

> 1- the user sends a request to his internet service provider(ISP) asking to reach ***www.foobar.com***

> 2- the ISP which has a resolver server searches for the required url in this resolver if it's available it sends bach the ip address of the requested URL

> 3- if the URL is not available in the resolver server the resolver asks the root server

> 4- root will send back the address of the TLD server (the server responsible for all the domains of .com) to the resolver

> 5- resolver then sends a request to the TLD server
> which will return the right name after removing the www. (using either cname or a records) and the address of the authoritative name server

> 6- the resolver then sends a request with the url to the authoritative name server which knows everything about the requested url including the ip address of the server having it

> 7- the authoritative name server returns back the ip address of the requested server to the resolver server

> 8- finally the resolver sends back the this ip to the client which will send the request to access to site

## accessing the site:

**after returning the ip to the client the client then sends a http of a https request to the server with the right ip address which is 8.8.8.8**

9- this server is the server which has the web server software(Nginx) and searches for the data wanted in it's static database and sends back an HTTP response if the data is found there.

> **NOTE: data requested by http is usually some html, css, JS, images, files..etc.**

10- the web server sends some code(request) to the application server which in return handle the dynamic content of this site and then manages the application logic, data manipulation, and user requests separate from the web server.

> **NOTE: web server primary role is to handle the http requests from the clients and maybe the static content**

11- the application server accesses the data store and returns what's requested to the web server which will return a http response to the client

## specifics about this infrastructure:

> **server**: it's a computer that provides services on behalf of clients (the end users who try to access it through the internet) it may be a real computer, a software or even a virtual machine

> **domain name and it's role**: Domain names serve as human-readable addresses for websites, making it easier for users to access online resources without having to remember numeric IP addresses.

> **type of DNS record www is in www.foobar.com**: it's CNAME (canonical name) record which translates the www.foobar.com to foobar.com

> **the role of the web server**: Handle mainly the http requests and sees if it has the the requested data on the it's static DB and sends requests to the application server to get the data requested if not available in the static DB.

> **role of the application server**: Handle all the dynamic content of web applications and it's main function to handle the application logic (calculations, data processing and other tasks) and the backend of the application which includes data management such as retrieving and sending data from and to the data base which in return gives the user the dynamic experience of a web application

> **role of the database**: management of the data of the data which include data storing, manipulation. It saves all the user and the web application data needed to have a functional web application

> **the server is using to communicate with the computer of the user requesting the website** the Hyper Text Transfer Protocol (HTTP) which enables the transfer of data like html or css docs between the server and the client as the client sends a request for certain resources or data then the web server sends a response to this request with the required data

## Issues:

### 1- SPOF(single point of failure):

    	- since the infrastructure consists only from non-redundant parts 1 server, 1 web server, 1 application server ...etc so any failure in any of them (SPOF) will result in a failure in the whole system and in return the whole web application will fail

### 2- Downtime when maintenance needed:

    	- unfortunately there will be a downtime if any changes needed to be made to the server because there is only 1vso there will be a loss in service

### 3- Cannot scale if too much incoming traffic:

    	- since there are only 1 server and no load balancers the server won't scale with too much traffic and maybe a loss or a slowdown in the services

#### The Main solution for all the issues is redundancy
