from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
import time

WEBSITE_URL_BASE="https://onskeskyen.dk/da"
XPATH_COOKIE_ACCEPT_BUTTON="//button[contains(text(), 'Accepter alle')]"
XPATH_INSPIRATION_DROPDOWN="//button[contains(span, 'Inspiration')]"
XPATH_BORN_BABY_CATEGORY="//button[contains(span, 'Børn & Baby')]"
XPATH_PRODUCT_NAME_H2="//div[contains(@class, 'fade-in')]//div[contains(@class, 'BrandItem__CardContainer')]//h2[contains(translate(., 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'plysdyr')]"
XPATH_FIND_MORE_BUTTON="//button[contains(div, 'Indlæs flere')]"
XPATH_PRODUCT_TRENDING_LIST_OPTION="//div[contains(text(), 'De største bamser')]"
XPATH_PRODUCT_TRENDING_LIST_FOLLOWERS="//p[contains(text(), 'følgere')]"

def scroll_to_element(element):
    scroll_origin = ScrollOrigin.from_element(element)
    ActionChains(driver).scroll_from_origin(scroll_origin, 0, 200).perform()

# Initialize WebDriver (Chrome)
driver = webdriver.Chrome()

# Maximize the window
# driver.maximize_window()

try:
    # Navigate to the website
    driver.get(WEBSITE_URL_BASE)

    # Click on the cookie accept button with the text "Accepter alle"
    cookie_accept_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, XPATH_COOKIE_ACCEPT_BUTTON))
    )
    cookie_accept_button.click()

    # Open "Inspiration" dropdown
    inspiration_dropdown = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, XPATH_INSPIRATION_DROPDOWN))
    )
    inspiration_dropdown.click()

    # Select "Brands" from the dropdown
    brands_option = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.LINK_TEXT, "Brands"))
    )
    brands_option.click()

    # Select "Børn & Baby" category
    born_baby_category = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, XPATH_BORN_BABY_CATEGORY))
    )
    born_baby_category.click()

    # Scroll and click on "Indlæs flere" if needed until you find the "Plysdyr.dk" product link
    while True:
        try:
            # wait till it becomes clickable
            product_name_h2 = driver.find_element(By.XPATH, XPATH_PRODUCT_NAME_H2)
            break
        except:
            print("Could not find the product link")
            time.sleep(2)
            try:
                more_button = driver.find_element(By.XPATH, XPATH_FIND_MORE_BUTTON)
                scroll_to_element(more_button)
                if more_button.is_displayed():
                    more_button.click()
            except Exception as e:
                # Print could not find the product link
                print("Could not find 'Indlæs flere'", e)

    scroll_to_element(product_name_h2)
    print("Found the product name and scrolled to it")
    # Print the immediate tag of the product_name_h2
    # Get the parent with class=fade-in
    product_container = product_name_h2.find_element(By.XPATH, "./ancestor::div[contains(@class, 'fade-in')]")

    try:
        product_link_clickable = product_container.find_element(By.XPATH, ".//descendant::img")
        if product_link_clickable.is_displayed():
            print("Clicked the product link")
            product_link_clickable.click()
        else:
            raise Exception("Could not find the clickable element inside the product link")

    except Exception as e:
        print(f"Failed to find and click the product link: {e}")

    # Open "De største bamser" from the "trending" list
    product_trending_list_option = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, XPATH_PRODUCT_TRENDING_LIST_OPTION))
    )
    product_trending_list_option.click()

    # Wait for the page to load (page title becomes "De største bamser")
    WebDriverWait(driver, 10).until(
        EC.title_contains("De største bamser")
    )
    print("Navigated to the 'De største bamser' page")
    # Wait till the followers count is displayed
    followers_count_elements = WebDriverWait(driver, 10).until(
        EC.visibility_of_all_elements_located((By.XPATH, XPATH_PRODUCT_TRENDING_LIST_FOLLOWERS))
    )
    print("Found the followers count element")
    # Get the text of the element (assuming to have only one element)
    followers_count_text = followers_count_elements[0].text
    followers_count = int(followers_count_text.split()[0])
    # Assert the number of trending list followers (it should be 3)
    assert followers_count == 3, f"Expected 3 followers in the trending list, but found {followers_count}"
    print("Test passed! Number of followers in the trending list is 3.")

finally:
    # Close the browser window
    driver.quit()
