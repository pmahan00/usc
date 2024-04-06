import os
from playwright.async_api import async_playwright
import asyncio
import pandas as pd
from datetime import datetime, timedelta

email = ""
password = ""

# Calculate the date 5 days from today
today = datetime.now()
target_date = today + timedelta(days=3)
formatted_date = f"{target_date.strftime('%a')[:-1]} {int(target_date.strftime('%d'))}"
print(formatted_date)

async def run(playwright):
    chromium = playwright.firefox # or "firefox" or "webkit".
    browser = await chromium.launch(headless=False)
    page = await browser.new_page()
    await page.goto("https://urbansportsclub.com/en/sports/bootcamp/berlin")
    await page.get_by_role("button", name="Accept all cookies").click()
    await page.get_by_role("link", name="Log in").click()
    await page.get_by_placeholder("Email *").click()
    await page.get_by_placeholder("Email *").type(email, delay=200)
    await page.get_by_placeholder("Email *").press("Tab")
    await page.get_by_placeholder("Password *").type(password, delay=250)
    await page.get_by_role("insertion").click()
    await page.get_by_role("button", name="Login").click()
    await page.get_by_role("link", name="BEAT81 - Alexanderplatz Indoor Workout", exact=True).click()
    print('alexander platz')
    await page.get_by_text("Courses", exact=True).click()
    print("courses")
    await page.get_by_text(formatted_date).click()
    print("date")
    await page.get_by_text(":30 — 11:15").click()
    print("time")
    await page.get_by_role("link", name="Strength & Cardio V2.0 with Marija 🇬🇧 - BEAT81").nth(1).click()

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

async def main():
    async with async_playwright() as playwright:
        await run(playwright)

asyncio.run(main())

