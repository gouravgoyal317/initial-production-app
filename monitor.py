import os

container_name = "cloud-app"

# Check if container running
status = os.popen(f"docker ps --filter name={container_name} --format '{{{{.Names}}}}'").read()

if container_name in status:
    print("✅ Container is running")
else:
    print("⚠️ Container stopped! Restarting...")
    os.system(f"docker start {container_name}")

