import socket

website = input("enter any website url ->")

ip = socket.gethostbyname(website)

print(f"ip address of {website} -> {ip}")