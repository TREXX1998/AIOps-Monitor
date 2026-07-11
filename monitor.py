import random

cpu = random.randint(10, 95)

print(f"CPU Usage: {cpu}%")

if cpu > 80:
    print("WARNING: High CPU Usage")
else:
    print("Server Healthy")