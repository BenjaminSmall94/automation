import re
import os


# https://stackoverflow.com/questions/25389095/python-get-path-of-root-project-structure
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

with open(f"{ROOT_DIR}/assets/potential-contacts.txt") as f:
    file_text = f.read()

phone_pattern = r"(?:(?:\d{3}-)?|(?:\(\d{3}\) ?))\d{3}-\d{4}"
phone_nums = re.findall(phone_pattern, file_text)

for i in range(len(phone_nums)):
    phone_nums[i] = phone_nums[i].replace("(", "")
    phone_nums[i] = phone_nums[i].replace(")", "-")
    if len(phone_nums[i]) == 8:
        phone_nums[i] = "206-" + phone_nums[i]

phone_nums.sort()

email_pattern = r"^\b\S*@\S*(?:\.com|\.org|\.net|\.gov|\.mil|\.edu)\b"
emails = re.findall(email_pattern, file_text)

emails.sort()
print(emails)

with open(f"{ROOT_DIR}/filtered-assets/phone_numbers.txt", "w") as f:
    for num in phone_nums:
        f.write(f"{num}\n")
