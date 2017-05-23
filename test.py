# -*- coding: utf-8 -*-
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import csv


def getPage(driver,spamwriter, pagenum):
    try:
        time.sleep(2)
        btn = driver.find_element_by_xpath('//*[@id="calories-grid_paginate"]/span[3]/span[' + str(pagenum) + ']')
        print(btn.text)
        btn.click()
        time.sleep(2)
        table = driver.find_element_by_xpath('//*[@id="calories-grid"]')
        trs = table.find_elements_by_tag_name('tr')
        for tr in trs[1:]:
            tds = tr.find_elements_by_tag_name('td')
            arr = []
            for td in tds:
                arr.append(td.text)
            try:
                spamwriter.writerow(arr)
            except:
                print("не получилось записать " + str(arr))
    except:
        print("не получилось загрузить "+str(pagenum))

driver = webdriver.Chrome('C:\\Program Files\\SeleniumUtils\\chromedriver.exe')
driver.get("http://dietadiary.com/tablica-kalorijnosti-productov#bju-produktov")
select = Select(driver.find_element_by_name("calories-grid_length"))
select.select_by_visible_text("50")

with open('food_full.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=';',)

    for i in range(1,3):
        getPage(driver,spamwriter, i)

    for i in range(465):
        getPage(driver,spamwriter, 4)

print("complete")