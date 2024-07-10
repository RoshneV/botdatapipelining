from flask import request, jsonify, json
import os
import requests
from dotenv import load_dotenv
import pandas as pd
from bs4 import BeautifulSoup
from pymongo import MongoClient, UpdateOne

# LOAD ENV FIELS
load_dotenv()

# GET ENV VARIABLES
URL = os.environ.get('MONGODBURL')
DATABASENAME = os.environ.get('DATABASENAME')
PORT = os.environ.get('PORT')
Dbname = os.environ.get('DBNAME2')

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
# TO STORE CRAWLERS IP ADDRESS 
def crawlersIP():
    try:
        #
        urls = ["https://myip.ms/files/bots/live_webcrawlers.txt"]
        for url in urls:
            res = requests.get(url)
            df = pd.DataFrame(res.text.strip().split('\n'), columns=['cidr'])
            df = df[~df.iloc[:, 0].str.startswith('#')]
            operations = []
            i = 0
            for ip in df['cidr']:
                i += 1
                data_dict = {}
                if '/' in ip:
                    data_dict['cidr'] = ip
                    data_dict['category'] = "Crawlers"
                    operation = UpdateOne({'cidr': ip}, {'$set': data_dict}, upsert=True)
                    operations.append(operation)
                else:
                    ip += '/32'  # convert IP to CIDR notation by adding /32
                    print(ip)
                    data_dict['cidr'] = ip
                    data_dict['category'] = "Crawlers"
                    operation = UpdateOne({'cidr': ip}, {'$set': data_dict}, upsert=True)
                    operations.append(operation)
            result = collection.bulk_write(operations)
    except Exception as e:
        print(f"Error in crawlersIP: {str(e)}")
# TO STORE DATACENTER IP ADDRESS
def DatacenterIP():
    try:
        urls = ["https://raw.githubusercontent.com/AnTheMaker/GoodBots/main/iplists/cloudflare.ips","https://raw.githubusercontent.com/AnTheMaker/GoodBots/main/iplists/bunnycdn.ips"]
        for url in urls:
            res = requests.get(url)
            df = pd.DataFrame(res.text.strip().split('\n'), columns=['cidr'])
            operations = []
            i = 0
            for ip in df['cidr']:
                i += 1
                data_dict = {}  
                if '/' in ip:
                    data_dict['cidr'] = ip
                    data_dict['category'] = "Data Center Bots"
                    operation = UpdateOne({'cidr': ip}, {'$set': data_dict}, upsert=True)
                    operations.append(operation)
                else:
                    ip += '/32'  # convert IP to CIDR notation by adding /32
                    print(ip)
                    data_dict['cidr'] = ip
                    data_dict['category'] = "Data Center Bots"
                    operation = UpdateOne({'cidr': ip}, {'$set': data_dict}, upsert=True)
                    operations.append(operation)
            result = collection.bulk_write(operations)
    except Exception as e:
        print(f"Error in DatacenterIP: {str(e)}")
#TO STORE SOC BOT IP ADDRESS
def SocbotIP():
    try:
        urls = ["https://raw.githubusercontent.com/AnTheMaker/GoodBots/main/iplists/ahrefsbot.ips","https://raw.githubusercontent.com/AnTheMaker/GoodBots/main/iplists/applebot.ips","https://raw.githubusercontent.com/AnTheMaker/GoodBots/main/iplists/bingbot.ips","https://raw.githubusercontent.com/AnTheMaker/GoodBots/main/iplists/duckduckbot.ips","https://raw.githubusercontent.com/AnTheMaker/GoodBots/main/iplists/googlebot.ips","https://raw.githubusercontent.com/AnTheMaker/GoodBots/main/iplists/mojeekbot.ips"]
        for url in urls:
            res = requests.get(url)
            df = pd.DataFrame(res.text.strip().split('\n'), columns=['cidr'])
            operations = []
            i = 0
            for ip in df['cidr']:
                i += 1
                data_dict = {}
                if '/' in ip:
                    data_dict['cidr'] = ip
                    data_dict['category'] = "soc bot"
                    operation = UpdateOne({'cidr': ip}, {'$set': data_dict}, upsert=True)
                    operations.append(operation)
                else:
                   ip += '/32'  # convert IP to CIDR notation by adding /32
#                print(ip)
                data_dict['cidr'] = ip
                data_dict['category'] = "soc bot"
                operation = UpdateOne({'cidr': ip}, {'$set': data_dict}, upsert=True)
                operations.append(operation)
        result=collection.bulk_write(operations)
    except Exception as e:
        print(f"Error in SocbotIP: {str(e)}")
#TO STORE SOCIAL MEDIA IP ADDRESS
def socialmediabotIP():
    try:
        urls = [
            "https://deviceandbrowserinfo.com/data/user_agent/bot/LinkedIn%20Bot",
            "https://deviceandbrowserinfo.com/data/user_agent/bot/Facebook%20external%20hit"
        ]

        user_agents = []

        # Send requests and get responses
        for url in urls:
            for url in urls:
                res = requests.get(url)
                df = pd.DataFrame(res.text.strip().split('\n'), columns=['cidr'])
                operations = []
                i = 0
                for ip in df['cidr']:
                    i += 1
                    data_dict = {}
                    if '/' in ip:
                        data_dict['cidr'] = ip
                        data_dict['category'] = "social media bot"
                        operation = UpdateOne({'cidr': ip}, {'$set': data_dict}, upsert=True)
                        operations.append(operation)
                    else:
                        ip += '/32'  # convert IP to CIDR notation by adding /32
    #                print(ip)
                    data_dict['cidr'] = ip
                    data_dict['category'] = "social media bot"
                    operation = UpdateOne({'cidr': ip}, {'$set': data_dict}, upsert=True)
                    operations.append(operation)
            result=collection.bulk_write(operations)
    except Exception as e:
        print(f"Error in SocialMediaIP: {str(e)}")
