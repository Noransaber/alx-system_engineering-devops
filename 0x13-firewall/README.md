# 0x13. Firewall

**Concepts**
For this project, we expect you to look at this concept:

- [Web stack debugging](https://intranet.alxswe.com/concepts/68)


<img src="fire.png" alt="">

## Resources
**Read or watch:**

- [What is a firewall](https://en.wikipedia.org/wiki/Firewall_%28computing%29)

# More Info
As explained in the web stack debugging guide concept page, telnet is a very good tool to check if sockets are open with telnet IP PORT. For example, if you want to check if port 22 is open on web-02:

`sylvain@ubuntu$ telnet web-02.holberton.online 22`
`Trying 54.89.38.100...`
`Connected to web-02.holberton.online.`
`Escape character is '^]'.`
`SSH-2.0-OpenSSH_6.6.1p1 Ubuntu-2ubuntu2.8`

`Protocol mismatch.`
`Connection closed by foreign host.`
`sylvain@ubuntu$``

We can see for this example that the connection is successful: Connected to web-02.holberton.online.

Now let’s try connecting to port 2222:`
`
`sylvain@ubuntu$ telnet web-02.holberton.online 2222`
`Trying 54.89.38.100...`
`^C`
`sylvain@ubuntu$`
`

## Tasks
- [0. Block all incoming traffic but](https://intranet.alxswe.com/projects/284)
