import re

email = '''
Please contact me at faith@gmail.com for more information.
You can also reach me at f.irakoze2@@company.co.uk or faith-irakoze@alu.edu.'''
email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
email_matches = re.findall(email_pattern, email)
print(f"Emails:{email_matches}")

