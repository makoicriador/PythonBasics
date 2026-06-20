import time

from playwright.sync_api import Page, expect


def test_playwrightBasics(playwright):
    brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"
    browser = playwright.chromium.launch(headless=False,executable_path=brave_path)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/")

def test_playwrightShortcut(page:Page):
    page.goto("https://rahulshettyacademy.com/")

def test_coreLocators(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("Learning@830$3mK1")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("link", name="terms and conditions").click()
    page.get_by_role("button",name="Sign In").click()
    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()
    #Incorrect username/password.
#random
