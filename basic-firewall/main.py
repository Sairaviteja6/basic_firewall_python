# main.py

from firewall.packet_capture import capture_packets
from firewall.rule_engine import process_packet
from firewall.ids import detect_attack
from firewall.rate_limiter import rate_limit
from firewall.logger import log_event
from datetime import datetime

def main():
    print("🔥 Advanced Firewall Started... Listening for packets")

    for packet in capture_packets():
        src_ip = packet[0][1].src  # Source IP of the packet

        # ===== Rate Limiting (DDoS Protection) =====
        if not rate_limit(src_ip):
            msg = f"{datetime.now()} - BLOCK (Rate Limit): Packet Flood from {src_ip}"
            log_event(msg)
            print(f"[BLOCK] Flood Detected from {src_ip}")
            continue

        # ===== IDS Monitoring =====
        ids_alert = detect_attack(packet)
        if ids_alert:
            msg = f"{datetime.now()} - ALERT: {ids_alert} from {src_ip}"
            log_event(msg)
            print(f"[ALERT] {ids_alert} from {src_ip}")

        # ===== Rule Engine (ALLOW/BLOCK Logic) =====
        action = process_packet(packet)

        if action == "ALLOW":
            msg = f"{datetime.now()} - ALLOW: Packet from {src_ip}"
            log_event(msg)
            print(f"[ALLOW] Packet from {src_ip}")
        else:
            msg = f"{datetime.now()} - BLOCK: Packet from {src_ip}"
            log_event(msg)
            print(f"[BLOCK] Packet from {src_ip}")

if __name__ == "__main__":
    main()
