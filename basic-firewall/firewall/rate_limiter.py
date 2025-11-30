import time

packet_history = {}
RATE_LIMIT = 50  # max packets per second

def rate_limit(ip):
    current_time = int(time.time())

    if ip not in packet_history:
        packet_history[ip] = {}

    if current_time not in packet_history[ip]:
        packet_history[ip][current_time] = 0

    packet_history[ip][current_time] += 1

    if packet_history[ip][current_time] > RATE_LIMIT:
        return False  # Block due to flood attack

    return True
