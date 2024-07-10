from flask import request,jsonify,json
import os
import requests
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient,UpdateOne
# LOAD ENV FIELS
load_dotenv()

# GET ENV VARIABLES
URL = os.environ.get('MONGODBURL')
DATABASENAME = os.environ.get('COLLECTIONNAME')
PORT = os.environ.get('PORT')
Dbname=os.environ.get('DBNAME1')

# CONNECT TO MONGODB
try:
    client = MongoClient(URL)
    db = client[DATABASENAME]
    if Dbname not in db.list_collection_names():
        collection = db.create_collection(Dbname)
    else:
        collection = db[Dbname]
        if not collection.index_information():
            collection.create_index([("cidr", "ascending")])
except Exception as e:
    print(f"Error connecting to MongoDB: {str(e)}")
# STORE ADTRAFFICBOT USERAGENT
def adtrafficbotUA():
    try:
        #URL COLLECTION
        urls = [
            "https://deviceandbrowserinfo.com/data/user_agent/bot/Google%20AdsBot",
            "https://deviceandbrowserinfo.com/data/user_agent/bot/Google%20AdsBot%20mobile",
            "https://user-agents.net/bots/amazon-cloudfront"
        ]
        
        user_agents = []
        # Send requests and get responses
        for url in urls:
                # print("user")
                response = requests.get(url)
                soup = BeautifulSoup(response.text, 'html.parser')
                
                # Find the ul element with li elements that have class "user-agent-li" as that consists of useragent list 
                try:
                    li_elements = soup.find_all('li', {'class': 'user-agent-li'})
                    #scarp the data
                    for li in li_elements:
                        user_agent = li.text.strip()
                        user_agents.append(user_agent)
                except Exception as e:
                    print(f"Error running {str(e)}")
                    success = False
            
        user_agents_with_category = [{"user_agent": ua, "category": "Ad Traffic Bot"} for ua in user_agents]
        requests_list = [] 
         # To update  data in mongo
        for ua in user_agents_with_category:
            requests_list.append(UpdateOne({"user_agent": ua["user_agent"]}, {"$set": ua}, upsert=True))
        result = collection.bulk_write(requests_list)
    except Exception as e:
        print(f"Error in adtrafficbot useragent: {str(e)}")

def archiving_botUA():
    try:
        urls = ["https://deviceandbrowserinfo.com/data/user_agent/bot/ia_archiver"]

        user_agents = []

        # Send requests and get responses
        for url in urls:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            # Find the ul element with li elements that have class "user-agent-li"
            try:
                li_elements = soup.find_all('li', {'class': 'user-agent-li'})
                #scarp the data
                for li in li_elements:
                    user_agent = li.text.strip()
                    user_agents.append(user_agent)
            except Exception as e:
                print(f"Error running {str(e)}")
                success = False
        user_agents_with_category = [{"user_agent": ua, "category": "Archiving bot"} for ua in user_agents]
        requests_list = []
        #TO UPDATE MONGODB
        for ua in user_agents_with_category:
            requests_list.append(UpdateOne({"user_agent": ua["user_agent"]}, {"$set": ua}, upsert=True))
        result = collection.bulk_write(requests_list)
    except Exception as e:
        print(f"Error in archivingbotUA: {str(e)}")


def crawlerUA():
    try:
        urls = [
            "https://deviceandbrowserinfo.com/data/user_agent/bot/Google%20APIs",
            "https://deviceandbrowserinfo.com/data/user_agent/bot/Google%20Inspection%20Tool",
            "https://deviceandbrowserinfo.com/data/user_agent/bot/Audisto%20Crawler",
            "https://deviceandbrowserinfo.com/data/user_agent/bot/PHPCrawl",
            "https://deviceandbrowserinfo.com/data/user_agent/bot/FAST-WebCrawler",
            "https://deviceandbrowserinfo.com/data/user_agent/bot/FAST%20Enterprise%20Crawler",
            "https://deviceandbrowserinfo.com/data/user_agent/bot/CCBot%20(Common%20crawl)",
            "https://deviceandbrowserinfo.com/data/user_agent/bot/Criteo%20crawler",
            "https://deviceandbrowserinfo.com/data/user_agent/bot/BrightEdge%20Crawler"
            # Add more URLs to the list if required
        ]
        user_agents = []

        # Send requests and get responses
        for url in urls:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            # Find the ul element with li elements that have class "user-agent-li"
            try:
                li_elements = soup.find_all('li', {'class': 'user-agent-li'})
                #scarp the data
                for li in li_elements:
                    user_agent = li.text.strip()
                    user_agents.append(user_agent)
            except Exception as e:
                print(f"Error running {str(e)}")
                success = False
        
        user_agents_with_category = [{"user_agent": ua, "category": "Crawler"} for ua in user_agents]
        requests_list = []
        # To bulk write the data
        for ua in user_agents_with_category:
            requests_list.append(UpdateOne({"user_agent": ua["user_agent"]}, {"$set": ua}, upsert=True))
        result = collection.bulk_write(requests_list)
    except Exception as e:
        print(f"Error in crawlerUA: {str(e)}")


def scrapingbotUA():
    try:
        urls = [
            "https://deviceandbrowserinfo.com/data/user_agent/bot/Python%20requests",
            "https://deviceandbrowserinfo.com/data/user_agent/bot/HTTPX",
            "https://deviceandbrowserinfo.com/data/user_agent/bot/Node%20fetch",
            "https://deviceandbrowserinfo.com/data/user_agent/bot/Curl",
            "https://deviceandbrowserinfo.com/data/user_agent/bot/HTTrack%20website%20copier",
            "https://deviceandbrowserinfo.com/data/user_agent/bot/libwww-perl",
            "https://deviceandbrowserinfo.com/data/user_agent/bot/Wget",
            "https://deviceandbrowserinfo.com/data/user_agent/bot/Urllib",
            "https://deviceandbrowserinfo.com/data/user_agent/bot/AIOHTTP",
            "https://deviceandbrowserinfo.com/data/user_agent/bot/HttpUnit",
            "https://deviceandbrowserinfo.com/data/user_agent/bot/Go%20HTTP%20client",
            "https://deviceandbrowserinfo.com/data/user_agent/bot/TurnitinBot"
            # Add more URLs to the list
        ]

        user_agents = []

        # Send requests and get responses
        for url in urls:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            # rint(soup)
            # Find the ul element with li elements that have class "user-agent-li"
            try:
                li_elements = soup.find_all('li', {'class': 'user-agent-li'})
                #scarp the data
                for li in li_elements:
                    user_agent = li.text.strip()
                    user_agents.append(user_agent)
            except Exception as e:
                print(f"Error running {str(e)}")
                success = False
        user_agents_with_category = [{"user_agent": ua, "category": "scraper"} for ua in user_agents]
        requests_list = []
        for ua in user_agents_with_category:
            requests_list.append(UpdateOne({"user_agent": ua["user_agent"]}, {"$set": ua}, upsert=True))
        result = collection.bulk_write(requests_list)
    except Exception as e:
        print(f"Error in scrapingbotUA: {str(e)}")

def socbotUA():
    try:
        urls = [
            "https://deviceandbrowserinfo.com/data/user_agent/bot/Google%20bot",    "https://deviceandbrowserinfo.com/data/user_agent/bot/HTTPX",
            "https://deviceandbrowserinfo.com/data/user_agent/bot/Google%20bot%20mobile",
            "https://deviceandbrowserinfo.com/data/user_agent/bot/Google%20Feedfetcher",
            "https://deviceandbrowserinfo.com/data/user_agent/bot/BingBot",
            "https://deviceandbrowserinfo.com/data/user_agent/bot/Buzzbot",
            "https://deviceandbrowserinfo.com/data/user_agent/bot/YandexBot",
            "https://deviceandbrowserinfo.com/data/user_agent/bot/GPTBot",
            "https://deviceandbrowserinfo.com/data/user_agent/bot/PerplexityBot",
            "https://deviceandbrowserinfo.com/data/user_agent/bot/Linguee%20Bot",
            "https://deviceandbrowserinfo.com/data/user_agent/bot/DataForSeoBot",
            "https://deviceandbrowserinfo.com/data/user_agent/bot/yacybot",
            "https://deviceandbrowserinfo.com/data/user_agent/bot/Bytespider",
            "https://deviceandbrowserinfo.com/data/user_agent/bot/Slurp"
            
            # Add more URLs to the list
        ]

        user_agents = []

        # Send requests and get responses
        for url in urls:
            # print("user")
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            # rint(soup)
            # Find the ul element with li elements that have class "user-agent-li"
            try:
                li_elements = soup.find_all('li', {'class': 'user-agent-li'})
                #scarp the data
                for li in li_elements:
                    user_agent = li.text.strip()
                    user_agents.append(user_agent)
            except Exception as e:
                print(f"Error running {str(e)}")
                success = False
        user_agents_with_category = [{"user_agent": ua, "category": "SOC bot"} for ua in user_agents]
        requests_list = []
        for ua in user_agents_with_category:
            requests_list.append(UpdateOne({"user_agent": ua["user_agent"]}, {"$set": ua}, upsert=True))
        result = collection.bulk_write(requests_list)
    except Exception as e:
        print(f"Error in socbotUA: {str(e)}")


def socialmedia_botUA():
    try:
        urls = [
            "https://deviceandbrowserinfo.com/data/user_agent/bot/LinkedIn%20Bot",
            "https://deviceandbrowserinfo.com/data/user_agent/bot/Facebook%20external%20hit"
        ]

        user_agents = []

        # Send requests and get responses
        for url in urls:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            # Find the ul element with li elements that have class "user-agent-li"
            try:
                li_elements = soup.find_all('li', {'class': 'user-agent-li'})
                #scarp the data
                for li in li_elements:
                    user_agent = li.text.strip()
                    user_agents.append(user_agent)
            except Exception as e:
                print(f"Error running {str(e)}")
                success = False

        # print(user_agents)
        user_agents_with_category = [{"user_agent": ua, "category": "Social Media Bots"} for ua in user_agents]
        requests_list = []
        # To append the data 
        for ua in user_agents_with_category:
            requests_list.append(UpdateOne({"user_agent": ua["user_agent"]}, {"$set": ua}, upsert=True))
        result = collection.bulk_write(requests_list)
    except Exception as e:
        print(f"Error in socialmediabotUA: {str(e)}")
