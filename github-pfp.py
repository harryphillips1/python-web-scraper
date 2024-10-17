import requests
from bs4 import BeautifulSoup as bs

def githubuserpfp():
    url = "https://github.com/" + input("What is the username you would like to search for?")
    r = requests.get(url)
    
    soup = bs(r.content, 'html.parser')
    pfp = soup.find('img', {'alt' : "Avatar"})['src']
    
    while True:
        answer = input("Would you like to 1) Print the link or 2) Save it to your photos folder?")
        if answer == 1:
            print(pfp)
            
            break

        elif answer == 2:
            
            name = input("What would you like to call the file?")
            location = input("Specify a file path (optional, will save to the local directory if left blank)")
            
            if location.endswith("/") = False or len(location) > 0:
                location = location + "/"

            r = requests.get(pfp)  
            with open(location+name+".png", 'wb') as f:
            f.write(r.content)

            break

        else:
            print("I'm not sure what that means, please try again")
    
if input.lower("Would you like to get a github users profile picture?") == "yes":
    githubuserpfp()
