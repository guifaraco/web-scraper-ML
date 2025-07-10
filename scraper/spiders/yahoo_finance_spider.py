# THIS THING IS DRIVING ME CRAZY. I FOUGHT A TOUGH FIGHT AGAINST YAHOO FINANCE'S ANTI-WEBSCRAPING AND ULTIMATELY LOST, BUT NOT ENTIRELY. THE SILVER LINING IS THAT I LEARNED A TON FROM INSPECTING THEIR HTTP REQUESTS.
# RIP SANITY...

# import time
# from scraper.base_spider import BaseSpider


# class YahooFinanceSpider(BaseSpider):
#     START_URL = "https://finance.yahoo.com/research-hub/screener/sec-ind_sec-largest-equities_healthcare"

#     def __init__(self):
#         super().__init__("YahooFinanceScreener_Selenium")
        
#         chrome_options = Options()
#         chrome_options.add_argument("--headless")
#         chrome_options.add_argument("--window-size=1920,1080")
#         chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36")
        
#         chrome_options.add_argument("--no-sandbox")
#         chrome_options.add_argument("--disable-dev-shm-usage")
#         chrome_options.add_argument("--disable-gpu")

#         self.driver = webdriver.Chrome(options=chrome_options)

#     def get_data(self):
#         print("Driving browser to the start URL...")
#         self.driver.get(self.START_URL)
#         all_html_content = ""
#         page_count = 1

#         try:
#             while True:
#                 print(f"Scraping page {page_count}...")
#                 wait = WebDriverWait(self.driver, 20)
#                 wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "table tbody tr")))
                
#                 all_html_content += self.driver.page_source

#                 next_button = self.driver.find_element(By.CSS_SELECTOR, "button[data-test='pagination-next-btn']")
                
#                 if not next_button.is_enabled():
#                     print("Last page reached. Finishing data collection.")
#                     break
                
#                 print("Clicking 'Next' button...")
#                 next_button.click()
#                 page_count += 1
#                 time.sleep(3)

#         except Exception as e:
#             print(f"An error occurred during browser automation: {e}")
#         finally:
#             self.driver.quit()
#             print("Browser session closed.")
        
#         return all_html_content

#     def parse_data(self, raw_data):
#         if not raw_data:
#             return []
            
#         print("Parsing collected HTML...")
#         soup = BeautifulSoup(raw_data, 'html.parser')
#         all_stocks = []

#         rows = soup.select("table tbody tr")

#         for row in rows:
#             cells = row.find_all("td")
#             if len(cells) > 5:
#                 stock_data = {
#                     "ticker": cells[0].text.strip(),
#                     "company_name": cells[1].text.strip(),
#                     "price": cells[2].text.strip(),
#                     "change": cells[3].text.strip(),
#                     "percent_change": cells[4].text.strip(),
#                 }
#                 all_stocks.append(stock_data)
        
#         return all_stocks