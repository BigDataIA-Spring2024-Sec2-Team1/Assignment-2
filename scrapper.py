#!/usr/bin/env python
# coding: utf-8


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup
import pandas as pd
from selenium.common.exceptions import NoSuchElementException

def initialize_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # To run Chrome in headless mode
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    return driver

def close_privacy_warning(driver):
    close_button = driver.find_element(By.ID, "closePrivacyWarning")
    close_button.click()

def click_next_button(driver):
    try:
        next_button = driver.find_element(By.CLASS_NAME, "coveo-pager-next")
        next_button.click()
        time.sleep(5)
        return driver
    except NoSuchElementException:
        return None

def scrape(driver, refresher_readings_list):
    time.sleep(5)  # Wait for the page to load
    html_content = driver.page_source
    soup = BeautifulSoup(html_content, 'html.parser')
    titles = soup.find_all('h4', class_='coveo-title')
    for title in titles:
        link = title.find('a', class_='CoveoResultLink')['href']
        reading = [title.text.strip(), link]
        refresher_readings_list.append(reading)

def get_reading_detail_data(driver, reading):
    driver.get(reading[1])
    time.sleep(5)
    html_content = driver.page_source
    soup = BeautifulSoup(html_content, 'html.parser')
    headings = soup.find_all('h2', class_="article-section")
    data = {"introduction": "", "learning_outcomes": "", "summary": "", "overview": ""}
    for section in headings:
        if section.text in ('Introduction', "Learning Outcomes", "Summary", "Overview"):
            if section.text == "Introduction":
                data["introduction"] = section.findParent().text
            elif section.text == "Learning Outcomes":
                data["learning_outcomes"] = section.find_next().text
            elif section.text == "Summary":
                data["summary"] = section.find_next().text
            elif section.text == "Overview":
                data["overview"] = section.find_next().text
    return data

def scrape_reading_detail(refresher_readings_list):
    data_list = []
    driver = initialize_driver()
    for reading in refresher_readings_list:
        reading_detail = get_reading_detail_data(driver, reading)
        data_list.append({
            'Title': reading[0],
            'Introduction': reading_detail['introduction'],
            'Learning Outcomes': reading_detail['learning_outcomes'],
            'Summary': reading_detail['summary'],
            'Overview': reading_detail['overview']
        })
    driver.quit()
    df = pd.DataFrame(data_list)
    return df

def main():
    refresher_readings_list = []
    driver = initialize_driver()
    url = "https://www.cfainstitute.org/en/membership/professional-development/refresher-readings#first=10&sort=%40refreadingcurriculumyear%20descending"
    driver.get(url)
    close_privacy_warning(driver)
    for page_num in range(23):
        scrape(driver, refresher_readings_list)
        driver = click_next_button(driver)
        if driver is None:
            break
    df = scrape_reading_detail(refresher_readings_list)
    print(df)
    df.to_csv('refresher_readings.csv', index=False)

if __name__ == "__main__":
    main()

