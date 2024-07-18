Datas scraped from:
	https://deviceandbrowserinfo.com/data/user_agents 
	https://github.com/AnTheMaker/GoodBots/tree/main/iplists 

Language used: Python

Framework used: Flask

Libraries used: pandas,BeautifulSoup,requests

Data directory:

BOTDATA/
│
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── bot_ip.py
│   ├── user_agent.py
│   └── mongodb.py
├── .env
├── env_loader.py
└── run.py

__init__.py
	In this code snippet flask is been initialised which is connected to routes
routes.py
           In this file the initialise the route to useragent file and ip address file which connects to http url which creates the 

mongodb.py
MongoDB Collection Initialization:
Checks if the specified collection exists in the MongoDB database.
Creates the collection if it doesn't exist.
Ensures there is an index on the cidr field for efficient querying.
Handles exceptions during connection and setup.
bot_ip.py
fetch_bot_ips
Purpose: Fetches IP addresses from given URLs, processes them, and prepares them for bulk insertion into MongoDB.
Parameters:
urls: List of URLs to fetch the IP addresses from.
category: The category to which these IP addresses belong (e.g., "Data Center Bots", "Crawler").
Returns:
A list of dictionaries, each containing an IP address (cidr) and its associated data (data_dict).
Processing Steps:
Sends a GET request to each URL to fetch IP data.
Converts the response text into a DataFrame for easier manipulation.
Filters out commented lines and unnecessary whitespace.
Converts plain IP addresses to CIDR notation (IPv4 to /32 and IPv6 to /128).
Prepares the data in a format suitable for bulk writing to MongoDB.
bulk_update_bot_ips
Purpose: Performs a bulk update operation to insert or update IP addresses in MongoDB.
Parameters:
ip_data_with_set: List of dictionaries containing IP addresses and associated data prepared by fetch_bot_ips.
Operation:
Creates UpdateOne operations for each IP address and its data.
Executes the bulk write operation to update the database.
Bot Category Functions
Each function defines a specific category of bots and uses the fetch_bot_ips and bulk_update_bot_ips functions to process and store their IP addresses.The categorise are data center,crawler, social media bot,soc bot
useragent.py
fetch_user_agents
Purpose: Fetches user agent strings from given URLs, processes them, and prepares them for bulk insertion into MongoDB.
Parameters:
urls: List of URLs to fetch the user agent strings from.
category: The category to which these user agent strings belong (e.g., "Ad Traffic Bot", "Crawler").
Returns:
A list of dictionaries, each containing a user agent string and its associated category.
Processing Steps:
Sends a GET request to each URL to fetch user agent data.
Parses the HTML content using BeautifulSoup.
Extracts user agent strings from the <li> elements with class user-agent-li.
Prepares the data in a format suitable for bulk writing to MongoDB.
Handles exceptions during data scraping, logs errors, and posts error messages to Slack.

bulk_update_user_agents
Purpose: Performs a bulk update operation to insert or update user agent strings in MongoDB.
Parameters:
user_agents_with_category: List of dictionaries containing user agent strings and associated categories prepared by fetch_user_agents.
Operation:
Creates UpdateOne operations for each user agent string and its category.
Executes the bulk write operation to update the database.
Handles exceptions during the update process, logs errors, and posts error messages to Slack.
User Agent Category Functions
Each function defines a specific category of user agents and uses the fetch_user_agents and bulk_update_user_agents functions to process and store them.The useragent categorise are soc bot, data centre bot, crawler bot, social media bot, scraper,ad fraud bot, archiving bot
