cat > conftest.py <<'EOF'
"""Fixtures compartilhadas do pytest: ciclo de vida do WebDriver."""
import os
import shutil

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

BASE_URL = os.getenv("BASE_URL", "https://www.saucedemo.com")


def _find_browser():
    """Localiza o binário do Chrome/Chromium (CHROME_BIN sobrescreve)."""
    candidates = (
        os.getenv("CHROME_BIN"),
        "chromium", "chromium-browser",
        "google-chrome", "google-chrome-stable",
    )
    for name in candidates:
        if name and shutil.which(name):
            return shutil.which(name)
    return None


@pytest.fixture
def driver():
    options = Options()
    if os.getenv("HEADLESS", "0") == "1":
        options.add_argument("--headless=new")
    options.add_argument("--window-size=1280,800")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    browser = _find_browser()
    if browser:
        options.binary_location = browser

    drv = webdriver.Chrome(options=options)
    drv.implicitly_wait(5)
    drv.get(BASE_URL)
    yield drv
    drv.quit()
EOF
