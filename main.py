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
