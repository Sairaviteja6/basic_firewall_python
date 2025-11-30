from scapy.layers.inet import TCP

def detect_attack(packet):
    # SYN Flood Detection
    if packet.haslayer(TCP):
        if packet[TCP].flags == "S":   # SYN flag only
            return "Possible SYN Flood"

        if packet[TCP].flags == "F":   # FIN only
            return "Suspicious FIN traffic"

    return None  # Normal
