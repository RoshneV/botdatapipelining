import requests
from bs4 import BeautifulSoup
from pymongo import UpdateOne
from app.mongodb import *
import logging
try:
    if legitimate_user_agent_collection not in db.list_collection_names():
        collection = db.create_collection(legitimate_user_agent_collection)
    else:
        collection = db[legitimate_user_agent_collection]
        if not collection.index_information():
            collection.create_index([("user_agent", "ascending")])
except Exception as e:
    print(f"Error connecting to MongoDB: {str(e)}")
    message=f"Error connecting to MongoDB:{str(e)}"
    post_to_slack(message)
    logging.error(f"Error connecting to MongoDB:{str(e)}")
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
            logging.error(message)
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
        logging.error(message)
def windows():
    urls = ["https://deviceandbrowserinfo.com/data/user_agent/human/Windows;;Firefox","https://deviceandbrowserinfo.com/data/user_agent/human/Windows;;Chrome","https://deviceandbrowserinfo.com/data/user_agent/human/Windows;;Edge",
            "https://deviceandbrowserinfo.com/data/user_agent/human/Windows;;Yandex","https://deviceandbrowserinfo.com/data/user_agent/human/Windows;;Opera","https://deviceandbrowserinfo.com/data/user_agent/human/Windows;;Vivaldi", ]
    user_agents = fetch_user_agents(urls, "Windows")
    bulk_update_user_agents(user_agents)

def mac():
    urls = ["https://deviceandbrowserinfo.com/data/user_agent/human/Mac%20OS;;Chrome","https://deviceandbrowserinfo.com/data/user_agent/human/Mac%20OS;;Edge","https://deviceandbrowserinfo.com/data/user_agent/human/Mac%20OS;;Firefox","https://deviceandbrowserinfo.com/data/user_agent/human/Mac%20OS;;Safari",
            "https://deviceandbrowserinfo.com/data/user_agent/human/Mac%20OS;;Yandex","https://deviceandbrowserinfo.com/data/user_agent/human/Mac%20OS;;Mobile%20Safari","https://deviceandbrowserinfo.com/data/user_agent/human/Mac%20OS;;Opera"]
    user_agents = fetch_user_agents(urls, "Mac OS")
    bulk_update_user_agents(user_agents)

def android():
    urls = [
            "https://deviceandbrowserinfo.com/data/user_agent/human/Android;;Chrome","https://deviceandbrowserinfo.com/data/user_agent/human/Android;;Firefox","https://deviceandbrowserinfo.com/data/user_agent/human/Android;;Opera","https://deviceandbrowserinfo.com/data/user_agent/human/Android;;Yandex","https://deviceandbrowserinfo.com/data/user_agent/human/Android;;Android%20Browser","https://deviceandbrowserinfo.com/data/user_agent/human/Android;;Edge"
            # Add more URLs to the list if required
        ]
    user_agents = fetch_user_agents(urls, "Android")
    bulk_update_user_agents(user_agents)

def ios():
    urls = [
            "https://deviceandbrowserinfo.com/data/user_agent/human/iOS;;Mobile%20Safari","https://deviceandbrowserinfo.com/data/user_agent/human/iOS;;Chrome","https://deviceandbrowserinfo.com/data/user_agent/human/iOS;;Edge","https://deviceandbrowserinfo.com/data/user_agent/human/iOS;;Firefox","https://deviceandbrowserinfo.com/data/user_agent/human/iOS;;Yandex"
            # Add more URLs to the list
        ]
    user_agents = fetch_user_agents(urls, "iOS")
    bulk_update_user_agents(user_agents)

def linux():
    urls = [
            "https://deviceandbrowserinfo.com/data/user_agent/human/Linux;;Chrome",
            "https://deviceandbrowserinfo.com/data/user_agent/human/Linux;;Firefox",
        "https://deviceandbrowserinfo.com/data/user_agent/human/Ubuntu;;Firefox",
        "https://deviceandbrowserinfo.com/data/user_agent/human/Ubuntu;;Chromium","https://deviceandbrowserinfo.com/data/user_agent/human/Linux;;Edge","https://deviceandbrowserinfo.com/data/user_agent/human/Linux;;Yandex","https://deviceandbrowserinfo.com/data/user_agent/human/Linux;;Opera","https://deviceandbrowserinfo.com/data/user_agent/human/Chromium%20OS;;Chrome","https://deviceandbrowserinfo.com/data/user_agent/human/Fedora;;Firefox"]
    user_agents = fetch_user_agents(urls, "linux")
    bulk_update_user_agents(user_agents)

