"""
Network Analysis Scripts for analyzing network data and generating insights.
"""

from config_local import MGMT_USERNAME, MGMT_SERVER

devices = [
    {"hostname": "core-sw01", "type": "Switch", "ip": "192.168.1.1",
     "location": "HQ-Floor1", "status": "up", "cpu": 42, "mem": 55,
     "uptime_days": 210, "backup_ok": True},
    {"hostname": "core-sw02", "type": "Switch", "ip": "192.168.1.2",
     "location": "HQ-Floor2", "status": "up", "cpu": 88, "mem": 76,
     "uptime_days": 45, "backup_ok": True},
    {"hostname": "edge-rtr01", "type": "Router", "ip": "192.168.2.1",
     "location": "HQ-DataCenter", "status": "up", "cpu": 35, "mem": 40,
     "uptime_days": 300, "backup_ok": False},
    {"hostname": "edge-rtr02", "type": "Router", "ip": "192.168.2.2",
     "location": "Branch-East", "status": "down", "cpu": 0, "mem": 0,
     "uptime_days": 0, "backup_ok": False},
    {"hostname": "fw-main", "type": "Firewall", "ip": "192.168.3.1",
     "location": "HQ-DataCenter", "status": "up", "cpu": 60, "mem": 82,
     "uptime_days": 120, "backup_ok": True},
    {"hostname": "fw-branch", "type": "Firewall", "ip": "192.168.3.2",
     "location": "Branch-West", "status": "up", "cpu": 15, "mem": 30,
     "uptime_days": 5, "backup_ok": True},
    {"hostname": "ap-lobby01", "type": "Access Point", "ip": "192.168.4.1",
     "location": "HQ-Floor1", "status": "up", "cpu": 20, "mem": 25,
     "uptime_days": 400, "backup_ok": True},
    {"hostname": "ap-lobby02", "type": "Access Point", "ip": "192.168.4.2",
     "location": "Branch-East", "status": "degraded", "cpu": 91, "mem": 95,
     "uptime_days": 2, "backup_ok": False},
]

def needs_attention(device):
    """
    Determines if a device needs attention based on its status, CPU, memory, and backup status.
    """
    if device["status"] != "up":
        return True
    if device["cpu"] > 85 or device["mem"] > 90:
        return True
    if not device["backup_ok"]:
        return True
    if device["uptime_days"] < 3:
        return True
    return False