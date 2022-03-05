from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time
import os

URL = "https://www.linkedin.com/jobs/search/?f_AL=true&geoId=90009713&keywords=Junior%20Python%20Developer&location=Region%20K%C3%B6ln%2FBonn&sortBy=R"
USER = os.environ["USER"]
PW = os.environ["PW"]
TEL = os.environ["TEL"]

s = Service("C:\Development\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get(URL)


# - - - - - - - - - - J O B S - - - - - - - - - -
log_in_a = driver.find_element(By.LINK_TEXT, "Einloggen")
log_in_a.click()

time.sleep(1)


# - - - - - - - - - - L O G I N - - - - - - - - - -
email = driver.find_element(By.ID, "username")
email.send_keys(USER)

pw = driver.find_element(By.ID, "password")
pw.send_keys(PW)
pw.send_keys(Keys.ENTER)
# fails:
# log_in_btn = driver.find_element(By.XPATH, "//form/div/btn")
# log_in_btn = driver.find_element(By.CSS_SELECTOR, "from btn")
# log_in_btn = driver.find_element(By.CLASS_NAME, "btn__primary--large from__button--floating")

time.sleep(2)


# - - - - - - - - - - J O B S - - - - - - - - - -
def open_job():
    try:
        apply_btn = driver.find_element(By.CSS_SELECTOR, ".jobs-apply-button")
        apply_btn.click()
        # fails:
        # apply_btn = driver.find_element(By.XPATH, "//div[@class=jobs-apply-button--top-card]/btn")
        time.sleep(1)
        return True
    except NoSuchElementException:
        print("No Button, as Company has already been contacted -> abort")
        return False

# - - - - - - - - - - A P P L I C A T I O N - - - - - - - - - -


def check_for_submit():
    try:
        driver.find_element(By.XPATH, "//button[@aria-label='Bewerbung senden']")
        return True
    except NoSuchElementException:
        print("No 'Bewerbung senden'-Btn found -> abort")
        return False


def check_for_double():
    for sent_heading in sent_apps:
        current_heading = driver.find_element(By.CSS_SELECTOR, "#jobs-apply-header")
        if sent_heading == str(current_heading.text.encode("utf8")):
            print("Company has already been contacted in the past -> abort")
            return False
    return True


def close_job_appl():
    close = driver.find_element(By.XPATH, "//li-icon[@type='cancel-icon']")
    close.click()
    discard = driver.find_element(By.XPATH, "//button[@data-control-name='discard_application_confirm_btn']")
    discard.click()


def fill_info():
    tel = driver.find_element(By.CLASS_NAME, "ember-text-field")
    tel.send_keys(TEL)
    try:
        follow = driver.find_element(By.XPATH, "//label[@for='follow-company-checkbox']")
        follow.click()
    except NoSuchElementException:
        print("No Unsubscribe-Btn found")


def submit():
    submit = driver.find_element(By.CSS_SELECTOR, "footer button")
    submit.click()
    time.sleep(1)
    close = driver.find_element(By.XPATH, "//li-icon[@type='cancel-icon']")
    close.click()
    # discard = driver.find_element(By.XPATH, "//button[@data-control-name='discard_application_confirm_btn']")
    # discard.click()



def gather_results():
    try:
        found_jobs = driver.find_elements(By.CSS_SELECTOR, ".jobs-search-results__list-item")
        return found_jobs
    except NoSuchElementException as e:
        print(str(e))
        return []


def add_application_to_list():
    heading = driver.find_element(By.CSS_SELECTOR, "#jobs-apply-header")
    sent_apps.append(heading.text.encode("utf8"))


# - - - - - - - - - - M A I N   S C R I P T - - - - - - - - - -
results = gather_results()
sent_apps = []
with open("sent_apps.txt", "r", encoding='utf8') as f:
    sent_apps = [app.rstrip() for app in f.readlines()]

for result in results:
    result.click()
    time.sleep(1)
    if open_job():
        if check_for_submit() and check_for_double():
            add_application_to_list()
            print(f"{len(sent_apps)} appl. sent")
            fill_info()
            submit()
        else:
            close_job_appl()
    if len(sent_apps) >= 10:
        break
    time.sleep(1)

with open('sent_apps.txt', 'w') as f:
    f.writelines("%s\n" % appl for appl in sent_apps)
