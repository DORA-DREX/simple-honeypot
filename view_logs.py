#!/usr/bin/env python3
"""
Honeypot Log Viewer
A simple script to view and analyze captured honeypot data.
"""

import json
import os
from datetime import datetime
from collections import Counter

LOG_DIR = "logs"
JSON_LOG_FILE = "honeypot_attempts.json"
TEXT_LOG_FILE = "honeypot_attempts.log"

def load_logs():
    """Load logs from JSON file"""
    json_path = os.path.join(LOG_DIR, JSON_LOG_FILE)
    
    if not os.path.exists(json_path):
        print(f"❌ No log file found at {json_path}")
        print("Run the honeypot server first to generate logs!")
        return []
    
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"❌ Error reading logs: {e}")
        return []

def display_summary(logs):
    """Display a summary of captured attempts"""
    if not logs:
        print("📊 No attempts captured yet.")
        return
    
    print(f"📊 HONEYPOT SUMMARY")
    print("=" * 50)
    print(f"Total attempts: {len(logs)}")
    
    # Count unique IPs
    ips = [log.get('client_ip', 'Unknown') for log in logs]
    unique_ips = len(set(ips))
    print(f"Unique IP addresses: {unique_ips}")
    
    # Most common usernames
    usernames = [log.get('username', '') for log in logs if log.get('username')]
    if usernames:
        common_usernames = Counter(usernames).most_common(5)
        print(f"\n🔤 Most common usernames:")
        for username, count in common_usernames:
            print(f"  • {username}: {count} attempts")
    
    # Most common passwords
    passwords = [log.get('password', '') for log in logs if log.get('password')]
    if passwords:
        common_passwords = Counter(passwords).most_common(5)
        print(f"\n🔐 Most common passwords:")
        for password, count in common_passwords:
            print(f"  • {password}: {count} attempts")
    
    # Time range
    timestamps = [log.get('server_timestamp', '') for log in logs if log.get('server_timestamp')]
    if timestamps:
        timestamps.sort()
        first_attempt = timestamps[0]
        last_attempt = timestamps[-1]
        print(f"\n⏰ Time range:")
        print(f"  First attempt: {first_attempt}")
        print(f"  Last attempt: {last_attempt}")

def display_detailed_logs(logs, limit=10):
    """Display detailed log entries"""
    if not logs:
        return
    
    print(f"\n📋 DETAILED LOGS (showing last {min(limit, len(logs))} attempts)")
    print("=" * 70)
    
    # Show most recent attempts first
    recent_logs = logs[-limit:] if len(logs) > limit else logs
    recent_logs.reverse()
    
    for i, log in enumerate(recent_logs, 1):
        print(f"\n🍯 ATTEMPT #{len(logs) - i + 1}")
        print("-" * 30)
        print(f"Time: {log.get('server_timestamp', 'Unknown')}")
        print(f"IP: {log.get('client_ip', 'Unknown')}")
        print(f"Username: {log.get('username', 'N/A')}")
        print(f"Password: {log.get('password', 'N/A')}")
        print(f"User Agent: {log.get('userAgent', 'N/A')[:60]}...")
        print(f"Platform: {log.get('platform', 'N/A')}")
        print(f"Language: {log.get('language', 'N/A')}")

def analyze_patterns(logs):
    """Analyze attack patterns"""
    if not logs:
        return
    
    print(f"\n🔍 ATTACK PATTERN ANALYSIS")
    print("=" * 50)
    
    # Group by IP
    ip_attempts = {}
    for log in logs:
        ip = log.get('client_ip', 'Unknown')
        if ip not in ip_attempts:
            ip_attempts[ip] = []
        ip_attempts[ip].append(log)
    
    print(f"📍 Attempts by IP address:")
    for ip, attempts in sorted(ip_attempts.items(), key=lambda x: len(x[1]), reverse=True):
        print(f"  • {ip}: {len(attempts)} attempts")
        if len(attempts) > 1:
            usernames = [a.get('username', '') for a in attempts]
            unique_usernames = len(set(usernames))
            print(f"    - Tried {unique_usernames} different usernames")
    
    # Common attack combinations
    combinations = [(log.get('username', ''), log.get('password', '')) for log in logs]
    common_combos = Counter(combinations).most_common(5)
    
    print(f"\n🎯 Most common username/password combinations:")
    for (username, password), count in common_combos:
        if username and password:
            print(f"  • {username}/{password}: {count} attempts")

def main():
    """Main function"""
    print("🍯 Simple Honeypot Log Viewer")
    print("=" * 40)
    
    # Load logs
    logs = load_logs()
    
    if not logs:
        print("\n💡 To generate logs:")
        print("1. Run: python honeypot_server.py")
        print("2. Visit: http://localhost:8080")
        print("3. Try some fake login attempts")
        print("4. Run this script again to see results!")
        return
    
    # Display analysis
    display_summary(logs)
    display_detailed_logs(logs)
    analyze_patterns(logs)
    
    print(f"\n📁 Raw log files location:")
    print(f"  • JSON: {os.path.join(LOG_DIR, JSON_LOG_FILE)}")
    print(f"  • Text: {os.path.join(LOG_DIR, TEXT_LOG_FILE)}")
    
    print(f"\n🎓 What this teaches you:")
    print("  • How attackers try common username/password combinations")
    print("  • The importance of monitoring login attempts")
    print("  • How honeypots can reveal attack patterns")
    print("  • Real-world cybersecurity monitoring techniques")

if __name__ == "__main__":
    main()