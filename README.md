ALU Regex Data Extraction - Faith Irakoze

In this project, I used Regular Expressions(Regex) to extract specific data types from text by using Python's built-in 're' module.

Project Overview

The program searches text inputs and extracts the following types of data:

1. Email addresses
2. URLs
3. Phone numbers
4. Credit card numbers
5. Time(both 12-hour and 24-hour formats)

It matches correct and valid formats and ignores invalid ones using regex patterns.

Languages used

1. Python 3
2. Regular expressions(re module)

Files

1. 'main.py': Contains all regex patterns with the sample text and printed results.
2. 'README.md': Contains the project's documentation.

In order to run the script:

- Clone the repository 'alu_regex-data-extraction-Faithirakoze' to your computer.

- Navigate to the folder of the project in your terminal by typing:
      'cd alu_regex-data-extraction-Faithirakoze'

- Run the script using:
      'python3 main.py'

Sample output

The program will display valid email addresses, URLs, phone numbers, credit card numbers, and time formats in the terminal like so:

- Emails: ['faith@gmail.com', 'faith-irakoze@alu.edu']
- URLs: ['http://example.org/about-me', 'https://subdomain.company.co.uk']
- Phone numbers: ['(123) 456-7890', '123-456-7890', '123.456.7890']
- Credit card numbers: ['1234 5678 9012 3456', '1234-5678-9012-3456']
- Time: ['9:30 AM', '12:45 PM', '19:45', '23:59']