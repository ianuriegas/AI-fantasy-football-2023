import requests
from bs4 import BeautifulSoup

url = "https://www.nfl.com/schedules/2023/REG1/"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Save the soup content to a file named "temp.html"
with open("temp.html", "w", encoding="utf-8") as file:
    file.write(str(soup))