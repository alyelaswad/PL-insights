import requests
from bs4 import BeautifulSoup
import csv

page = requests.get("https://onefootball.com/en/competition/premier-league-9/results")

class Match:
    def __init__(self,homeTeam,awayTeam,Score,Date):
        self.homeTeam = homeTeam
        self.awayTeam = awayTeam
        self.Score = Score
        self.Date = Date
    def displayMatch(self):
        print(f"{self.homeTeam} {self.Score} {self.awayTeam}")
        
def main(page):
    src= page.content
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

main(page)
