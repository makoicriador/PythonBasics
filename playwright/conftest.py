import pytest

@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args):
    return {
        **browser_type_launch_args,
        "executable_path": "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe",
        "headless": True,
        # 1. Add the Chromium argument to maximize the window
        "args": ["--start-maximized"]
    }

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        # 2. Prevent Playwright from overriding the maximized window with its default 800x600 viewport
        "no_viewport": True
    }

#random