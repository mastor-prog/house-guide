from playwright.sync_api import sync_playwright

def take_screenshots():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        # Mobile viewport (iPhone SE)
        context = browser.new_context(viewport={'width': 375, 'height': 667})
        page = context.new_page()
        page.goto('file:///d:/Antivigravity/House_guide_v01/index.html')
        
        # Wait for images to load
        page.wait_for_load_state('networkidle')
        
        # Take full page screenshot
        page.screenshot(path='d:/Antivigravity/House_guide_v01/mobile_screenshot.png', full_page=True)
        browser.close()

take_screenshots()
