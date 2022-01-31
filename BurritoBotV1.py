# bot.py
import os
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import randominfo
import random
from selenium.webdriver.support.select import Select
from random import randint
from selenium.webdriver.common.alert import Alert
s = Service('C:\Program Files (x86)\chromedriver.exe')
driver: WebDriver = webdriver.Chrome(service=s)

import discord


firstname = randominfo.get_first_name(gender = None)
lastname = randominfo.get_last_name()
email = (firstname + lastname + '@gmail.com')
phonedata = random.randint(1111111, 9999999)
phone = ('423' + str(phonedata))
password = (lastname + firstname)
day = random.randint(1,30)
monthdata = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November","December")
month = random.choice(monthdata)
year = random.randint(1970,2000)

TOKEN = ('ODgzODg0MjA0Mzk4NjMzMDMw.YTQbUA._GlYIylUTjFdofdllmwTwom_pHk')

client = discord.Client()


@client.event


async def on_message(message):
    if message.author == client.user:
        return

    burrito = [
        'Making burrito!',
        'Making burrito!',
        (
            'Making burrito! ',
            'Making burrito!'
        ),
    ]

    if message.content == '!burrito':
        response = random.choice(burrito)
        await message.channel.send(response)
        driver.get("https://salsaritas.com/rewards-sign-up/")
        sleep(5)
        driver.maximize_window()
        sleep(5)
        driver.switch_to.frame(0)
        driver.find_element_by_id("user_email").send_keys(email)
        sleep(1)
        driver.find_element_by_id("user_first_name").send_keys(firstname)
        sleep(1)
        driver.find_element_by_id("user_last_name").send_keys(lastname)
        sleep(1)
        driver.find_element_by_id("user_phone").send_keys(phone)
        sleep(1)
        driver.find_element_by_id("user_password").send_keys(password)
        sleep(1)
        driver.find_element_by_id("user_password_confirmation").send_keys(password)
        sleep(1)
        Select(driver.find_element_by_id("user_birthday_3i")).select_by_value(str(day))
        sleep(1)
        Select(driver.find_element_by_id("user_birthday_2i")).select_by_visible_text(str(month))
        sleep(1)
        Select(driver.find_element_by_id("user_birthday_1i")).select_by_visible_text(str(year))
        sleep(1)
        Select(driver.find_element_by_id("user_fav_location_id")).select_by_visible_text("Morristown")
        sleep(5)
        driver.find_element_by_id("invisible-recaptcha").click()
        sleep(60)
        driver.find_element_by_id("redemption-offers").click()
        driver.get("https://iframe.punchh.com/whitelabel/salsaritas/offers")

        alert = Alert(driver)

        sleep(10)
        driver.find_element_by_id("offer-submit").click()
        sleep(5)
        alert.accept()
        code = driver.find_element_by_class_name("congrats-code").text
        print("Code:")
        print(code)
        await client.get_channel(930323308862390312).send(code)


client.run(TOKEN)


