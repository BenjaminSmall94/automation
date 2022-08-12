import re
import os


# https://stackoverflow.com/questions/25389095/python-get-path-of-root-project-structure
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def read_file(relative_dir):
    with open(f"{ROOT_DIR}{relative_dir}") as f:
        return f.read()


def find_phone_nums(text):
    phone_pattern = r"(?:(?:\d{3}-)?|(?:\(\d{3}\) ?))\d{3}-\d{4}"
    return re.findall(phone_pattern, text)


def find_emails(text):
    email_pattern = r"\S*@\S*(?:\.com|\.org|\.net|\.gov|\.mil|\.edu)"
    return re.findall(email_pattern, text)


def write_file(contact_list, relative_dir):
    with open(f"{ROOT_DIR}{relative_dir}", "w") as f:
        for contact in contact_list:
            f.write(f"{contact}\n")


def format_phone_nums(nums):
    for i in range(len(nums)):
        nums[i] = nums[i].replace("(", "")
        nums[i] = nums[i].replace(")", "-")
        if len(nums[i]) == 8:
            nums[i] = "206-" + nums[i]

file_text = read_file("/assets/potential-contacts.txt")

phone_nums = find_phone_nums(file_text)
format_phone_nums(phone_nums)
phone_nums.sort()
write_file(phone_nums, "/filtered-assets/phone_numbers.txt")

emails = find_emails(file_text)
emails.sort()
write_file(emails, "/filtered-assets/emails.txt")
