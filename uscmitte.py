#Book usc for beachvolleyball 
import os
from playwright.async_api import async_playwright
import asyncio
import pandas as pd
import asyncio
from playwright.async_api import async_playwright, Playwright
from datetime import datetime, timedelta
email = ""
password = ""
# Calculate the date 5 days from today
today = datetime.now()
target_date = today + timedelta(days=13)
# Format the date to match the format used in your page.get_by_text() call
# Use %a for abbreviated weekday name, remove the last letter, and remove leading zeros by converting day to an integer
formatted_date = f"{target_date.strftime('%a')[:-1]} {int(target_date.strftime('%d'))}"

async def run(playwright: Playwright):
    chromium = playwright.firefox # or "firefox" or "webkit".
    browser = await chromium.launch(headless = False)
    page = await browser.new_page()
    await page.goto("https://urbansportsclub.com/en/venues/community-sports-beachmitte") #Testing playground berlin booking , change this to community sports 
    await page.get_by_role("button", name="Accept all cookies").click()
    await page.get_by_role("link", name="Log in").click()
    await page.get_by_placeholder("Email *").click()
    await page.get_by_placeholder("Email *").type(email,delay =200)
    await page.get_by_placeholder("Email *").press("Tab")
    await page.get_by_placeholder("Password *").type(password, delay=250)
    await page.get_by_role("insertion").click()
    await page.get_by_role("button", name="Login").click()
    # courses 
    #await page.get_by_text("Free Trainings", exact=True).click()
    print("courses")
    await page.get_by_role("button", name="").click()
    await page.get_by_text(formatted_date).click()
    print(formatted_date)
    await page.get_by_text("Community Sports – Beachvolleyball Beach Volleyball").click()

    #await page.get_by_text("19:00 — 21:00").click()----> this doesnt give me anything but time
    #await page.get_by_role("link", name="Beachvolleyball Training A2/A3 (-50%)").nth(1).click()
    #await page.get_by_role("link", name="Continue").second.click()---> first continue button (this should be the case for USC)
    # await page.get_by_role("link", name="Continue").nth(2).click() #---> second continuebutton
        # Check if "Instant book" button is present
    try:
        await page.wait_for_selector('button:has-text("Instant book")', state='visible', timeout=5000)
        print("Instant book button is present.")
        await page.click('button:has-text("Instant book")')
        await asyncio.sleep(10) # Wait for 10 seconds
    except:
        print("Instant book button is not present.")

    # Check if "Cancel booking" button is present
    try:
        await page.wait_for_selector('button:has-text("Cancel booking")', state='visible', timeout=5000)
        print("Cancel booking button is present.")
        # Hover over the "Cancel booking" button and wait for 10 seconds
        await page.hover('button:has-text("Cancel booking")')
        await asyncio.sleep(10) # Wait for 10 seconds
    except:
        print("Cancel booking button is not present.")

    print("finishing the code")

    print("time")
    await asyncio.sleep(10)
 

async def main():
    async with async_playwright() as playwright:
        await run(playwright)
asyncio.run(main())