from bs4 import BeautifulSoup as bs
import requests

url = requests.get("https://sslproxies.org")
soup = bs(url.text, "html.parser")

tbody = soup.find("tbody")
rows = tbody.find_all("tr") if tbody else []

with open("proxies.txt", "w") as file:
    for row in rows:
        cells = row.find_all("td")
        if len(cells) >= 2: 
            ip_address = cells[0].text
            port = cells[1].text
            file.write(f"{ip_address}:{port}\n")