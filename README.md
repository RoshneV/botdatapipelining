**Datas scraped from**:
	https://deviceandbrowserinfo.com/data/user_agents 
	https://github.com/AnTheMaker/GoodBots/tree/main/iplists 

**Language used**: Python

**Framework used**: Flask

**Libraries used**: pandas,BeautifulSoup,requests

**__init__.py**
	In this code snippet flask is been initialised which is connected to routes
routes.py
           In this file the initialise the route to useragent file and ip address file which connects to http url which creates the 

**mongodb.py**
-Checks if the specified collection exists in the MongoDB database.
-Creates the collection if it doesn't exist.
-Ensures there is an index on the cidr field for efficient querying.
-Handles exceptions during connection and setup.
bot_ip.py
**fetch_bot_ips**
-Sends a GET request to each URL to fetch IP data.
-Converts the response text into a DataFrame for easier manipulation.
-Filters out commented lines and unnecessary whitespace.
-Converts plain IP addresses to CIDR notation (IPv4 to /32 and IPv6 to /128).-
-Prepares the data in a format suitable for bulk writing to MongoDB.
**bulk_update_bot_ips**
Creates UpdateOne operations for each IP address and its data.
Executes the bulk write operation to update the database.
**Bot Category Functions**
Each function defines a specific category of bots and uses the fetch_bot_ips and bulk_update_bot_ips functions to process and store their IP addresses.The categorise are data center,crawler, social media bot,soc bot
**useragent.py**
**fetch_user_agents**
Sends a GET request to each URL to fetch user agent data.
Parses the HTML content using BeautifulSoup.
Extracts user agent strings from the <li> elements with class user-agent-li.
Prepares the data in a format suitable for bulk writing to MongoDB.
Handles exceptions during data scraping, logs errors, and posts error messages to Slack.
**bulk_update_user_agents**
-Performs a bulk update operation to insert or update user agent strings in MongoDB.
**user_agents_with_category**: 
Each function defines a specific category of user agents and uses the fetch_user_agents and bulk_update_user_agents functions to process and store them.The useragent categorise are soc bot, data centre bot, crawler bot, social media bot, scraper,ad fraud bot, archiving bot
