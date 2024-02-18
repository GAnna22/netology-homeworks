from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


def wait_element(browser, delay_seconds=1, by=By.TAG_NAME, value=None):
    return WebDriverWait(browser, delay_seconds).until(
        expected_conditions.presence_of_element_located((by, value))
    )


path = ChromeDriverManager().install()
browser_service = Service(executable_path=path)
browser = Chrome(service=browser_service)


browser.get("https://spb.hh.ru/search/vacancy?text=python&area=1&area=2/")

parsed_data = []

vacancies_list_tag = wait_element(browser, 1, By.ID,
                                  "a11y-main-content")
for article_tag in vacancies_list_tag.find_elements(By.CLASS_NAME,
                                                        "serp-item serp-item_link serp-item-redesign"):
    h3_tag = wait_element(article_tag, 1, By.TAG_NAME, "h3")
    a_tag = h3_tag.find_element(By.TAG_NAME, "a")
    vacancy_name_tag = article_tag.find_element(By.TAG_NAME, "span")

    vacancy_name = vacancy_name_tag.text
    link = a_tag.get_attribute("href")
    print('vacancy_name:', vacancy_name)
    print('link:', link)

    parsed_data.append(
        {
            "vacancy_name": vacancy_name,
            "link": link,
            "salary": "",
            "company_name": "",
            "city": ""
        }
    )

# for parsed_article in parsed_data:
#     browser.get(parsed_article["link"])
#     article_tag = wait_element(browser, 1, By.ID, "post-content-body")
#     article_text = article_tag.text
#     parsed_article["text"] = article_text[:100]
