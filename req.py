import requests
import json
from typing import List, Optional
from ad_data import AdData


def get_response(url, params) -> requests.Response:
    session = requests.Session()
    return session.get(url, params=params)
   

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
    return [AdData.from_dict(item) for item in feed_items]

