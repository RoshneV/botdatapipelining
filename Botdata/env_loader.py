import os
from dotenv import load_dotenv

def load_env_variables():
    load_dotenv()
    return {
        'MONGODBURL': os.getenv('MONGODBURL'),
        'DB_NAME': os.getenv('DB_NAME'),
        'bot_user_agent_collection': os.getenv('bot_user_agent_collection'),
        'legitimate_user_agent_collection': os.getenv('legitimate_user_agent_collection'),
        'bot_ip_collection': os.getenv('bot_ip_collection'),
        'SLACK_WEBHOOK_URL': os.getenv('SLACK_WEBHOOK_URL'),
        'SLACK_CHANNEL_CODE': os.getenv('SLACK_CHANNEL_CODE'),
        'PORT':os.getenv('PORT'),
        'LOG_FILE':os.getenv('LOG_FILE')
    }