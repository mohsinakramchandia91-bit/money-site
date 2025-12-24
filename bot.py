import requests
import random
import time

# High CPM Countries IPs (Fake Headers Jugar)
high_cpm_ips = ["1.1.1.1", "2.2.2.2", "44.55.66.77"] # USA, UK, Germany list

# Mobile User Agents
devices = [
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 14; SM-S928B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36"
]

def send_signal(url):
    headers = {
        'User-Agent': random.choice(devices),
        'X-Forwarded-For': random.choice(high_cpm_ips), # Real USA/UK Identity Hack
        'Referer': 'https://www.google.com/'
    }
    try:
        response = requests.get(url, headers=headers, timeout=10)
        print(f"Signal Sent! Status: {response.status_code}")
    except:
        print("Connection skipped...")

# 24/7 Loop
while True:
    target_links = ["https://f973a1.netlify.app", "YOUR_VERCEL_LINK"]
    for link in target_links:
        send_signal(link)
    time.sleep(random.randint(1, 5)) # Human-like delay
