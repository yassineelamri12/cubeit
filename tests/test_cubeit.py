from playwright.sync_api import Page, expect

BASE_URL = "http://127.0.0.1:8000/"

def test_cube(page: Page):
    page.goto(BASE_URL)

    input = page.locator("//input[@id='numberInput']")
    input.fill("5")

    btn = page.locator("button")
    btn.click()

    result = page.locator("p#result")

    expect(result).to_contain_text("125")

def test_empty_input(page: Page):
    page.goto(BASE_URL)

    btn = page.locator("button")
    btn.click()

    result = page.locator("p#result")
    expect(result).to_contain_text("something")
