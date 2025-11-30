import json
from scapy.layers.inet import TCP, UDP, IP

RULES_FILE = "config/rules.json"

def load_rules():
    with open(RULES_FILE, "r") as f:
        return json.load(f)

def process_packet(packet):
    rules = load_rules()
    ip_layer = packet.getlayer(IP)
    src_ip = ip_layer.src

    # Check if IP is blocked
    if src_ip in rules["blocked_ips"]:
        return "BLOCK"

    # Check if IP is authenticated
    if src_ip not in rules["authenticated_ips"]:
        return "BLOCK"

    # Check TCP/UDP ports
    if packet.haslayer(TCP):
        dport = packet[TCP].dport
        if dport in rules["allowed_ports"]:
            return "ALLOW"
        else:
            return "BLOCK"

    if packet.haslayer(UDP):
        dport = packet[UDP].dport
        if dport in rules["allowed_ports"]:
            return "ALLOW"
        else:
            return "BLOCK"

    return "ALLOW"
