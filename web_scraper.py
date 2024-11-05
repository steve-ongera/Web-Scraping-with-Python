import requests
from bs4 import BeautifulSoup
import csv

# The URL of the website you want to scrape
url = 'https://www.worldometers.info/world-population/'

# Send an HTTP request to the URL and get the response
response = requests.get(url)

# If the response is successful (status code 200), parse the HTML
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find all <a> tags (links)
    links = soup.find_all('a')
    
    # Open a CSV file to save the scraped data
    with open('scraped_links.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        
        # Write the header (column names)
        writer.writerow(['Link Text', 'URL'])
        
        # Loop through the links and save each to the CSV file
        for link in links:
            link_text = link.get_text()
            link_url = link.get('href')
            writer.writerow([link_text, link_url])

    print("Scraping complete! Data saved in 'scraped_links.csv'.")
else:
    print("Failed to retrieve the page. Status code:", response.status_code)
