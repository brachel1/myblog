from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

# Set up Selenium to use Chrome
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode (no UI)
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--ignore-ssl-errors')

# Initialize the WebDriver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
driver.set_page_load_timeout(30)  # Increase the page load timeout

# URL of the Utah Jazz roster page
url = 'https://www.nhl.com/utah/roster'
driver.get(url)

# Use WebDriverWait to wait for player links to load
try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, "//a[contains(@href, '/player/')]"))
    )
    # Extract player links and names
    player_elements = driver.find_elements(By.XPATH, "//a[contains(@href, '/player/')]")
    player_data = []
    for element in player_elements:
        player_id = element.get_attribute('href').split('/')[-1]
        player_name = element.find_element(By.XPATH, "./ancestor::div[@class='sc-dlDPRo eHWnvT']").get_attribute('aria-label').replace(" ", "-").lower()
        player_data.append((player_id, player_name))
except Exception as e:
    print(f"Error finding player links: {e}")
    driver.quit()
    exit()

# Function to construct the player URL
def construct_url(name, player_id):
    return f"https://www.nhl.com/utah/player/{name}-{player_id}"

# Function to scrape career stats from a player's page
def scrape_player_stats(player_url):
    for attempt in range(3):  # Try up to 3 times
        try:
            driver.get(player_url)
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '#CAREER-tabpanel > div.sc-hLtZSE.cKhdQH > div > table'))
            )
            # Find the career stats table
            career_stats_table = driver.find_element(By.CSS_SELECTOR, '#CAREER-tabpanel > div.sc-hLtZSE.cKhdQH > div > table')

            # Extract stats into a list of dictionaries
            rows = career_stats_table.find_elements(By.TAG_NAME, 'tr')
            headers = [header.text for header in rows[0].find_elements(By.TAG_NAME, 'th')]
            stats = []
            for row in rows[1:]:
                cells = row.find_elements(By.TAG_NAME, 'th') + row.find_elements(By.TAG_NAME, 'td')
                stat = {headers[i]: cells[i].text for i in range(len(cells))}
                stats.append(stat)
            return stats
        except TimeoutException:
            wait_time = 2 ** attempt  # Exponential backoff
            print(f"Timeout on {player_url}, retrying in {wait_time} seconds...")
            time.sleep(wait_time)
        except Exception as e:
            print(f"Error scraping stats from {player_url}: {e}")
            return []
    return []  # If all retries fail, return an empty list

# Initialize a list to hold all players' stats
all_players_stats = []

for player_id, player_name in player_data:
    # Construct the URL
    url = construct_url(player_name, player_id)

    # Scrape player stats
    player_stats = scrape_player_stats(url)

    # Add player name to each stat dictionary
    for stat in player_stats:
        stat['Player Name'] = player_name
        stat['Player ID'] = player_id

    all_players_stats.extend(player_stats)
# Create a DataFrame from the collected stats
df = pd.DataFrame(all_players_stats)

# Print the DataFrame
print(df)

# Optional: Save to CSV
df.to_csv('utah_nhl_players_stats.csv', index=None)