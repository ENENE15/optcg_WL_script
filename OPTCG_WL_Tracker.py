import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

EVENTS_URL = ("https://www.bandai-tcg-plus.com/my_event"
              "?favorite=0&game_title_id=&limit=20&offset=0"
              "&past_event_display_flg=1&pref_code[]=&selected_tab=3")

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 15)

#Login manually
driver.get(EVENTS_URL)
input("Log in manually in the Chrome window, then press ENTER here to start scraping...")

try:
    # Click the "Display Results" dropdown/toggle
    display_count = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "label.btn.icon-display-count"))
    )
    driver.execute_script("arguments[0].scrollIntoView({block:'center'});", display_count)
    driver.execute_script("arguments[0].click();", display_count)
    print("Clicked Display Results toggle")

    # Click "100 results"
    option_100 = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "label[for='displayCountNumber100']"))
    )
    driver.execute_script("arguments[0].scrollIntoView({block:'center'});", option_100)
    driver.execute_script("arguments[0].click();", option_100)
    print("Selected 100 results")
    driver.refresh()

except TimeoutException:
    print("Could not change display count to 100")


# CSV file generation + write
with open("match_history.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Event", "Wins", "Losses", "Ranking"])

    wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "h2.event-name-link")))
    events = driver.find_elements(By.CSS_SELECTOR, "h2.event-name-link")
    page = 1
    while True:
        print(f"\n📄 Scraping page {page}...")
        wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "h2.event-name-link")))


        for i in range(len(events)):
            # Fetch each event in a loop

            driver.execute_script("window.scrollTo(0, 0);")
            time.sleep(1)
            events = driver.find_elements(By.CSS_SELECTOR, "h2.event-name-link")
            event = events[i]
            event_name = event.text.strip()
            print(f"\nProcessing: {event_name}")

            # Click details on Bandai TCG+
            details_btn = event.find_element(By.XPATH, "./following::button[contains(@class,'btn-detail')]")
            driver.execute_script("arguments[0].click();", details_btn)

            # Look for Match History
            time.sleep(2)  
            buttons = driver.find_elements(By.CSS_SELECTOR, "button.navi-icon-btn.history")
            if not buttons:
                print(f"No Match History for {event_name}, skipping...")
                driver.back()
                wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "h2.event-name-link")))
                continue

            # Click Match History
            driver.execute_script("arguments[0].scrollIntoView({block:'center'});", buttons[0])
            driver.execute_script("arguments[0].click();", buttons[0])
            print("Clicked Match History")
            time.sleep(2)
            # Scrape ranking + wins/losses
            try:
                ranking_el = wait.until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "span.rank-number"))
                )
                ranking = ranking_el.text.strip()
            except TimeoutException:
                ranking = "N/A"

            wins = len(driver.find_elements(By.XPATH, "//td[normalize-space(text())='win']"))
            losses = len(driver.find_elements(By.XPATH, "//td[normalize-space(text())='lose']"))

            print(f"{event_name}: {wins} wins, {losses} losses | Rank {ranking}")
            writer.writerow([event_name, wins, losses, ranking])

            # Go back twice
            driver.back()  # match history → details
            time.sleep(2)
            driver.back()  # details → event list
            wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "h2.event-name-link")))
        next_page = page + 1
        try:
            next_btn = driver.find_element(
                By.XPATH, f"//button[@class='btn-page' and normalize-space(text())='{next_page}']"
            )
            driver.execute_script("arguments[0].scrollIntoView({block:'center'});", next_btn)
            driver.execute_script("arguments[0].click();", next_btn)
            print(f"Moved to page {next_page}")
            # Wait for the next page's events to load before looping
            wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "h2.event-name-link")))
            page = next_page
        except NoSuchElementException:
                print("\nNo more pages. Scraping complete.")
                break
    print("\nResults saved to match_history.csv")
    driver.quit()
