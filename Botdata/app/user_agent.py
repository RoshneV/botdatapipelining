import requests
from bs4 import BeautifulSoup
from pymongo import UpdateOne
from app.mongodb import *


try:
    if user_agent_collection not in db.list_collection_names():
        collection = db.create_collection(user_agent_collection)
    else:
        collection = db[user_agent_collection]
        if not collection.index_information():
            collection.create_index([("cidr", "ascending")])
except Exception as e:
    print(f"Error connecting to MongoDB: {str(e)}")
def fetch_user_agents(urls, category):
    
    user_agents = []
    for url in urls:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        try:
            li_elements = soup.find_all('li', {'class': 'user-agent-li'})
                    #scarp the data
            for li in li_elements:
                user_agent = li.text.strip()
                user_agents.append(user_agent)
                user_agents_with_category = [{"user_agent": ua, "category": category} for ua in user_agents]
        except Exception as e:
            message=(f"Error scraping {url}: {str(e)}")
            post_to_slack(message)
    return user_agents_with_category

def bulk_update_user_agents(user_agents_with_category):
    try:
        requests_list=[]
            # To update  data in mongo
        for ua in user_agents_with_category:
                requests_list.append(UpdateOne({"user_agent": ua["user_agent"]}, {"$set": ua}, upsert=True))
        result = collection.bulk_write(requests_list)
    except Exception as e:
        message =f"Error in updating :{str(e)}"
        post_to_slack(message)
def adtrafficbot_ua():
    urls = [
            "https://deviceandbrowserinfo.com/data/user_agent/bot/Google%20AdsBot",
            "https://deviceandbrowserinfo.com/data/user_agent/bot/Google%20AdsBot%20mobile"    ]
    user_agents = fetch_user_agents(urls, "Ad Traffic Bot")
    bulk_update_user_agents(user_agents)

def archiving_bot_ua():
    urls = ["https://deviceandbrowserinfo.com/data/user_agent/bot/ia_archiver"]
    user_agents = fetch_user_agents(urls, "Archiving bot")
    bulk_update_user_agents(user_agents)

def crawler_ua():
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
    user_agents = fetch_user_agents(urls, "Crawler")
    bulk_update_user_agents(user_agents)

def scrapingbot_ua():
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
    user_agents = fetch_user_agents(urls, "Scraping Bot")
    bulk_update_user_agents(user_agents)

def socialmedia_bot_ua():
    urls = [
            "https://deviceandbrowserinfo.com/data/user_agent/bot/LinkedIn%20Bot",
            "https://deviceandbrowserinfo.com/data/user_agent/bot/Facebook%20external%20hit"
        ]
    user_agents = fetch_user_agents(urls, "Social Media Bot")
    bulk_update_user_agents(user_agents)

def socbot_ua():
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

    user_agents = fetch_user_agents(urls, "Soc Bot")
    bulk_update_user_agents(user_agents)
