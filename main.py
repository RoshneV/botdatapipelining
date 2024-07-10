from flask import Flask, jsonify, request
from dotenv import load_dotenv
import os
import requests
import logging
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

# ROUTES METHOD IMPORT
from botIPaddress import crawlersIP, DatacenterIP, socialmediabotIP, SocbotIP
from useragent import adtrafficbotUA, socialmedia_botUA, socbotUA, archiving_botUA, scrapingbotUA, crawlerUA

# LOAD ENV FILE
load_dotenv()

# INITIALIZE THE FLASK APP
app = Flask(__name__)

# GET ENV VARIABLES
PORT = os.environ.get('PORT')
SLACK_WEBHOOK_URL = os.environ.get('SLACK_WEBHOOK_URL')
SLACK_CHANNEL_CODE=os.environ.get('SLACK_CHANNEL_CODE')
LOG_FILE = os.environ.get('LOG_FILE')
Slackclient=WebClient(SLACK_WEBHOOK_URL)
# SET UP LOGGING
logging.basicConfig(filename=LOG_FILE, level=logging.INFO)

#CALLING ALL THE USERAGENT BOT CATEGORY
@app.route('/run_UA', methods=['GET'])
def run_UA():
    success=True
    try:
        crawlerUA()
        scrapingbotUA()
        adtrafficbotUA()
        socbotUA()
        archiving_botUA()
        socialmedia_botUA()
        logging.info("Useragent of bots stored successfully")
        Slackclient.chat_postMessage(channel=SLACK_CHANNEL_CODE,text='All UserAgent of bots updated successfully')
        return jsonify({'status': 'Useragent of bots stored successfully'})
    except Exception as e:
        logging.error(f"Error storing useragents: {str(e)}")
        print(e)
        Slackclient.chat_postMessage(channel=SLACK_CHANNEL_CODE,text=f"Error storing IP addresses: {str(e)}")
        return jsonify({'status': 'Error storing useragents'}), 500
# CALLING IP API TO RUN ALL IP CATGEORY BOTS
@app.route('/run_IP', methods=['GET'])
def run_IP():
    try:
        crawlersIP()
        DatacenterIP()
        socialmediabotIP()
        SocbotIP()
        #LOGGING  INFO
        logging.info("IP addresses of bots stored successfully")
        #SEND SUCCESS MESSAGE TO SLACK
        Slackclient.chat_postMessage("IP addresses of bots stored successfully")
        return jsonify({'status': 'IP addresses of bots stored successfully'})
    except Exception as e:
        #LOGGING ERROR
        logging.error(f"Error storing IP addresses: {str(e)}")
        print(e)
        #SEND ERROR MESSAGE TO SLACK
        Slackclient.chat_postMessage(channel=SLACK_CHANNEL_CODE,text=f"Error storing IP addresses: {str(e)}")
        return jsonify({'status': 'Error storing IP addresses'}), 500
# TO RUN TKE MAIN 
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=PORT)