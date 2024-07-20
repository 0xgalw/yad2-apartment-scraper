from ad_data import AdData
from typing import List, Tuple
from geopy.distance import geodesic

from cache import local_cache, save_cache_to_file

def serialize_data(ads: List[AdData], starting_point: Tuple[int, int], num_ads=10) -> str:
    """
    Serialize the list of AdData objects into a string message
    """
    # First lines of the message are a summary of the ads
    # i.e a dotted list 1. address, price, updated_at
    global local_cache
    summary_lines = []
    
    ads= [ad for ad in ads if ad.link not in local_cache]
    ads = ads[:num_ads]
    
    for i, ad in enumerate(ads, start=1):
        summary_lines.append(f"{i}. {ad.street} {ad.address_home_number}, {ad.price}, {ad.updated_at}")
    
    # Then we add the details of each ad, title, link, price, date_added, geo_distance
    details_lines = []
    for i, ad in enumerate(ads, start=1):
        distance = geodesic(starting_point, (ad.coordinates['latitude'], ad.coordinates['longitude'])).meters
        details_lines.append(f"{i}. {ad.street} {ad.address_home_number} - {ad.price} \n התווסף ב {ad.date_added}\n {ad.updated_at}\nמרחק {distance:.2f}m\n {ad.link}")
    
    # Update the local cache with the new links
    local_cache.update({ad.link for ad in ads})
    save_cache_to_file()
    
    # Combine the summary and details into a single message
    summary = "\n".join(summary_lines)
    details = "\n\n".join(details_lines)
    return f"{summary}\n\n{details}"
    
    
