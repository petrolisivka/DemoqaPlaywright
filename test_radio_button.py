import pytest
import time
from playwright.sync_api import Playwright, sync_playwright, expect

def test_radio_button(page):
    page.goto('https://demoqa.com/elements')
    page.get_by_text('Radio Button').click()

    # Click to the Yes radio button and verify this selection
    # page.locator('label.custom-control-label[for="yesRadio"]').click()
    page.check("#yesRadio", force=True)
    assert page.get_by_text('You have selected Yes').is_visible(), "Text 'Yes' not found"
    time.sleep(2)

    # Click to the Impressive radio button and verify this selection
    page.check('#impressiveRadio', force=True)
    assert page.get_by_text('You have selected Impressive').is_visible(), "Text 'Impressive' not found"
    time.sleep(2)
