# 🍯 Simple Honeypot - Beginner's Guide

A beginner-friendly honeypot system that demonstrates cybersecurity concepts through hands-on learning.

## 📚 What You'll Learn

- **How honeypots work** - Understanding deception-based security
- **Attack patterns** - See real login attempts and common passwords
- **Security monitoring** - Learn to analyze and respond to threats
- **Web security basics** - HTML, JavaScript, and server concepts

## 🎯 What This Honeypot Does

This honeypot creates a **fake admin login page** that:
- ✅ Looks like a real administrative portal
- ✅ Captures all login attempts (usernames, passwords, IP addresses)
- ✅ Always shows "Login Failed" to maintain deception
- ✅ Logs everything to files for analysis
- ✅ Provides detailed analytics of captured data

## 📁 Project Structure

```
simple-honeypot/
├── index.html              # The fake login page (the bait)
├── honeypot_server.py       # Python server that hosts and logs
├── view_logs.py            # Script to analyze captured data
├── logs/                   # Directory where captures are stored
│   ├── honeypot_attempts.log    # Human-readable log file
│   └── honeypot_attempts.json   # Machine-readable log file
└── README.md               # This file
```

## 🚀 Quick Start Guide

### Step 1: Start the Honeypot Server

```bash
# Navigate to the honeypot directory
cd simple-honeypot

# Start the server (requires Python 3)
python honeypot_server.py
```

You should see:
```
🍯 Simple Honeypot Server
========================================
Starting server on port 8080
Logs will be saved to: logs/
Access the honeypot at: http://localhost:8080

⚠️  EDUCATIONAL USE ONLY - Use responsibly!
========================================

🚀 Server running! Visit http://localhost:8080
Press Ctrl+C to stop the server
```

### Step 2: Visit the Honeypot

Open your web browser and go to: **http://localhost:8080**

You'll see a convincing admin login page that looks like this:

```
┌─────────────────────────────────┐
│     🏢 ADMIN PORTAL             │
│   Secure Administrative Access │
│                                 │
│  👤 Username: [____________]    │
│  🔒 Password: [____________]    │
│                                 │
│         [🔐 LOGIN]              │
│                                 │
│  ⚠️  WARNING: Authorized        │
│     Personnel Only              │
└─────────────────────────────────┘
```

### Step 3: Test the Honeypot

Try logging in with fake credentials like:
- Username: `admin`, Password: `password`
- Username: `administrator`, Password: `123456`
- Username: `root`, Password: `admin`

**Every attempt will "fail"** - this is the deception! But everything is being logged.

### Step 4: View Captured Data

In a new terminal window, run:

```bash
python view_logs.py
```

You'll see detailed analysis like:
```
🍯 Simple Honeypot Log Viewer
========================================
📊 HONEYPOT SUMMARY
==================================================
Total attempts: 5
Unique IP addresses: 1

🔤 Most common usernames:
  • admin: 3 attempts
  • administrator: 1 attempts
  • root: 1 attempts

🔐 Most common passwords:
  • password: 2 attempts
  • 123456: 1 attempts
  • admin: 1 attempts
```

## 🔍 Understanding the Components

### The Bait (index.html)
- **Professional design** makes it look like a real admin portal
- **Realistic behavior** with loading animations and error messages
- **Hidden logging** captures data without revealing it's a trap

### The Trap (honeypot_server.py)
- **Python web server** hosts the fake login page
- **Automatic logging** saves all attempts to files
- **Real-time feedback** shows captures in the terminal

### The Analysis (view_logs.py)
- **Summary statistics** show attack patterns
- **Detailed logs** reveal individual attempts
- **Pattern analysis** helps understand attacker behavior

## 📊 What the Logs Reveal

### Common Attack Patterns You'll See:

1. **Default Credentials**
   - admin/admin
   - admin/password
   - administrator/password

2. **Brute Force Attempts**
   - Multiple rapid attempts from same IP
   - Systematic password variations

3. **Reconnaissance**
   - Testing common usernames
   - Probing for system information

### Sample Log Entry:
```
🍯 HONEYPOT CAPTURE - 2025-08-01T09:15:23.456Z
============================================================
Username: admin
Password: password123
Client IP: 192.168.1.100
User Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)...
Platform: Win32
Language: en-US
Referrer: Direct access
URL: http://localhost:8080/
Timestamp: 2025-08-01T09:15:23.456Z
```

## 🛡️ Security & Ethics

### ✅ Safe Uses (Educational)
- **Learning cybersecurity concepts**
- **Understanding attack methods**
- **Testing on your own network**
- **Demonstrating security principles**

### ❌ Illegal Uses (Don't Do This!)
- **Deploying on networks you don't own**
- **Collecting real user credentials**
- **Using for malicious purposes**
- **Violating privacy laws**

### 🔒 Safety Features Built-In
- **Isolated system** - Can't be used to attack others
- **Local only** - Runs on your computer by default
- **No real data** - Doesn't store actual sensitive information
- **Educational focus** - Designed for learning, not harm

## 🎓 Learning Exercises

### Beginner Exercises:
1. **Run the honeypot** and try different login combinations
2. **Analyze the logs** to see what gets captured
3. **Modify the HTML** to make it look like a different service
4. **Change the port** in the Python server

### Intermediate Exercises:
1. **Add email logging** to get notified of attempts
2. **Create IP blocking** after multiple failed attempts
3. **Add geolocation** to see where attacks come from
4. **Build a web dashboard** to view logs in real-time

### Advanced Exercises:
1. **Deploy safely** on an isolated network segment
2. **Add multiple services** (SSH, FTP honeypots)
3. **Integrate with SIEM** systems for enterprise monitoring
4. **Create automated responses** to different attack types

## 🔧 Customization Options

### Change the Appearance:
Edit [`index.html`](index.html) to modify:
- Company name and branding
- Colors and styling
- Warning messages
- Form fields

### Modify Logging:
Edit [`honeypot_server.py`](honeypot_server.py) to:
- Change log file locations
- Add new data fields
- Modify server responses
- Change the port number

### Enhance Analysis:
Edit [`view_logs.py`](view_logs.py) to:
- Add new statistics
- Create charts and graphs
- Export data to other formats
- Set up automated alerts

## 🚨 Troubleshooting

### Common Issues:

**"Port already in use" error:**
```bash
# Try a different port
python honeypot_server.py --port 8081
```

**"Permission denied" error:**
```bash
# On Linux/Mac, you might need:
sudo python honeypot_server.py
```

**No logs appearing:**
- Check that the `logs/` directory exists
- Verify the server is running
- Try the login form in your browser

**Browser shows "This site can't be reached":**
- Confirm the server is running
- Check the URL: http://localhost:8080
- Try http://127.0.0.1:8080 instead

## 📖 Further Learning

### Recommended Reading:
- **"The Cuckoo's Egg" by Cliff Stoll** - Classic honeypot story
- **NIST Cybersecurity Framework** - Industry standards
- **OWASP Top 10** - Common web vulnerabilities

### Next Steps:
1. **Learn about real honeypot systems** (Cowrie, Dionaea, Honeyd)
2. **Study network security monitoring** (Wireshark, tcpdump)
3. **Explore SIEM systems** (Splunk, ELK Stack)
4. **Practice ethical hacking** (with proper authorization)

## 🤝 Contributing

This is an educational project! Feel free to:
- Add new features
- Improve the documentation
- Create additional honeypot types
- Share your learning experiences

## 📄 License

This project is for educational purposes only. Use responsibly and ethically!

---

**Remember: With great power comes great responsibility. Use this knowledge to defend, not attack!** 🛡️