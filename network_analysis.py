# Network Analysis Scripts for analyzing network data and generating insights.

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
    # Determines if a device needs attention based on its status, CPU, memory, and backup status.
    reasons = []
    if device["status"] != "up":
        reasons.append(f"status is '{device['status']}'")
    if device["cpu"] > 85:
        reasons.append("high CPU")
    if device["mem"] > 90:
        reasons.append("high memory")
    if not device["backup_ok"]:
        reasons.append("backup failed")
    if device["uptime_days"] < 3:
        reasons.append("low uptime")
    return reasons

def print_report():
    print("NETWORK DEVICE HEALTH REPORT")
    print(f"Management server: {MGMT_SERVER}  (checked in as {MGMT_USERNAME})")

    type_totals = {}
    location_totals = {}
    flagged = []

    for d in devices:
        type_totals[d["type"]] = type_totals.get(d["type"], 0) + 1
        location_totals[d["location"]] = location_totals.get(d["location"], 0) + 1

        print(f"\nHost: {d['hostname']} ({d['type']})")
        print(f"  IP: {d['ip']} | Location: {d['location']} | Status: {d['status']}")
        print(f"  CPU: {d['cpu']}% | Memory: {d['mem']}% | Uptime: {d['uptime_days']}d")
        print(f"  Backup OK: {d['backup_ok']}")

        reasons = needs_attention(d)
        if reasons:
            flagged.append((d["hostname"], reasons))
            print(f"  >>> FLAGGED: {', '.join(reasons)}")

    # Final Print
    print("\n" + "-" * 60)
    print("TOTALS BY DEVICE TYPE")
    for t, count in type_totals.items():
        print(f"  {t}: {count}")

    print("\nTOTALS BY LOCATION")
    for loc, count in location_totals.items():
        print(f"  {loc}: {count}")

    print("\n" + "-" * 60)
    print(f"DEVICES NEEDING ATTENTION: {len(flagged)} of {len(devices)}")
    for hostname, reasons in flagged:
        print(f"  - {hostname}: {', '.join(reasons)}")
    print("=" * 60)


if __name__ == "__main__":
    print_report()