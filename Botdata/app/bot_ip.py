import requests
import pandas as pd
from pymongo import UpdateOne
from app.mongodb import db, bot_ip_collection
from app.mongodb import post_to_slack
try:
    if bot_ip_collection not in db.list_collection_names():
        collection = db.create_collection(bot_ip_collection)
    else:
        collection = db[bot_ip_collection]
        if not collection.index_information():
            collection.create_index([("cidr", "ascending")])
except Exception as e:
    message=f"Error connecting to MongoDB: {str(e)}"
    post_to_slack(message)

def fetch_bot_ips(urls, category):
    ip_data_with_set = []
    for url in urls:
        res = requests.get(url)
        df = pd.DataFrame(res.text.strip().split('\n'), columns=['cidr'])
        df = df[~df.iloc[:, 0].str.startswith('#')]
        df = df[~df.iloc[:, 0].str.startswith(" ")]
        
        try:
            for ip in df['cidr']:
                data_dict = {}
                if '/' in ip:
                    data_dict['cidr'] = ip
                else:
                    if ':' in ip:  # Check if it's an IPv6 address
                        ip += '/128'  # Convert IPv6 to CIDR notation by adding /128
                    else:  # It's an IPv4 address
                        ip += '/32'  # Convert IPv4 to CIDR notation by adding /32
                
                data_dict['cidr'] = ip
                data_dict['category'] = category
                ip_data_with_set.append({"cidr": ip, "data_dict": data_dict})
        except Exception as e:
            message=(f"Error scraping {url}: {str(e)}")
            post_to_slack(message)
    return ip_data_with_set

def bulk_update_bot_ips(ip_data_with_set):
    try:
        operations = [UpdateOne({"cidr": entry["cidr"]}, {"$set": entry["data_dict"]}, upsert=True) for entry in ip_data_with_set]
        result = collection.bulk_write(operations)
    except Exception as e:
        message=f"Error updating :{str(e)}"
        post_to_slack(message)

def data_center_ip():
    urls = [
        "https://raw.githubusercontent.com/AnTheMaker/GoodBots/main/iplists/cloudflare.ips",
        "https://raw.githubusercontent.com/AnTheMaker/GoodBots/main/iplists/bunnycdn.ips"
    ]
    bot_ips = fetch_bot_ips(urls, "Data center bot")
    bulk_update_bot_ips(bot_ips)

def crawler_ip():
    urls = ["https://myip.ms/files/bots/live_webcrawlers.txt"]
    bot_ips = fetch_bot_ips(urls, "Crawler")
    bulk_update_bot_ips(bot_ips)

def socialmedia_bot_ip():
    urls = [
        "https://raw.githubusercontent.com/AnTheMaker/GoodBots/main/iplists/twitterbot.ips",
        "https://raw.githubusercontent.com/AnTheMaker/GoodBots/main/iplists/telegrambot.ips",
        "https://raw.githubusercontent.com/AnTheMaker/GoodBots/main/iplists/facebookbot.ips"
    ]
    bot_ips = fetch_bot_ips(urls, "Social Media Bot")
    bulk_update_bot_ips(bot_ips)

def socbot_ip():
    urls = [
        "https://raw.githubusercontent.com/AnTheMaker/GoodBots/main/iplists/ahrefsbot.ips",
        "https://raw.githubusercontent.com/AnTheMaker/GoodBots/main/iplists/applebot.ips",
        "https://raw.githubusercontent.com/AnTheMaker/GoodBots/main/iplists/bingbot.ips",
        "https://raw.githubusercontent.com/AnTheMaker/GoodBots/main/iplists/duckduckbot.ips",
        "https://raw.githubusercontent.com/AnTheMaker/GoodBots/main/iplists/googlebot.ips",
        "https://raw.githubusercontent.com/AnTheMaker/GoodBots/main/iplists/mojeekbot.ips"
    ]
    bot_ips = fetch_bot_ips(urls, "Soc Bot")
    bulk_update_bot_ips(bot_ips)
