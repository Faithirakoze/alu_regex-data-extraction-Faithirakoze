import re

#Regex capturing correct email formats
email = '''
Please contact me at faith@gmail.com for more information.
You can also reach me at f.irakoze2@@company.co.uk or faith-irakoze@alu.edu.'''
email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
email_matches = re.findall(email_pattern, email)
print(f"Emails:{email_matches}")

#Regular expression extracting valid URLs
urls = '''
You can also check:
- http://example.org/about-me
- https://subdomain.company.co.uk
- http:/mywebsite.com
- htp://mywebsite.com'''
urls_pattern = r'https?:\/\/[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(?:\/\S*)?'
url_matches = re.findall(urls_pattern, urls)
print(f"URLs: {url_matches}")

#Regular expression capturing valid phone numbers
phone_number = '''
For support, call us me:
- (123) 456-7890
- 123-456-7890
- 123.456.7890
- 1234567890'''
phone_pattern = r'(?:\(?\d{3}\)?)[\s\-\.]\d{3}[\s\-\.]\d{4}'
phone_matches = re.findall(phone_pattern, phone_number)
print(f"Phone numbers: {phone_matches}")