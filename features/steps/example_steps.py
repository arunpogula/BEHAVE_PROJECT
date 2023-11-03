# --FILE: features/steps/example_steps.py
from behave import given, then, when
from selenium import webdriver


@given("I open the Google homepage")
def step_open_google(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.google.com")

@when(" I search for '{search_term}'")
def step_check_title(context, search_term):
    search_box = context.driver.find_element("name", "q")
    search_box.send_keys(search_term)
    search_box.submit()

@then('I should search the results')
def step_then_search_results(context):
    assert 'Google Search' in context.driver.title
    assert 'Behave and Selenium' in context.driver.page_source 


