#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Simple Honeypot Server
A beginner-friendly honeypot that logs login attempts to files.
"""

import http.server
import socketserver
import socket
import json
import os
import datetime
import urllib.parse
import sys
from pathlib import Path

# Fix Windows console encoding issues
if sys.platform.startswith('win'):
    import codecs
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')

# Configuration
PORT = 8080
LOG_DIR = "logs"
LOG_FILE = "honeypot_attempts.log"
JSON_LOG_FILE = "honeypot_attempts.json"

class HoneypotHandler(http.server.SimpleHTTPRequestHandler):
    """Custom handler for our honeypot server"""
    
    def __init__(self, *args, **kwargs):
        # Ensure log directory exists
        os.makedirs(LOG_DIR, exist_ok=True)
        super().__init__(*args, **kwargs)
    
    def do_POST(self):
        """Handle POST requests (login attempts)"""
        if self.path == '/log-attempt':
            self.handle_login_attempt()
        else:
            self.send_error(404)
    
    def handle_login_attempt(self):
        """Process and log a login attempt"""
        try:
            # Get the request data
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            
            # Parse JSON data
            attempt_data = json.loads(post_data.decode('utf-8'))
            
            # Add server-side information
            attempt_data['client_ip'] = self.client_address[0]
            attempt_data['server_timestamp'] = datetime.datetime.now().isoformat()
            attempt_data['headers'] = dict(self.headers)
            
            # Log the attempt
            self.log_attempt(attempt_data)
            
            # Send response
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            
            response = {'status': 'logged', 'message': 'Attempt recorded'}
            self.wfile.write(json.dumps(response).encode())
            
        except Exception as e:
            print(f"Error handling login attempt: {e}")
            self.send_error(500)
    
    def log_attempt(self, data):
        """Log the attempt to both text and JSON files"""
        
        # Log to human-readable text file
        log_path = os.path.join(LOG_DIR, LOG_FILE)
        with open(log_path, 'a', encoding='utf-8') as f:
            f.write(f"\n{'='*60}\n")
            f.write(f"🍯 HONEYPOT CAPTURE - {data['server_timestamp']}\n")
            f.write(f"{'='*60}\n")
            f.write(f"Username: {data.get('username', 'N/A')}\n")
            f.write(f"Password: {data.get('password', 'N/A')}\n")
            f.write(f"Client IP: {data.get('client_ip', 'N/A')}\n")
            f.write(f"User Agent: {data.get('userAgent', 'N/A')}\n")
            f.write(f"Platform: {data.get('platform', 'N/A')}\n")
            f.write(f"Language: {data.get('language', 'N/A')}\n")
            f.write(f"Referrer: {data.get('referrer', 'N/A')}\n")
            f.write(f"URL: {data.get('url', 'N/A')}\n")
            f.write(f"Timestamp: {data.get('timestamp', 'N/A')}\n")
        
        # Log to JSON file for easy parsing
        json_log_path = os.path.join(LOG_DIR, JSON_LOG_FILE)
        
        # Read existing logs
        logs = []
        if os.path.exists(json_log_path):
            try:
                with open(json_log_path, 'r', encoding='utf-8') as f:
                    logs = json.load(f)
            except:
                logs = []
        
        # Add new log
        logs.append(data)
        
        # Write back to file
        with open(json_log_path, 'w', encoding='utf-8') as f:
            json.dump(logs, f, indent=2, ensure_ascii=False)
        
        # Print to console for immediate feedback
        try:
            print(f"\n🍯 HONEYPOT CAPTURE!")
        except UnicodeEncodeError:
            print(f"\n[CAPTURE] HONEYPOT CAPTURE!")
        print(f"Time: {data['server_timestamp']}")
        print(f"IP: {data.get('client_ip', 'Unknown')}")
        print(f"Username: {data.get('username', 'N/A')}")
        print(f"Password: {data.get('password', 'N/A')}")
        print(f"User Agent: {data.get('userAgent', 'N/A')[:50]}...")
        print("-" * 50)
    
    def do_OPTIONS(self):
        """Handle CORS preflight requests"""
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
    
    def log_message(self, format, *args):
        """Override to reduce server log noise"""
        # Only log important messages
        if "POST /log-attempt" in format % args:
            return
        super().log_message(format, *args)

def find_available_port(start_port=8080, max_attempts=10):
    """Find an available port starting from start_port"""
    for port in range(start_port, start_port + max_attempts):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind(('', port))
                return port
        except OSError:
            continue
    return None

def main():
    """Start the honeypot server"""
    
    try:
        print("🍯 Simple Honeypot Server")
    except UnicodeEncodeError:
        print("[HONEYPOT] Simple Honeypot Server")
    
    print("=" * 40)
    
    # Find an available port
    available_port = find_available_port(PORT)
    if available_port is None:
        print(f"❌ Could not find an available port starting from {PORT}")
        print("Please stop other running servers or try again later.")
        return
    
    if available_port != PORT:
        print(f"⚠️  Port {PORT} is in use, using port {available_port} instead")
    
    print(f"Starting server on port {available_port}")
    print(f"Logs will be saved to: {LOG_DIR}/")
    print(f"Access the honeypot at: http://localhost:{available_port}")
    print("\nWARNING: EDUCATIONAL USE ONLY - Use responsibly!")
    print("=" * 40)
    
    # Change to the directory containing our HTML file
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    # Create the server with the available port
    with socketserver.TCPServer(("", available_port), HoneypotHandler) as httpd:
        try:
            try:
                print(f"\n🚀 Server running! Visit http://localhost:{available_port}")
            except UnicodeEncodeError:
                print(f"\n[RUNNING] Server running! Visit http://localhost:{available_port}")
            print("Press Ctrl+C to stop the server")
            httpd.serve_forever()
        except KeyboardInterrupt:
            try:
                print("\n\n🛑 Server stopped by user")
            except UnicodeEncodeError:
                print("\n\n[STOPPED] Server stopped by user")
            print("Check the logs/ directory for captured data!")

if __name__ == "__main__":
    main()