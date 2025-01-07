import requests
from bs4 import BeautifulSoup
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

# page = requests.get("https://onefootball.com/en/competition/premier-league-9/results")
driver.get("https://onefootball.com/en/competition/premier-league-9/results")
time.sleep(15)
try:
    cookies_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'I Accept')]"))
    )
    cookies_button.click()
    print("Cookies consent clicked")
except:
    print("Cookies consent button not found or already handled")

show_all_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Show all results')]")
show_all_button.click()
time.sleep(5)
src = driver.page_source
# driver.quit()
class Match:
    def __init__(self,homeTeam,awayTeam,Score,Date):
        self.homeTeam = homeTeam
        self.awayTeam = awayTeam
        self.Score = Score
        self.Date = Date
    def displayMatch(self):
        print(f"{self.homeTeam} {self.Score} {self.awayTeam}")
        
def main(src):
    # src= page.content
    soup = BeautifulSoup(src,"lxml")
    allGameweeks = soup.find_all('div',{"class": 'MatchCardsListsAppender_container__y5ame'})
    allMatches = allGameweeks[0].find_all('ul',{'class':'MatchCardsList_matches__8_UwB'})
    # numMatchesInGW = len(allMatches[0])
    # print(len(allGameweeks[0]))
    all_TeamNames = []
    all_TeamScores = []
    
    for j in range(len(allMatches)):
        TeamNames = allMatches[j].find_all('span', {'class': 'SimpleMatchCardTeam_simpleMatchCardTeam__name__7Ud8D'})
        TeamScores = allMatches[j].find_all('span', {'class': 'SimpleMatchCardTeam_simpleMatchCardTeam__score__UYMc_'})

        # print(myMatch.text)
        for i in range(len(TeamNames)):
            all_TeamNames.append(TeamNames[i].text)
            all_TeamScores.append(TeamScores[i].text)

    allMatches_scraped=[]
    for i in range(0,len(all_TeamNames),2):
        score = f"{all_TeamScores[i]} - {all_TeamScores[i+1]}"
        allMatches_scraped.append(Match(all_TeamNames[i],all_TeamNames[i+1],score,""))

    GWnum = 20
    for i in range(len(allMatches_scraped)):
        if (i%10 == 0):
            print("-" * 50)
            print(f"Gameweek {GWnum}")
            GWnum = GWnum -1
        allMatches_scraped[i].displayMatch()

main(src)
