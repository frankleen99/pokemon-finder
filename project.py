# 1 ask for user input 
# 2 create a dynamic url based on step 1
# 3 fetch the data from the url in step 2
# 4 convert JSON to dictionary 
# 5 print out the pokemon data

import requests
while True:
    character = input("Which character do you want to find? ")
    character = character.lower()

    url = f"https://pokeapi.co/api/v2/pokemon/{character}"

    req = requests.get(url)
    if req.status_code == 200:
        data = req.json()
        print (f"Name is\t\t{data['name']}")
        print("Abilities:")
        for ability in data['abilities']:
            print(ability['ability']['name'])
    else: 
        print("Pokemon not found! ")

