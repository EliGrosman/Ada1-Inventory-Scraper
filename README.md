# Ada1ModScraper

A python script that fetches Ada-1's current inventory in Destiny 2 and puts it into a database.

## Setup

Out of the box, this script is set up for a MySQL database running on the local machine with the name 'adamods'. 
You can either create a database to match this configuration or make adjustments as needed to match your system.

You will also need a Bungie API application in order to access Ada's mods. You can register an application here: https://www.bungie.net/en/Application. I recommend setting your OAuth Client Type to "Confidential".
After creating your application, take note of your API Key, OAuth client_id, and OAuth client_secret. You will need these later.

Before starting the script, you will need a refresh token. This can be confusing to find so I suggest following this guide: https://lowlidev.com.au/destiny/authentication-2.  
Once you have a refresh token, paste it in `tokens.txt`. The script will use this to get a new access token and refresh token each time it runs.

## Running the script

When running the script you will need to include your database password, API key, and client secret as command line arguments. The syntax should look like:
`python getMods.py DATABASE_PASSWORD API_KEY CLIENT_SECRET`

Ada's mods change daily so running the script once a day will add everything she is selling to the database. I suggest setting up a cron job to automate this! 

## Insights

Some interesting visualizations using data from the past year can be found here:
https://public.tableau.com/views/Destiny2Mods/Story1?:language=en-US&publish=yes&:display_count=n&:origin=viz_share_link
