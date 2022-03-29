import argparse


parser = argparse.ArgumentParser()
# Command Line Parameters for Source and Destination IP
parser.add_argument("source_ip", help = "Source IP Address")
parser.add_argument("destination_ip", help = "Destination IP Address")

args = parser.parse_args()

# Get Source and Destination IPs from Command Line
source_ip = args.source_ip
destination_ip = args.destination_ip