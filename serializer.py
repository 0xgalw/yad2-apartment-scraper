from ad_data import AdData
from typing import List, Tuple
from geopy.distance import geodesic


def serialize_data(ads: List[AdData], starting_point: Tuple[int, int]) -> str:
    """
    Serialize the list of AdData objects into a string message
    """
    # First lines of the message are a summary of the ads
    # i.e a dotted list 1. address, price, updated_at
    summary_lines = []
    for i, ad in enumerate(ads, start=1):
        summary_lines.append(f"{i}. {ad.street} {ad.address_home_number}, {ad.price}, {ad.updated_at}")
    
    # Then we add the details of each ad, title, link, price, date_added, geo_distance
    details_lines = []
    for i, ad in enumerate(ads, start=1):
        distance = geodesic(starting_point, (ad.coordinates['latitude'], ad.coordinates['longitude'])).meters
        details_lines.append(f"{i}. {ad.street} {ad.address_home_number} - {ad.price} \n התווסף ב {ad.date_added}\n {ad.updated_at}\nמרחק {distance:.2f}m\n {ad.link}")
                             
    
    # Combine the summary and details into a single message
    summary = "\n".join(summary_lines)
    details = "\n\n".join(details_lines)
    return f"{summary}\n\n{details}"
    
    
