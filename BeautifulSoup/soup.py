import requests
from bs4 import BeautifulSoup

# Define the keyword to search for
keyword = "inno glow burn"

# Define the base URL of the website
base_url = "https://www.innosupps.com"

# Initialize a list to store the URLs of all pages
page_urls = []

# Start on the first page of the website
page = 1

# Use a while loop to iterate through each page
while True:
    # Construct the URL for the current page
    url = f"{base_url}?page={url}"

    # Make a request to the website
    response = requests.get(url)

    # Parse the HTML content of the website
    soup = BeautifulSoup(response.content, "html.parser")

    # Find all instances of the keyword on the website
    matches = soup.find_all(string=lambda text: keyword in text)

    # Print the number of matches found
    print(f"Found {len(matches)} instances of '{keyword}' on page {page}")

    # Print the text of each match
    for match in matches:
        print(match)

    # Check if there is a link to the next page
    next_page = soup.find("a", {"class": "next-page"})

    # If there is no link to the next page, break out of the loop
    if not next_page:
        break

    # If there is a link to the next page, add it to the list of page URLs
    page_urls.append(next_page["href"])

    # Increment the page number
    page += 1
