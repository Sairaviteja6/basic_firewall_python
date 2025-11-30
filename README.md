# basic_firewall_python 🔥

A simple Python-based firewall that captures network packets, applies rate-limiting, intrusion detection, and rule-based allow/block logic.  

## 📘 Overview

This firewall implementation combines:  
- **Packet capture** from network interface(s) using a packet-capture module.  
- **Rate limiting** by source IP (to mitigate flooding / DDoS-like behavior).  
- **Intrusion Detection System (IDS)** checking each packet for suspicious content.  
- A **rule engine** to ALLOW or BLOCK packets based on configurable rules.  
- **Logging** of all firewall decision events (allow/block/alerts) with timestamps.  

The project structure is modular, making it easy to extend or customize: packet capture, rate limiter, rule engine, IDS, and logger are separated into modules.

## ⚙️ Features

- Real-time packet capture and inspection  
- Rate limiting per source IP  
- Basic IDS for detecting suspicious/malicious packets  
- Rule-based packet filtering (allow/block)  
- Logging of all events with timestamps for auditing  

## 🧰 Requirements

- Python 3.x  
- Root / administrator privileges (required for raw packet capture)  
- Install any dependencies required by modules (e.g. `scapy`, or whichever library you use for packet capture)  

## 🚀 Installation & Running

1. Clone the repository:  
    ```bash
    git clone https://github.com/Sairaviteja6/basic_firewall_python.git
    cd basic_firewall_python
    ```  
2. Install dependencies (if any). For example:  
    ```bash
    pip install -r requirements.txt
    ```  
3. Run the firewall (likely with elevated privileges):  
    ```bash
    sudo python main.py
    ```  
4. Monitor console output — packets will be printed as ALLOW, BLOCK, or ALERT along with source IPs. Logs will also be written (depending on your logger configuration).
 ---

## 📝 Configuration / Customization

- You can extend or customize modules like **rate limiter**, **IDS**, or **rule engine** as per your needs.  
- Adjust rate-limit thresholds, update IDS patterns, or define more sophisticated firewall rules to suit your environment.  

## 🧑‍💻 Contributing

Contributions are welcome! To contribute:  
1. Fork the repo  
2. Create a new feature/fix branch: `git checkout -b feature-mychange`  
3. Implement your changes, commit, and push to your fork.  
4. Open a Pull Request detailing your changes.  

If you extend the firewall (e.g. support IPv6, TCP/UDP ports filtering, logging enhancements, etc.), please include unit tests and update documentation accordingly.

## 📄 License

This project is provided as-is for educational and hobby purposes. Use responsibly.  
(Optional: Replace with an open-source license of your choice, e.g. MIT, GPL, etc.)

---

*Created by Sai Ravi Teja — feel free to reach out if you need help or want to collaborate.*  

## 🧪 How it Works (Flow)

