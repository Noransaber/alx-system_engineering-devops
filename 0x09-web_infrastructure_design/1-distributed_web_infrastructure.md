# WEB INFRASTRUCTURE PROJECT TASK 1

[Imgur](https://i.imgur.com/DnmxpFQ.jpg)

## Definitions and Explanations

1. **For every additional element, why are adding it:**
Added a new server so if one fails, the whole server system or network don't collapse while the failed server is being tended to.
2. **What distribution algorithm your load balancer is configured with and how it
works:**
Round Robin algorithm. The Round Robin algorithm is like people taking turns on a swing at the playground. Each person gets a fixed time to swing before they have to let someone else have a turn. It keeps going in a circle, so everyone gets a fair chance to swing, just like computer processes take turns using the CPU.
3. **Is your load-balancer enabling an Active-Active or Active-Passive setup, explain
the difference between both:**
The load balancer enables Active-Active setup where both nodes (servers) are actively running the same kind of service simultaneously.
In Active-Passive setup, if the first node is active, the second node will be on standby.
4. **How a database Primary-Replica (Master-Slave) cluster works:**
In a Primary-Replica (Master-Slave) database cluster, there's one primary/master node that handles write operations (updates to the database). Replicas/slave nodes copy data from the primary and handle read operations. This setup improves performance and provides redundancy; if the primary fails, one of the replicas can take over as the new primary to ensure data availability and reliability.
5. **What is the difference between the Primary node and the Replica node in regard to
the application:**
A replica node is a copy of the primary node, they provide redundant copies of the application codebase to protect against hardware failure and increase capacity to serve read requests like searching or retrieving a document.

## Issues

1. **SPOF(Single Point Of Failure):**
The single point of failure in this infrastructure is having only one load balancer
2. **Security issues(no firewall, no HTTPS):**
The security issues are:
a. The application communicate over unsecure HTTP protocol which might give attackers a chance to doublecross sensitive datas being transmitted
b. The application doesn’t have a firewall, This can allow an attacker to perform a denial of service attack(DOS or DDOS) that may cause a major downtime in the system, or allow a malicious attacker to breach the system exploiting unknown open ports and perform data exfiltration.
3. **No monitoring:**
Monitoring the application would allow the owner to identify any problems, downtime, or security threats and resolve them quickly before they turn into a serious problem. It will also improve productivity and as well improve user experience.
