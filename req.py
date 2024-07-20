import requests
import json
from typing import List, Optional
from ad_data import AdData
import random
from datetime import datetime

#Set a random user agent for the request ou of a lis of 10 popular user agents
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.3",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.3",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.3",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.3"
]

# user_agent = random.choice(user_agents)
# user_agent =
 
def get_response(url, params) -> requests.Response:
    session = requests.Session()
    user_agent = random.choice(user_agents)
    # headers = {'User-Agent': user_agent}

    return session.get(url, params=params)
    # return session.get(url, params=params, headers=headers)


def parse_response(response_text: str) -> Optional[List[AdData]]:
    try:
        data = json.loads(response_text)
    except json.JSONDecodeError as e:
        print(f"Failed to parse JSON: {e}")
        return None
    
    # Extract and process only feed_items
    feed_items = data.get('feed', {}).get('feed_items', [])
    # Keep only actual places
    feed_items = [item for item in feed_items if 'order_type_id' in item]
    ads = [AdData.from_dict(item) for item in feed_items]
    # Sort ads by ads.date_added (most recent first)
    ads.sort(key=lambda ad: datetime.strptime(ad.date_added, '%d/%m/%Y'), reverse=True)
    return ads

