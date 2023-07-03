import argparse
import ipaddress

# Create an argument parser
parser = argparse.ArgumentParser(description='Calculate the number of hosts in an IPv4 network.')

# Add argument for IPv4 address
parser.add_argument('-i', type=str, help='An IPv4 address in CIDR notation')

# Parse the arguments
args = parser.parse_args()

# Check if an IPv4 address was provided
if args.i:
    network = ipaddress.ip_network(args.i)
    num_hosts = network.num_addresses - 2
    print(f'The number of hosts in the IPv4 network {args.i} is: {num_hosts}')
