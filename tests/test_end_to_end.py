import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

@pytest.fixture
def driver():
    # Set up the WebDriver
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
    driver.get("http://localhost:3000")
    yield driver
    # Tear down the WebDriver after the test
    driver.quit()

def test_add_user(driver):
    pseudo, email, password = 'end_to_end', 'end_to_end@example.com', 'endtoend'
    # sleep to let the page load
    time.sleep(3)
    menu_button = driver.find_element(By.CSS_SELECTOR, ".btn.btn-ghost.btn-circle")
    menu_button.click()
    # get the button to add a user
    add_user_button = driver.find_element(By.ID, 'add_user')
    add_user_button.click()
    # get the input fields
    pseudo_input = driver.find_element(By.ID, 'add_user_pseudo')
    email_input = driver.find_element(By.ID, 'add_user_email')
    password_input = driver.find_element(By.ID, 'add_user_password')
    # fill the input fields
    pseudo_input.send_keys(pseudo)
    email_input.send_keys(email)
    password_input.send_keys(password)
    # get the button to submit the form
    submit_button = driver.find_element(By.ID, 'add_user_submit')
    # click on the button
    submit_button.click()
    time.sleep(1)
    # now check if the user is in the list of users
    users_select = driver.find_element(By.ID, 'select_user')
    user_options = users_select.find_elements(By.TAG_NAME, "option")
    user_list = [option.text for option in user_options]

    assert pseudo in user_list

def test_create_task(driver):
    task_title = "End-to-End Task"
    user_pseudo = "end_to_end"

    time.sleep(3)

    # Locate the "Add Task" button and click on it
    add_task_button = driver.find_element(By.ID, "add_task")
    add_task_button.click()

    # Fill in the task creation form
    task_title_input = driver.find_element(By.ID, "add_task_title")
    task_title_input.send_keys(task_title)

    # Check the "Done" checkbox
    done_checkbox = driver.find_element(By.ID, "add_task_done")
    done_checkbox.click()

    # Select the user from the dropdown
    user_select = driver.find_element(By.ID, "add_task_user")
    user_select.send_keys(Keys.DOWN)
    user_select.send_keys(Keys.ENTER)


    # Submit the form
    submit_button = driver.find_element(By.ID, "add_task_submit")
    submit_button.click()

    # Wait for the task to be added to the list
    time.sleep(1)
    task_list_items = driver.find_elements(By.CSS_SELECTOR, ".card.bg-base-300.text-primary-content")
    assert task_list_items is not None
    
    # Create a list of dicts with the task data
    task_list = []
    for task in task_list_items:
        task_list.append({
            "title": task.find_element(By.CSS_SELECTOR, ".card-title").text,
            "done": task.find_element(By.CSS_SELECTOR, ".badge").text == "Done",
        })
    
    # check if in the list we have a dict with the right data
    wanted_task = {
        "title": task_title,
        "done": True,
    }
    assert wanted_task in task_list
