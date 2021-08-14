import requests
import time
import sys
import mysql.connector

# apiKey and token come from command line arguments
apiKey = sys.argv[2] 
client_secret = sys.argv[3]
refreshToken = open("tokens.txt", "r").readlines()[0]

# define urls to get data from
ada1Url = "https://www.bungie.net/Platform/Destiny2/3/Profile/4611686018467836343/Character/2305843009299338095/Vendors/350061650/?components=400,401,402"
itemDefUrl = "https://www.bungie.net/common/destiny2_content/json/en/DestinyInventoryItemDefinition-339ab5ed-b919-4d17-9328-cc340f8c2b61.json"
refreshTokenUrl = "https://www.bungie.net/Platform/App/OAuth/Token/"

# create database connection
db = mysql.connector.connect(
  host="localhost",
  user="root",
  password= sys.argv[1],
  database="adamods"
)

cursor = db.cursor()

def getCurrentMods():
    token = getRefreshToken(refreshToken)
    # Get item definitions 
    r = requests.get(itemDefUrl)
    itemDefJson = r.json()

    # Get Ada-1 vendor data
    headers = {"X-API-Key": apiKey, "Authorization": f"Bearer {token}"}
    r = requests.get(ada1Url, headers = headers)
    json = r.json()

    # extract categories and sales from vendor data
    categories = json['Response']['categories']['data']['categories']
    sales = json['Response']['sales']['data']

    # Get the categories used for Ada-1's mods
    modCategories = (categories[1]['itemIndexes'])[0:2]

    rows = []

    for cat in modCategories:
        # extract item hash for each mod
        itemHash = sales[str(cat)]['itemHash']

        # join item hash with item definitions to get the mod type and name
        modType = itemDefJson[str(itemHash)]["itemTypeAndTierDisplayName"]
        modName = itemDefJson[str(itemHash)]["displayProperties"]["name"]

        # format mod type
        if('Armor Mod' in modType):
            modType = "Armor Mod"
        else:
            modType = "Combat Style Mod"

        # append to rows to be added to the DB
        rows.append( (modName, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), modType) )
    
    return rows

def getRefreshToken(refreshToken):
    # set headers and body
    headers = {"X-API-Key": apiKey, "Content-Type": "application/x-www-form-urlencoded"}
    body = {"client_id": "37372", "grant_type": "refresh_token", "refresh_token": refreshToken, "client_secret": client_secret}

    # make request
    r = requests.post(refreshTokenUrl, headers = headers, data = body)
    json = r.json()
    # save refresh token to file for later use
    open("tokens.txt", "w").writelines(json['refresh_token'])
    return json['access_token']

getCurrentMods()