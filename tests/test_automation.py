import pytest
from automation.automation import find_phone_nums, find_emails, format_phone_nums


def test_find_format_phone_nums(sample_data):
    phone_nums = find_phone_nums(sample_data)
    format_phone_nums(phone_nums)
    phone_nums.sort()
    assert phone_nums == ['123-456-7890', '206-355-8576']


def test_find_emails(sample_data):
    emails = find_emails(sample_data)
    emails.sort()
    assert emails == ['abe_lincoln@gettysburg.mil', 'joe@email.com']


@pytest.fixture
def sample_data():
    return """joe@email.com I've got a lovely bunch of coconuts ade355-8576dfs
Four score and Seven Years Ago abe_lincoln@gettysburg.mil (123)456-7890 12-43-08
george_washingbeard@conccond .net"""
