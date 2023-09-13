import requests
from bs4 import BeautifulSoup

# Define the Craigslist URL for your location, search category, and location radius
craigslist_url = "https://denver.craigslist.org/search/bia"

# Define the keywords to search for in the Craigslist listings
keywords = ["domane", "roubaix", "endurance", "defy", "synapse", "strael"]
# Define the keywords to filter out of the Craigslist listings
search_words = ["trek domane", "specialized roubaix", "canyon endurance", "giant defy", "cannondale synapse", "endurance"]
sizes = ["53cm", "53 cm", "54cm", "54 cm", "medium", "small"]

# Define the location (ZIP code) and search radius (in miles)
location = "80111"
search_radius = 55

# Function to search Craigslist and return matching results
def search_craigslist(url, keywords, location, search_radius):
    # Build the query string as a or-separated list of keywords
    query = '|'.join(keywords)
    # Build the URL with location and radius parameters
    search_url = f"{url}?search_distance={search_radius}&postal={location}&query={query}"
    response = requests.get(search_url)
    print(f"Searching Craigslist for {keywords} in {location} within {search_radius} miles...")
    print(f"URL: {response.url}\n")
    print("----------------------------------------")

    if response.status_code == 200:
        print("Success!\n")
        soup = BeautifulSoup(response.text, 'html.parser')
        listings = soup.find_all('li', class_='cl-static-search-result')
        if not listings:
            print("No listings found on the page.")
        else:
            for listing in listings:
                # filter by search_words
                if not any(word in listing.text.lower() for word in search_words):
                    continue
                # filter by size
                if not any(size in listing.text.lower() for size in sizes):
                    continue
                title = listing.find('div', class_='title')
                price = listing.find('div', class_='price')
                location = listing.find('div', class_='location')
                link = listing.find('a')['href']
                if title and price:
                    title_text = title.text.strip()
                    price_text = price.text.strip()
                    location_text = location.text.strip() if location else 'N/A'
                    description = extract_description(link)
                    print(f"Title: {title_text}")
                    print(f"Price: {price_text if price else 'N/A'}")
                    print(f"Location: {location_text}")
                    print(f"Description: {description}")
                    print(f"Link: {link}")
                    print("\n")
    else:
        print("An error occurred, response code:", response.status_code)
        print(response.text)

# Function to extract the description from a Craigslist listing URL
def extract_description(listing_url):
    response = requests.get(listing_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        description = soup.find('section', {'id': 'postingbody'})
        return description.text.strip() if description else 'No description available'
    else:
        return 'Failed to retrieve listing description'

# Call the search function
search_craigslist(craigslist_url, keywords, location, search_radius)
