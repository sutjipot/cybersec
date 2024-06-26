#!/usr/bin/env python3
import sys
import socket


def get_accessible_ports(address, min_port, max_port):
	found_ports = []

	for port in range(min_port, 1+max_port):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.settimeout(1)
		try:
			s.connect((address, port))
			found_ports.append(port)
		except (socket.timeout, socket.error):
			pass
		finally:
			s.close()
	return found_ports


def main(argv):
	address = argv[1]
	min_port = int(argv[2])
	max_port = int(argv[3])
	ports = get_accessible_ports(address, min_port, max_port)
	for p in ports:
		print(p)

# This makes sure the main function is not called immediatedly
# when TMC imports this module
if __name__ == "__main__": 
	if len(sys.argv) != 4:
		print('usage: python %s address min_port max_port' % sys.argv[0])
	else:
		main(sys.argv)
