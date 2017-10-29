# illumio_challenge

I tested my solution by creating a firewall and importing packets to see if they were accepted by the firewall. I used the basic firewall dimensions given in the specs and wrote a few more of my tests.

The naive solution that I created was to simply store all of the rules inside a list, and then check the packet against the list one by one. This is of course inefficient because it takes big O(n), if n is the amount of rules. My next idea is to store the rules inside a nested dictionary/hashtable by direction and protocol. However, this would still take in the worst case big O(n), since all of the rules could have the same direction and protocol, but if the rules were somewhat "spread out randomly", it would be practically faster.

I couldn't figure out how to put into a hashtable using the IP or port, since it could take ranges. I thought about splitting each port into ranges of 1000 ports each(e.g. [0,1000], [1001, 2000]) and doing a similar thing with the IP address, so that at the end of nested hashtable, we would have a lot less rules to sort through. However, I did not have enough time to implement this.

Another idea I had was that for each packet, create a Rule using the packet and checking if the Rule was in a hashtable. However, this would mean since IP and ports could take ranges, I would have to create many rules for each IP range which would take up a lot of space depending on how big the range is. This would make the constructor slow, since it would have a big O(n * p * q) time, with n = number of Rules, p = range of IP, and q = range of port. Using this method though, seeing if a packet could be accepted would be in big O(1) because checking for inclusion in a hashtable is constant time. This would of course, be a better runtime since in the specs, it expects "reasonably quick" runtime after the constructor is built, but I also did not have enough time to implement this after I got the naive version working.

Anyways, I'm interested in working on the data team! I'm particularly interested on working on Illummination, recommending optimized policies to the user. Next semester I'm taking CS161(Computer Security) as well as EE127(Optimization Models in Engineering, one of the machine learning courses) and I think working on finding optimized policies would be a really good intersection of these two classes. I do not know so much about Illumination 2.0, but I believe that working on generating policies would also fit in my interests of working with security and optimization.


