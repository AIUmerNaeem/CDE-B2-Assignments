from selenium import webdriver
path =r'pip install -r requirements.txt'
from selenium.webdriver.chrome.service import Services

werbsite = 'https://www.365scores.com/football/league/laliga-11/standings'
path =r'C:\Users\Omer Naeem\Downloads\chromedriver-win64.zip\chromedriver-win64'

service = Service(path)
service.start()

# Create a new instance of the chrome driver
driver.get(website)

standings = driver.find_element_by_xpath("//a[id= 'navigation-tabs_competition_standing]")

# Create
driver = webdriver.Chrome(path)
driver.get(website)

standings = driver.find_elements_by_xpath('"//table[@class="table"]')
for standing in standing:
# Find the element containing the club name
# club_name = standing.find_elem

