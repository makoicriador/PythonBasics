import time
from playwright.sync_api import Page, expect


def test_UIChecks(page:Page):
    #hide / display placeholders
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()
    page.get_by_role("button", name = "Hide").click()
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_hidden()
    #time.sleep(2)

    #alertBoxes
    page.on("dialog", lambda dialog:dialog.accept())
    #time.sleep(2)
    page.get_by_role("button", name = "Confirm").click()
    #time.sleep(2)

    #FrameHandling
    pageFrame = page.frame_locator("#courses-iframe")
    pageFrame.get_by_role("link", name = "Courses", exact = True).click()
    #time.sleep(2)
    (expect(pageFrame.locator("body")).to_contain_text("Selenium Python Automation Testing"))

