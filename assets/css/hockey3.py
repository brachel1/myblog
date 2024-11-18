from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

# Set up Selenium to use Chrome
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--ignore-ssl-errors')

# Initialize the WebDriver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
driver.set_page_load_timeout(30)

# URL of the Utah Hockey Club roster page
url = 'https://www.nhl.com/utah/roster'
driver.get(url)

# Wait for the player rows to be visible
try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, "//tr[contains(@class, 'rt-tr')]"))
    )
    # Extract player rows
    player_rows = driver.find_elements(By.XPATH, "//tr[contains(@class, 'rt-tr')]")
    player_data = []
    for row in player_rows:
        try:
            # Extracting data from each row
            player_name = row.find_element(By.XPATH, ".//th//a").text
            player_id = row.find_element(By.XPATH, ".//th//a").get_attribute('href').split('/')[-1]
            player_number = row.find_element(By.XPATH, ".//td[1]").text
            player_position = row.find_element(By.XPATH, ".//td[2]").text
            player_handedness = row.find_element(By.XPATH, ".//td[3]").text
            player_height = row.find_element(By.XPATH, ".//td[4]").text
            player_weight = row.find_element(By.XPATH, ".//td[5]").text
            player_birthdate = row.find_element(By.XPATH, ".//td[6]").text
            player_birthplace = row.find_element(By.XPATH, ".//td[7]//span").text

        except Exception as e:
            print(f"Error extracting data for player: {e}")
            continue

        # Add the player's data to the list
        player_data.append({
            'Player ID': player_id,
            'Player Name': player_name,
            'Number': player_number,
            'Position': player_position,
            'Handedness': player_handedness,
            'Height': player_height,
            'Weight': player_weight,
            'Birthdate': player_birthdate,
            'Birthplace': player_birthplace
        })

except Exception as e:
    print(f"Error finding player data: {e}")
finally:
    driver.quit()

# Create a DataFrame and save to CSV
df = pd.DataFrame(player_data)
print(df)

# Optional: Save to CSV
df.to_csv('utah_nhl_players_info.csv', index=None)
