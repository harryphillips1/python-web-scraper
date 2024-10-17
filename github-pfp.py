import requests
from bs4 import BeautifulSoup as bs
# import bs4 for web scraping and requests to get data from sites
def githubuserpfp():
    url = "https://github.com/" + input("What is the username you would like to search for?")
    r = requests.get(url)
# gets github page data
    soup = bs(r.content, 'html.parser')
    pfp = soup.find('img', {'alt' : "Avatar"})['src']
# searches for pfp and stores it to pfp
    while True:
        answer = input("Would you like to 1) Print the link or 2) Save it to your photos folder?")
        if answer == 1:
            print(pfp)
#
            break
#
        if answer == 2:
#
            name = input("What would you like to call the file?")
            location = input("Specify a file path (optional, will save to the local directory if left blank)")
# adds slash to the end of the path if not included exculding empty paths
            if location.endswith("/") is False or len(location) > 0:
                location = location + "/"
# stores file
            r = requests.get(pfp)  
            with open(location+name+".png", 'wb') as f:
                f.write(r.content)
#
            break
# trys again if valid option isnt selected
        else:
            print("I'm not sure what that means, please try again")
# asks user if it would like to get a github pfp before running function to perform it
if input.lower("Would you like to get a github users profile picture?") == "yes":
    githubuserpfp()
else print("okay")
