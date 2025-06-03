import socket


host = "google.com"
ports = range(100)

for port in ports:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(0.5)
    code = client.connect_ex((host, port))
    if code == 0:
        print("[+] {} open".format(port));
