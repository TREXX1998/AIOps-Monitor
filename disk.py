import random

disk = random.randint(30, 95)

print(f"Disk Usage: {disk}%")

if disk > 85:
    print("CRITICAL: Disk Almost Full")