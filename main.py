from playwright.sync_api import sync_playwright

def main():

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()


        page.goto('https://www.google.com/')

        print(f"Successfully Loaded: {page.title()}")
        page.wait_for_timeout(10000)
        browser.close()
        
if __name__ == "__main__":
    main()
