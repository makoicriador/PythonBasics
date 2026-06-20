import time
from playwright.sync_api import Page, expect

def test_UIValidationDynamicScript(page:Page):
    #iphone X, Nokia Edge -> verify 2 items are showing in cart
    page.goto("https://rahulshettyacademy.com/loginpagePractise")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("Learning@830$3mK2")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("link", name="terms and conditions").click()
    page.get_by_role("button", name="Sign In").click()
    iphoneproduct = page.locator("app-card").filter(has_text="iphone X")
    iphoneproduct.get_by_role("button").click()
    nokiaproduct = page.locator("app-card").filter(has_text="Nokia Edge")
    nokiaproduct.get_by_role("button").click()
    time.sleep(3)
    page.get_by_text("Checkout").click()
    expect(page.locator(".media-body")).to_have_count(2)
    time.sleep(5)

def test_childWindowHandle(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise")
    with page.expect_popup() as newPage_info:
        page.locator(".blinkingText").filter(has_text="Free Access").click()
        child_page = newPage_info.value
        text = child_page.locator(".red").text_content()
        #print(text)
        left_words = text.split("at ")
        email = left_words[1].split(" ")[0]
        assert email == "mentor@rahulshettyacademy.com"
        time.sleep(5)

#random