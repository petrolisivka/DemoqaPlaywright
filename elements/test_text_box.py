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
    page.get_by_placeholder("Full Name").fill(fullName)
    page.get_by_placeholder("name@example.com").fill(generatedEmail)
    page.get_by_placeholder("Current Address").fill(currentAddress)
    page.locator("#permanentAddress").fill(permanentAddress)
    page.get_by_role('button', name='Submit').click()
    # page.wait_for_selector("text=New_user", timeout=5000)
    assert page.get_by_text(f"Name:{fullName}").is_visible(),"Name not found"
    assert page.get_by_text(f"Email:{generatedEmail}").is_visible(), "Email not found"
    assert page.get_by_text(f"Current Address :{currentAddress}").is_visible(), "Current address not found"
    assert page.get_by_text(f"Permananet Address :{permanentAddress}").is_visible(), "Permanent address not found"



