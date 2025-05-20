#!/usr/bin/env python3

import re

# Regex capturing correct email formats
email = '''
Please contact me at faith@gmail.com for more information.
You can also reach me at f.irakoze2@@company.co.uk or faith-irakoze@alu.edu.'''
email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
email_matches = re.findall(email_pattern, email)
print(f"Emails:{email_matches}")

# Regular expression extracting valid URLs
urls = '''
You can also check:
- http://example.org/about-me
- https://subdomain.company.co.uk
- http:/mywebsite.com
- htp://mywebsite.com'''
urls_pattern = r'https?:\/\/[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(?:\/\S*)?'
url_matches = re.findall(urls_pattern, urls)
print(f"URLs: {url_matches}")

# Regular expression capturing valid phone numbers
phone_number = '''
For support, call us me:
- (123) 456-7890
- 123-456-7890
- 123.456.7890
- 1234567890'''
phone_pattern = r'(?:\(?\d{3}\)?)[\s\-\.]\d{3}[\s\-\.]\d{4}'
phone_matches = re.findall(phone_pattern, phone_number)
print(f"Phone numbers: {phone_matches}")

# Regular expression capturing valid credit card numbers
credit_card = '''
Here are some of my credit card numbers:
1234 5678 9012 3456
1234-5678-9012-3456
1234-5678-9012-345'''
creditcard_pattern = r'[0-9]{4}[\s\-][0-9]{4}[\s\-][0-9]{4}[\s\-][0-9]{4}'
creditcard_matches = re.findall(creditcard_pattern, credit_card)
print(f"Credit card numbers: {creditcard_matches}")

# Regular expression capturing valid time formats
time = '''
I usually go to school at 9:30 AM and have lunch break at 12:45 PM.
I leave school at 13:75 or 19:45 and sleep at 23:59 or 24:01'''
time_pattern = r'\b(?:[0-1]?\d|2[0-3]):[0-5]\d(?:\s?(?:AM|PM))?\b'
time_matches = re.findall(time_pattern, time)
print(f"Time: {time_matches}")
