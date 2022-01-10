from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time
import csv
START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs#Field_brown_dwarfs"
browser = webdriver.Chrome("C:/Users/sibsankar maity/Desktop/projects/webScraping2/chromedriver.exe")
browser.get(START_URL)
time.sleep(10)
headers = ["name", "light_years_from_earth", "planet_mass", "stellar_magnitude", "discovery_date", "hyperlink", "planet_type", "planet_radius", "orbital_radius", "orbital_period", "eccentricity"]
planet_data = []
new_planet_data = []
def scrape():
    for i in range(1, 430):
        while True:
            time.sleep(2)
            soup = BeautifulSoup(browser.page_source, "html.parser")
            current_page_num = int(soup.find_all("input", attrs={"class", "page_num"})[0].get("value"))
            if current_page_num < i:
                browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
            elif current_page_num > i:
                browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[1]/a').click()
            else:
                break
        for ul_tag in soup.find_all("ul", attrs={"class", "exoplanet"}):
            li_tags = ul_tag.find_all("li")
            temp_list = []
            for index, li_tag in enumerate(li_tags):
                if index == 0:
                    temp_list.append(li_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(li_tag.contents[0])
                    except:
                        temp_list.append("")
            planet_data.append(temp_list)
        browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
    with open("final.csv", "w") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(final_planet_data)    
scrape()



