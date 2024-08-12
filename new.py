import re
from playwright.sync_api import Playwright, sync_playwright, expect



def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False,slow_mo=1000)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://forms.office.com/pages/responsepage.aspx?id=l4EKSYN7EE-JuYMYm-ODXgFIE8qLYohPtMzjXU0ggHZUREowSDY3V0QyUTNFQ1YxWE4xTjdBRkdKNy4u",timeout=50000)

    # Page 1
    page.get_by_role("radio", name="Woman").check()
    page.get_by_role("radio", name="-24").check()
    page.get_by_role("radio", name="Widowed").check()
    page.get_by_role("radio", name="Postgraduate").check()
    page.get_by_label("Next").click()

    # Page 2
    page.get_by_role("radio", name="Occasionally (3-5 times)").check()

    page.get_by_role("radio", name="Very Inaccurate").check()
    page.get_by_label("7.How quickly did the AI-").get_by_role("radio", name="Neutral").check()
    print(page.get_by_label("7.How quickly did the AI-").get_by_role("radio", name="Neutral"))
    page.get_by_label("8.Rate the overall").get_by_role("radio", name="Neutral").check()
    page.get_by_role("radio", name="Sometimes").check()
    page.get_by_label("10.Rate the clarity of").get_by_role("radio", name="Neutral").check()
    page.get_by_label("11.How effective is the AI").get_by_role("radio", name="Neutral").check()
    page.get_by_label("12.How consistent were the").get_by_role("radio", name="Neutral").check()
    page.get_by_label("Next").click()

    # Page 3
    page.get_by_label("13.How satisfied are you with").get_by_role("radio", name="Neutral").check()
    page.get_by_label("14.How satisfied are you with").get_by_role("radio", name="Very dissatisfied").check()
    page.get_by_label("15.How satisfied are you with").get_by_role("radio", name="Neutral").check()
    page.get_by_label("16.How satisfied are you with").get_by_role("radio", name="Neutral").check()
    page.get_by_label("17.How satisfied are you with").get_by_role("radio", name="Very dissatisfied").check()
    page.get_by_label("18.Would you prefer using AI-").get_by_role("radio", name="Strongly Disagree").check()
    page.get_by_label("19.Did the AI-enabled chatbot").get_by_role("radio", name="Strongly Disagree").check()
    page.get_by_role("radio", name="Very unlikely").check()
    page.get_by_label("21.Rate your overall").get_by_role("radio", name="Very satisfied").check()
    page.get_by_label("Next").click()

    # Page 4
    page.get_by_role("radio", name="Very comfortable").check()
    page.get_by_role("radio", name="likely", exact=True).check()
    page.get_by_role("radio", name="Very Secure").check()
    page.get_by_role("radio", name="Very Inconsistent").check()
    page.get_by_role("radio", name="Excellent").check()
    page.get_by_label("Do you trust AI-enabled chatbots to handle your queries accurately? , Yes").check()
    page.get_by_label("Do you feel that AI-enabled chatbots improve the overall efficiency of customer service, Maybe").check()
    page.get_by_label("Do you believe AI-enabled chatbots provide a personalized customer service experience, No").check()
    page.get_by_role("cell", name="Do you find AI-enabled chatbots more convenient than traditional customer service methods?, Maybe").click()
    page.get_by_role("button", name="Submit").click()

    page.wait_for_timeout(3000)

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
