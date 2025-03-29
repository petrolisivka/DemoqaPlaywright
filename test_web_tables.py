import pytest
from playwright.sync_api import Playwright, sync_playwright, expect
import time
from faker import Faker
# Prepare data to fill in the specified fields
fake = Faker(locale='en_US')
fullName = (fake.first_name() +" " + fake.last_name())
generatedEmail = (fake.email())
currentAddress = (fake.address())
permanentAddress = (fake.country() + ", " + fake.city() + ", " + fake.postcode())

def test_fill_text_boxes(page):
    page.goto("https://demoqa.com/elements")
    page.get_by_text("Text Box").click()