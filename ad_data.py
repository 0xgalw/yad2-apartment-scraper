from datetime import datetime
from dataclasses import dataclass
from typing import Optional, Dict

@dataclass
class AdData:
    price: Optional[str]
    image_url: Optional[str]
    coordinates: dict
    title_1: Optional[str]
    title_2: Optional[str]
    updated_at: Optional[str]
    date_added: Optional[str]
    street: Optional[str]
    address_home_number: Optional[str]
    contact_name: Optional[str]
    link: Optional[str] = None

    @classmethod
    def from_dict(cls, ad_dict: Dict) -> 'AdData':
        return cls(
            price=ad_dict.get('price'),
            image_url=ad_dict.get('images_urls')[0] if ad_dict.get('images_urls') else None,
            coordinates=ad_dict.get('coordinates'),
            title_1=ad_dict.get('title_1'),
            title_2=ad_dict.get('title_2'),
            updated_at=ad_dict.get('updated_at'),
            date_added= datetime.strptime(ad_dict.get('date_added'), '%Y-%m-%d %H:%M:%S').strftime('%d/%m/%Y') if ad_dict.get('date_added') else None,
            street=ad_dict.get('street'),
            address_home_number=ad_dict.get('address_home_number'),
            contact_name=ad_dict.get('contact_name'),
            link=f"https://www.yad2.co.il/realestate/item/{ad_dict.get('link_token')}"
        )

# # Creating an instance of the dataclass using the class method
# ad_data_instance = AdData.from_dict(ad_dict)
# print(ad_data_instance)
