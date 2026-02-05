import os

print("Checking server health...\n")

# CPU Load
cpu = os.popen("top -bn1 | grep load | awk '{printf \"CPU Load: %.2f\", $(NF-2)}'").read()
print(cpu)

# Disk Usage
disk = os.popen("df -h / | awk 'NR==2{print \"Disk Used: \"$5}'").read()
print(disk)

# Memory
memory = os.popen("free -m | awk 'NR==2{print \"Memory Used: \"$3\"MB / \"$2\"MB\"}\"'").read()
print(memory)

print("\n✅ Monitoring Completed")


