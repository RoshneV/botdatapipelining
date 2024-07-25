from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import logging
# Import the env_loader module
from env_loader import load_env_variables

# Load the environment variables
env_vars = load_env_variables()

# Initialize MongoDB client
from pymongo import MongoClient

client = MongoClient(env_vars['MONGODBURL'])
db = client[env_vars['DB_NAME']]

bot_user_agent_collection = env_vars['bot_user_agent_collection']
bot_ip_collection = env_vars['bot_ip_collection']
legitimate_user_agent_collection = env_vars['legitimate_user_agent_collection']

# Initialize Slack client
slack_client = WebClient(token=env_vars['SLACK_WEBHOOK_URL'])

def post_to_slack(message):
    try:
        slack_client.chat_postMessage(channel=env_vars['SLACK_CHANNEL_CODE'], text=message)
        logging.info(message)
    except SlackApiError as e:
        print(f"Error posting to Slack: {e.response['error']}")
        logging.error(f"Error posting to Slack:{e.response['error']}")

