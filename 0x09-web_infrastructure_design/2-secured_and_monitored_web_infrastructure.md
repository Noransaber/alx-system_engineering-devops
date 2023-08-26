# Alx project 
## Web infrastructure design
## Task 2
## Definition and explanation

<img src="Screenshot 2023-08-26 123112.png" alt="Image of a secured and monitored infrastructure">
Visit Board => https://imgur.com/p26odBC


**Q1. For every additional element why you added them?** 
- We added, firewall for every server to protect it from being attacked or exploited
Also, 1 SSL certification for our server www. Foobar.com and 3 monitoring clients to collect logs and send them to our collector sumologic

**Q2. What are Firewalls for**
- Firewalls are used for network security. They act as barriers between a trusted internal network and untrusted external network, controlling and monitoring incoming and outgoing network traffic to prevent unauthorized access.

**Q3. Why is the traffic served over HTTPS**
- Because data will be transferred in plain text and it will be secured when the data is being encrypted using Transfer Layer Security (TLS)

**Q4. What monitoring is used for**
- If there are any web application performance issues it detects and diagnosis it.

**Q5. How the monitoring tool is collecting data**
- It collects logs from application server, MYSQL Database and Nginx. Log is an automatically generated, time-stamped record of occurrences pertinent to a specific system.

**Q6. Explain what to do if you want to monitor your web server QPS**
- One web server may process a thousand requests per second; therefore, I'll keep an eye on it from the network and application level

# ISSUES
1. Why terminating SSL at the load balancer level is an issue
- because it exposes the decrypted data to potential risks and compromises the end-to-end encryption that SSL provides.

2. Why having only one MySQL server capable of accepting writes is an issue
- This is so that if you have a bug in one of the servers’ components, the bug will also affect the other servers.

3. Why having servers with all the same components (database, web server and application server) might be a problem
- Because if it's down, data can't be uploaded to it or modified, which means some parts of the application won't function.


