import pytest
from playwright.sync_api import Playwright, sync_playwright, expect

def test_check_box(page):
    page.goto('https://demoqa.com/elements')
    page.get_by_text('Check Box').click()

    # Expand all
    locator = page.locator(
        "path[d='M19 3H5c-1.11 0-2 .9-2 2v14c0 1.1.89 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm-2 10h-4v4h-2v-4H7v-2h4V7h2v4h4v2z']")
    locator.click()

    # Checking all checkboxes
    page.check('label[for="tree-node-home"]')
    page.uncheck('label[for="tree-node-home"]')
    page.check('label[for="tree-node-downloads"]')
    page.check('label[for="tree-node-office"]')
    page.check('label[for="tree-node-workspace"]')
    page.check('label[for="tree-node-documents"]')
    page.check('label[for="tree-node-desktop"]')
    page.uncheck('label[for="tree-node-home"]')
    # page.get_by_label('tree-node-home').click()

    # Collapse all
    locator = page.locator(
        "path[d='M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm-2 10H7v-2h10v2z']")
    locator.click()

    # time.sleep(2)

