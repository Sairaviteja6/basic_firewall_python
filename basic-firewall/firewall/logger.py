import logging
import os
import threading

# Absolute path to project root (one level above 'firewall')
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Ensure 'logs' folder exists in project root
LOGS_FOLDER = os.path.join(PROJECT_ROOT, "logs")
os.makedirs(LOGS_FOLDER, exist_ok=True)

# Full path to log file
LOG_FILE = os.path.join(LOGS_FOLDER, "firewall.log")

# Configure logging
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Thread-safe list for live SSE feed
log_events = []
log_lock = threading.Lock()

def log_event(message):
    logging.info(message)
    with log_lock:
        log_events.append(message)

def get_events():
    with log_lock:
        events = log_events.copy()
        log_events.clear()
    return events
