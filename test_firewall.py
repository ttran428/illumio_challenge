import firewall
def test_firewall_initializer():
	fw = firewall.Firewall("tests/test.csv")
	assert fw.rules == ['inbound,tcp,80,192.168.1.2\r\n', 
									'outbound,tcp,10000-20000,192.168.10.11\r\n', 
									'inbound,udp,53,192.168.1.1-192.168.2.5\r\n', 
									'outbound,udp,1000-2000,52.12.48.92']

def test_accept_packet():
	fw  = firewall.Firewall("tests/test.csv")

	#provided test cases
	assert fw.accept_packet("inbound", "tcp", 80, "192.168.1.2") == True
	assert fw.accept_packet("inbound", "udp", 53, "192.168.2.1") == True
	assert fw.accept_packet("outbound", "tcp", 10234, "192.168.10.11") == True
	assert fw.accept_packet("inbound", "tcp", 81, "192.168.1.2") == False
	assert fw.accept_packet("inbound", "udp", 24, "52.12.48.92") == False

	# other tests and edge cases
	assert fw.accept_packet("inbound", "udp", 80, "192.168.1.2") == False
	assert fw.accept_packet("outbound", "udp", 80, "192.168.1.2") == False
	assert fw.accept_packet("inbound", "udp", 53, "192.168.2.6") == False
	assert fw.accept_packet("outbound", "tcp", 10000, "192.168.10.11") == True
	assert fw.accept_packet("outbound", "tcp", 20000, "192.168.10.11") == True
	assert fw.accept_packet("outbound", "tcp", 9999, "192.168.10.11") == False
	assert fw.accept_packet("outbound", "tcp", 20001, "192.168.10.11") == False