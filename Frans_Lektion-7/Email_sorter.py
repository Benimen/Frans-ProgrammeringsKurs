import re

# Opens users.txt and reads its content
with open("users.txt", "r") as file:
    text = file.read()


# Capture email addresses
email_pattern = r"[a-zA-Z0-9]+@[a-zA-Z.-]+\.[a-zA-Z]{2,}"

gmail_pattern = r"[a-zA-Z0-9]+@[gmail.-]+\.[a-zA-Z]{2,}"

yahoo_pattern = r"[a-zA-Z0-9]+@[yahoo.-]+\.[a-zA-Z]{2,}"

outlook_pattern = r"[a-zA-Z0-9]+@[outlook.-]+\.[a-zA-Z]{2,}"

example_pattern = r"[a-zA-Z0-9]+@[example.-]+\.[a-zA-Z]{2,}"


# Finds all email addresses in the text and saves it to new variable
gmail_emails = re.findall(gmail_pattern, text)
yahoo_emails = re.findall(yahoo_pattern, text)
outlook_emails = re.findall(outlook_pattern, text)
example_emails = re.findall(example_pattern, text)

# Concatenate lists to a single variable
emails = gmail_emails + yahoo_emails + outlook_emails + example_emails

# Prints all emails
for email_list in emails:
    print(email_list)

# Creates a file named emails.txt
with open("emails.txt", "w") as email_filtered:
    email_filtered.write("\n".join(emails))
