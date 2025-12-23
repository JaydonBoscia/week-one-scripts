import os
import platform
import socket
import subprocess
from datetime import datetime

def get_hostname_info():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return hostname, ip_address

def get_network_interfaces():
    if os.name == "nt":
        return subprocess.getoutput("ipconfig /all")
    else:
        return subprocess.getoutput("ifconfig -a")

def test_connectivity():
    target = "8.8.8.8"
    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = ["ping", param, "4", target]
    return subprocess.getoutput(" ".join(command))

def write_report(content):
    filename = f"network_audit_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(filename, "w") as f:
        f.write(content)

if __name__ == "__main__":
    hostname, ip = get_hostname_info()
    interfaces = get_network_interfaces()
    ping_results = test_connectivity()

    report = (
        f"Hostname: {hostname}\n"
        f"IP Address: {ip}\n\n"
        f"=== Network Interfaces ===\n{interfaces}\n\n"
        f"=== Connectivity Test (Ping 8.8.8.8) ===\n{ping_results}\n"
    )

    write_report(report)
    print("Network audit completed. Report generated.")
