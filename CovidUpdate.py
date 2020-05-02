import requests
from bs4 import BeautifulSoup
import os

clear = lambda: os.system('cls')
res = requests.get('https://news.google.com/covid19/map?hl=en-PH&gl=PH&ceid=PH:en')
soup = BeautifulSoup(res.text, 'html.parser')
link = soup.select(".l3HOY")
covid_list = []
covid_list_temp = ["Country", "Confirm", "Per 1m", "Deaths", "Recovered"]
count = 0
for a in link:
    covid_list_temp[count] = a.text.strip().upper()
    count += 1
    if count > 4:
        covid_list.append(covid_list_temp)
        covid_list_temp = ["Country", "Confirm", "Per 1m", "Deaths", "Recovered"]
        count = 0

user_input = ""
is_true = True

while is_true:
    clear()
    print("=" * 45)
    print(" " * 10, "Covid19 Cases Live Update")  # 25
    print("=" * 45)
    print(covid_list[0][0])
    print("{:>14}{:>15}".format("Confirmed:", covid_list[0][1]))
    print("{:>14}{:>15}".format("Recovered:", covid_list[0][3]))
    print("{:>14}{:>15}".format("Deaths:", covid_list[0][4]))
    print("")

    for row, country in enumerate(covid_list):

        if user_input == country[0]:
            print(covid_list[row][0])
            print("{:>14}{:>15}".format("Confirmed:", covid_list[row][1]))
            print("{:>14}{:>15}".format("Recovered:", covid_list[row][3]))
            print("{:>14}{:>15}".format("Deaths:", covid_list[row][4]))
            print("")

    user_input = input("Enter Country: ").upper()
    if user_input == "EXIT":
        is_true = False
