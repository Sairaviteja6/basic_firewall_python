import json
import socket

def get_client_ip():
    hostname = socket.gethostname()
    return socket.gethostbyname(hostname)

def authenticate():
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == "admin" and password == "1234":
        print("✔ Authentication Successful")
        add_authenticated_ip()
        return True
    else:
        print("❌ Authentication Failed")
        return False

def add_authenticated_ip():
    ip = get_client_ip()
    with open("config/rules.json", "r") as f:
        rules = json.load(f)

    if ip not in rules["authenticated_ips"]:
        rules["authenticated_ips"].append(ip)

    with open("config/rules.json", "w") as f:
        json.dump(rules, f, indent=4)

    print(f"IP {ip} added to authenticated list")
