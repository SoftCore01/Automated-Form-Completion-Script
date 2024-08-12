from playwright.sync_api import Playwright, sync_playwright

def run(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://forms.office.com/pages/responsepage.aspx?id=l4EKSYN7EE-JuYMYm-ODXgFIE8qLYohPtMzjXU0ggHZUREowSDY3V0QyUTNFQ1YxWE4xTjdBRkdKNy4u",timeout=50000)

    page.get_by_role("radio", name="Woman").check()
    page.get_by_role("radio", name="-24").check()
    page.get_by_role("radio", name="Widowed").check()
    page.get_by_role("radio", name="Postgraduate").check()
    page.get_by_label("Next").click()

    page.get_by_role("radio", name="Occasionally (3-5 times)").check()
    
    text = page.locator("//div[@aria-labelledby='QuestionId_r6f1ff28fea1549dc8624fda38401b814 QuestionInfo_r6f1ff28fea1549dc8624fda38401b814']").get_by_text("Accurate", exact=True).click()
    print(text)
    page.wait_for_timeout(3000)
    page.close()
    browser.close()


with sync_playwright() as p:
    run(p)