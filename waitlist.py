import os
import asyncio
from playwright.async_api import async_playwright

# This part works with a javascript that has saved your login data, but you can also use your normal login function as you did in the other scripts

async def main():
    auth_file = 'usc.json'

    if not os.path.exists(auth_file):
        raise FileNotFoundError(f"Die Authentifizierungsdatei '{auth_file}' wurde nicht gefunden.")

    async with async_playwright() as p:
        browser = await p.firefox.launch(headless=False)
        context = await browser.new_context(storage_state=auth_file)

        # Setze eine erweiterte Standard-Timeout-Zeit
        context.set_default_timeout(60000)  # 60 Sekunden Timeout

        page = await context.new_page()

# From here it runs the loop the get the spot

        while True:  # Endlose Schleife
            try: # Here you need to adjust the venue and the data you want to get the spot while you're on the waiting list
                await page.goto("https://urbansportsclub.com/en/venues/community-sports-beach61-east61?date=2024-05-03&plan_type=2")
                await asyncio.sleep(5)

                await page.get_by_role("link", name="Continue").click()
                await page.wait_for_selector('button:has-text("Instant book")', state='visible', timeout=5000)
                print("Instant book button is present.")
                await page.click('button:has-text("Instant book")')

                # Überprüfe, ob der "Cancel booking"-Button sichtbar ist
                cancel_button = await page.wait_for_selector('button:has-text("Cancel booking")', state='visible', timeout=5000)
                if cancel_button:
                    print("Der 'Cancel booking'-Button ist sichtbar. Die Schleife wird beendet.")
                    break  # Beende die Schleife

            except Exception as e:
                print(f"Ein Fehler ist aufgetreten: {e}")
                await asyncio.sleep(30)

# Starte das Hauptprogramm
asyncio.run(main())
