from flask import Flask, jsonify
from app.mongodb import post_to_slack
from app.user_agent import (
    adtrafficbot_ua,
    archiving_bot_ua,
    crawler_ua,
    scrapingbot_ua,
    socialmedia_bot_ua,
    socbot_ua
)
from app.bot_ip import (
    crawler_ip,
    data_center_ip,
    socialmedia_bot_ip,
    socbot_ip
)

app = Flask(__name__)

@app.route('/update_user_agents', methods=['GET'])
def update_user_agents():
    adtrafficbot_ua()
    archiving_bot_ua()
    crawler_ua()
    scrapingbot_ua()
    socialmedia_bot_ua()
    socbot_ua()
    message=f"User agents updated successfully"
    post_to_slack(message)
    return jsonify({"message": "User agents updated successfully"}), 200

@app.route('/update_bot_ips', methods=['GET'])
def update_bot_ips():
    crawler_ip()
    data_center_ip()
    socialmedia_bot_ip()
    socbot_ip()
    message=f"IP addresses updated successfully"
    post_to_slack(message)
    return jsonify({"message": "Bot IPs updated successfully"}), 200

if __name__ == '__main__':
    app.run(debug=True)
