from scapy.all import sniff

def capture_packets():
    return sniff(prn=lambda x: x, store=False)
