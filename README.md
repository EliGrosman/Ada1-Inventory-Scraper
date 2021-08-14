# Ada1ModScraper

A python script that fetches Ada-1's current inventory in Destiny 2 and puts it into a database.

## Setup

Out of the box, this script is set up for a MySQL database running on the local machine with the name 'adamods'. 
You can either create a database to match this configuration or make adjustments as needed to match your system.

You will also need a Bungie API application in order to access Ada's mods. You can register an application here: https://www.bungie.net/en/Application. I recommend setting your OAuth Client Type to "Confidential".
After creating your application, take note of your API Key, OAuth client_id, and OAuth client_secret. You will need these later.

In the URL on line 12 you will see placeholders "MEMBERSHIP_ID" and "CHARACTER_ID". These are specific to your Destiny 2 profile. To get these, make a GET request to https://www.bungie.net/Platform/Destiny2/SearchDestinyPlayer/-1/YOUR_DESITNY2_NAME (note: YOUR_DESTINY2_NAME is your display name on whichever platform you play on). Include your API Key in the Headers under `X-API-Key`. This will give you your membership Id and membership type. Next, make a GET request to https://www.bungie.net/Platform/Destiny2/YOUR_MEMBERSHIP_TYPE/Profile/YOUR_MEMBERSHIP_ID/?components=200 to obtain your character Id for the character you last played. Paste these into the script.

Before starting the script, you will need a refresh token. This can be confusing to find so I suggest following this guide: https://lowlidev.com.au/destiny/authentication-2.  
Once you have a refresh token, paste it in `tokens.txt`. The script will use this to get a new access token and refresh token each time it runs.

## Running the script

When running the script you will need to include your database password, API key, and client secret as command line arguments. The syntax should look like:
`python getMods.py DATABASE_PASSWORD API_KEY CLIENT_SECRET`

Ada's mods change daily so running the script once a day will add everything she is selling to the database. I suggest setting up a cron job to automate this! 

## Insights

Some interesting visualizations using data from the past year can be found here:
https://public.tableau.com/views/Destiny2Mods/Story1?:language=en-US&publish=yes&:display_count=n&:origin=viz_share_link
