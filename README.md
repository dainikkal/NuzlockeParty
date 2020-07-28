# NuzlockeParty
A tool that fetches information from a google sheet and creates a image for a party and another image non party mons. 
It should be a helpful tool for streamers. Especially for Nuzlockes the tool is great to visualize your current party or all pokemon you encountered to their streaming audience.

# Prerequisites:
Since the tool is fetching data from a google sheet you need to connect it to the api. which is explained in this guide.

## Getting the Google Spreadsheet
[Google Sheet Templete](https://docs.google.com/spreadsheets/d/1vuRwyKBmP0qiYCc6NR9SaK-5cf0tuJ-JGlO0Zme_yMc/edit?usp=sharing)

To edit the spreadsheet you need to make a copy, `File` → `Make a Copy`

## Getting the API key
Once you made a copy of the spreadsheet you need to give the tool access.

To get your API key you need to give it access first.

1. Create a New Project  
    - Select a Project  
    - Create a New Project  
    - New Project 
    - Create
2. Get Google Drive Credentials
    - Search for Google Drive in the big top search bar
    - Enable Google Drive API
    - Create Credentials
    - Which API are you using? ``Google Drive API``
    - Where will you be calling the API from? ``Web server (e.g node.js, Tomgcat)`` 
    - What data will you be accessing? ``Application Data``
    - Are you planning to use this API with App Engine or Compute Engine? ``No, I'm not using them.``
    - Service account name? ``NuzlockeParty`` *can be anything*
    - Role? ``Project → Editor``
    - Continue
    - Download the file under ``%APPDATA%\gspread\service_account.json`` *create the folder gspread if it does not exist yet*
      Name it ``service_account.json``
3. Get Google Sheet Api
    - Search for Google Sheet API in the big top search bar
    - Enable Google Drive API
    
## Give the Client Access to the Google Sheet
  - Open the downloaded ``service_account.json`` file with any Editor
  - Copy the ``client_email``
  - Open your copy of the Google Spreadsheet
  - Share the Spreadsheet with that ``client_email`` as Editor
    
### Installation   


[gspread Authentication Documentation](https://gspread.readthedocs.io/en/latest/oauth2.html)
