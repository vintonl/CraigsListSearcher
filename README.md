# Craigslist Bike Listing Scraper

This Python script allows you to scrape bike listings from Craigslist based on specific keywords, location, and search radius. It retrieves information such as titles, prices, locations, descriptions, and links to individual listings.

## Prerequisites

Before using this script, make sure you have the following:

- Python 3 installed on your system.
- Required Python packages installed: beautifulsoup4


## Usage

1. Clone or download this repository to your local machine.

2. Open a terminal or command prompt and navigate to the directory where the script is located.

3. Customize the script by setting the following parameters:

- `craigslist_url`: The Craigslist URL for your location and desired category (e.g., "https://denver.craigslist.org/search/bia" for bikes).
- `keywords`: A list of keywords to search for. Separate multiple keywords with a pipe symbol ('|') for an OR search.
- `location`: Your ZIP code or location.
- `search_radius`: The search radius in miles from your location.

4. Run the script by executing the following command in the terminal:
    ```
    pip3 install requests beautifulsoup4 
    pip3 road_bike.py
    ```
    
5. The script will begin searching Craigslist for listings that match your keywords within the specified location and radius. It will display information about each matching listing, including the title, price, location, description, and a direct link to the listing.

6. You can also filter the results to find listings that mention "disc brakes" in their title or description.

7. Review the scraped data and use it for your intended purposes, such as finding bike listings that match your criteria.

## Notes

- Craigslist's terms of service may prohibit or restrict web scraping. Use this script responsibly and in compliance with Craigslist's policies.

- Craigslist listings can vary in format and content, so the script relies on text matching to find relevant listings. As a result, not all listings may be captured, and the accuracy of results may depend on the quality of the listing descriptions.
