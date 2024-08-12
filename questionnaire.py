from playwright.sync_api import Playwright, sync_playwright
from random import choice

# Page 1


def run(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto('https://forms.office.com/pages/responsepage.aspx?id=l4EKSYN7EE-JuYMYm-ODXgFIE8qLYohPtMzjXU0ggHZUREowSDY3V0QyUTNFQ1YxWE4xTjdBRkdKNy4u',timeout=50000)
    i = 0

    while i < 50:
        # Page 1 Variables
        gender = choice(['Woman','Man',"Non-binary","Prefer not to say"])
        age = choice(["18-24","25-34","35-44","45-54"])
        marital_status = choice(["Single","Married","Widowed","Divorced","Separated"])
        highest_level_of_education = choice(["High school","Undergraduate","Postgraduate"])

        # Page 2 Variables
        ai_enabled = choice(["Rarely (1-2 times)","Occasionally (3-5 times)","Frequently (more than 5 times)"]) #5
        accuracy = choice(["Very Inaccurate","Inaccurate","Neutral","Accurate","Very Accurate"]) #6
        quickly = choice(["Very Quickly","Quickly","Neutral","Slow","Very Slow"]) #7
        effective = choice(["Very effective","Effective","Neutral","Ineffective","Very Ineffective"]) #8 
        often = choice(["Never","Rarely","Sometimes","Often","Always"]) #9
        clarity = choice(["Very Unclear","Unclear","Neutral","Clear","Very Clear"]) #10
        effective1 = choice(["Very effective","Effective","Neutral","Ineffective","Very ineffective"]) #11
        consistent = choice(["Very Consistent","Consistent","Neutral","Inconsistent","Very Inconsistent"]) #12

        # Page 3 Variables
        satisfaction = choice(["Very dissatisfied","Dissatisfied","Neutral","Satisfied","Very satisfied"]) #13-17,21
        agree = choice(["Strongly agree","agree","Neutral","Disagree","Strongly Disagree"]) #18-19
        unlikely = choice(["Very unlikely","Unlikely","Neutral","likely","Very likely"]) #20,23

        # Page 4 Variables
        comfort = choice(["Very comfortable","comfortable","Neutral","uncomfortable","Very uncomfortable"]) #22
        unlikely = choice(["Very unlikely","Unlikely","Neutral","likely","Very likely"]) #23
        insecure = choice(["Very Insecure","Insecure","Neutral","Secure","Very Secure"]) #24
        inconsistent = choice(["Very Inconsistent","Inconsistent","Neutral","Consistent","Very Consistent"]) #25
        good = choice(["Excellent","Good","Fair","Poor","Don't know"]) #26
        value1 = choice(["1","2","4"])
        value2 = choice(["1","2","4"])
        value3 = choice(["1","2","4"])
        value4 = choice(["1","2","4"])
        

        # Page 1
        page.wait_for_selector(f"//input[@value='{gender}']").click() #1
        page.wait_for_selector(f"//input[@value='{age}']").click() #2
        page.wait_for_selector(f"//input[@value='{marital_status}']").click() #3
        page.wait_for_selector(f"//input[@value='{highest_level_of_education}']").click() #4
        page.wait_for_selector(f"//button[text()='Next']").click()

        # Page 2
        page.get_by_role("radio", name=f"{ai_enabled}").check() #5
        
        # Page continuation 2
        page.locator("//div[@aria-labelledby='QuestionId_r6f1ff28fea1549dc8624fda38401b814 QuestionInfo_r6f1ff28fea1549dc8624fda38401b814']").get_by_text(accuracy, exact=True).click() #6
        page.locator("//div[@aria-labelledby='QuestionId_r4142c500335c4c648a7f69b55a74a1bb QuestionInfo_r4142c500335c4c648a7f69b55a74a1bb']").get_by_text(quickly, exact=True).click()#7
        page.locator("//div[@aria-labelledby='QuestionId_rd4a48d97fc8749ac826d68afd5a341fd QuestionInfo_rd4a48d97fc8749ac826d68afd5a341fd']").get_by_text(effective, exact=True).click()#8
        page.locator("//div[@aria-labelledby='QuestionId_rb1f639ffaf49421e956e06144545fb42 QuestionInfo_rb1f639ffaf49421e956e06144545fb42']").get_by_text(often, exact=True).click()#9
        page.locator("//div[@aria-labelledby='QuestionId_rf7c2c89ca407480d89fef34fdd5084ff QuestionInfo_rf7c2c89ca407480d89fef34fdd5084ff']").get_by_text(clarity, exact=True).click()#10
        page.locator("//div[@aria-labelledby='QuestionId_r4d84ae9ea46c4a9180e5563b8bd77685 QuestionInfo_r4d84ae9ea46c4a9180e5563b8bd77685']").get_by_text(effective1, exact=True).click()#11
        page.locator("//div[@aria-labelledby='QuestionId_r2ced4fcb99d0457387f25eca203cb2a5 QuestionInfo_r2ced4fcb99d0457387f25eca203cb2a5']").get_by_text(consistent, exact=True).click()#12
        page.wait_for_selector(f"//button[text()='Next']").click()
        

        # Page 3
        page.locator("//div[@aria-labelledby='QuestionId_r95f5c689ea5641b88f1752fa5d0c76de QuestionInfo_r95f5c689ea5641b88f1752fa5d0c76de']").get_by_text(satisfaction, exact=True).click() #13
        page.locator("//div[@aria-labelledby='QuestionId_re6641a791a4844138e06ad4740fa7fd1 QuestionInfo_re6641a791a4844138e06ad4740fa7fd1']").get_by_text(satisfaction, exact=True).click() #14
        page.locator("//div[@aria-labelledby='QuestionId_rf9203566b87e4aada4ec06128a03a3e6 QuestionInfo_rf9203566b87e4aada4ec06128a03a3e6']").get_by_text(satisfaction, exact=True).click() #15
        page.locator("//div[@aria-labelledby='QuestionId_r25fcca9d875841fcafa315af502132d4 QuestionInfo_r25fcca9d875841fcafa315af502132d4']").get_by_text(satisfaction, exact=True).click() #16
        page.locator("//div[@aria-labelledby='QuestionId_rb0498fbe40ad425d99d716a038c26191 QuestionInfo_rb0498fbe40ad425d99d716a038c26191']").get_by_text(satisfaction, exact=True).click() #17
        page.locator("//div[@aria-labelledby='QuestionId_r93bb223ad1b14230828b663f72eac077 QuestionInfo_r93bb223ad1b14230828b663f72eac077']").get_by_text(agree, exact=True).click() #18
        page.locator("//div[@aria-labelledby='QuestionId_re4d4ac0e0ccf40d99ace7250df31c6db QuestionInfo_re4d4ac0e0ccf40d99ace7250df31c6db']").get_by_text(agree, exact=True).click() #19
        page.locator("//div[@aria-labelledby='QuestionId_r0a3c156e4a174ce78b36414f2dc9b461 QuestionInfo_r0a3c156e4a174ce78b36414f2dc9b461']").get_by_text(unlikely, exact=True).click() #20
        page.locator("//div[@aria-labelledby='QuestionId_re2b34c83665b46f3afb80c860228b781 QuestionInfo_re2b34c83665b46f3afb80c860228b781']").get_by_text(satisfaction, exact=True).click() #21
        page.wait_for_selector(f"//button[text()='Next']").click()


        # Page 4
        page.locator("//div[@aria-labelledby='QuestionId_re62e4e6e00b5465998c9c331d5f0d795 QuestionInfo_re62e4e6e00b5465998c9c331d5f0d795']").get_by_text(comfort, exact=True).click() #22
        page.locator("//div[@aria-labelledby='QuestionId_r0cbf6aa287184e4096d63c943ea92695 QuestionInfo_r0cbf6aa287184e4096d63c943ea92695']").get_by_text(unlikely, exact=True).click() #23
        page.locator("//div[@aria-labelledby='QuestionId_r1f4b303de8f94f7bb8f6f5fb8d016b51 QuestionInfo_r1f4b303de8f94f7bb8f6f5fb8d016b51']").get_by_text(insecure, exact=True).click() #24
        page.locator("//div[@aria-labelledby='QuestionId_re439403d548e4f49bb2284440e40d799 QuestionInfo_re439403d548e4f49bb2284440e40d799']").get_by_text(inconsistent, exact=True).click() #25
        page.locator("//div[@aria-labelledby='QuestionId_rf662e6be9bda4c648eedb7cf096c0a58 QuestionInfo_rf662e6be9bda4c648eedb7cf096c0a58']").get_by_text(good, exact=True).click() #26
        # 27
        page.locator("//tr[@aria-labelledby='LikertId_r42fa8f543b2d4dcdb133c29a7741b1b2']").locator(f"//input[@value='{value1}']").click()
        page.locator("//tr[@aria-labelledby='LikertId_r9e9a2d4dbffd48dba8d14c11d374400e']").locator(f"//input[@value='{value2}']").click()
        page.locator("//tr[@aria-labelledby='LikertId_rc06461a1534a4c37b6f3ee48d7ebdd84']").locator(f"//input[@value='{value3}']").click()
        page.locator("//tr[@aria-labelledby='LikertId_r5c595fb978214e99a6f072000696d133']").locator(f"//input[@value='{value4}']").click()

        page.get_by_role("button", name="Submit").click()
        page.get_by_text("Submit another response").click()
        page.wait_for_timeout(3000)
        i += 1
        print(i)
        continue

    page.wait_for_timeout(3000)
    page.close()
    browser.close()       
        

            
    


with sync_playwright() as p:
    run(p)