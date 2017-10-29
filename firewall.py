# basic interface given outline of the Assignment.

#intial naive solution storing all rules in a list and checking each rule.
# class Firewall:
# 	def __init__(self, path_to_csv):
# 		self.rules = []
# 		with open(path_to_csv, "r") as f:
# 			for line in f:
# 				rule = Rule(line)
# 				self.rules.append(rule)
# 	def accept_packet(self, direction, protocol, port, ip_address):
# 		for rule in self.rules:
# 			if rule.compare(direction, protocol, port, ip_address):
# 				return True
# 		return False

#less naive solution that will only check rules if they match the 
# direction and protocol.
class Firewall:
	def __init__(self, path_to_csv):
		self.rules = {"inbound": {
						"udp": set(),
						 "tcp": set()
					 },
					  "outbound": {
					  	"udp": set(),
					  	"tcp": set()
					  }
		}

		with open(path_to_csv, "r") as f:
			for line in f:
				rule = Rule(line)
				self.rules[rule.direction][rule.protocol].add(rule)
	def accept_packet(self, direction, protocol, port, ip_address):
		for rule in self.rules[direction][protocol]:
			if rule.compare(direction, protocol, port, ip_address):
				return True
		return False

class Rule:
	def __init__(self, rule_params):
		# splits up string into all of the parameters
		all_params = [param.strip() for param in rule_params.split(",")]
		self.direction = all_params[0]
		self.protocol = all_params[1]
		self.port = Range_Vars(all_params[2])
		self.ip_address = Range_Vars(all_params[3].strip("\n").strip("\r"))
	def compare(self, direction, protocol, port, ip_address):
		return (self.direction == direction and
				self.protocol == protocol and
				self.port.compare(str(port)) and
				self.ip_address.compare(ip_address))


#class that represents both Ports and IP since they are
#implemented the same way.
class Range_Vars:
	def __init__(self, valid_params):
		if "-" in valid_params:
			first, last = valid_params.split("-")
			self.range = True
			self.params = [first, last]
		else:
			self.range = False
			self.params = valid_params
	def compare(self, param):
		if self.range:
			return param >= self.params[0] and param <= self.params[1]
		return param == self.params

# class Port:
# 	def __init__(self, valid_ports):
# 		if "-" in valid_ports:
# 			first, last = valid_ports.split("-")
# 			self.range = True
# 			self.port = [first, last]
# 		else:
# 			self.range = False
# 			self.port = valid_ports
# 	def compare(self, port):
# 		if self.range:
# 			return port >= self.port[0] and port <= self.port[1]
# 		return port == self.port


# class IP:
# 	def __init__(self, valid_IP):
# 		if "-" in valid_IP:
# 			first, last = valid_IP.split("-")
# 			self.range = True
# 			self.IP = [first, last]
# 		else:
# 			self.range = False
# 			self.IP = valid_IP
# 	def compare(self, IP):
# 		if self.range:
# 			return IP >= self.IP[0] and IP <= self.IP[1]
# 		return IP == self.IP
