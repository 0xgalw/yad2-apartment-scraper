import time
import random
import cache
from req import get_response, parse_response
from serializer import serialize_data
from telegram_bot import send_message

# CENTER_POINT = (32.092854269221746, 34.78229929820614)
CENTER_POINT = (32.06793624793461, 34.76624377643179)
DISTANCE = 400
URL = "https://www.yad2.co.il/api/feed/get"

# params = {
#     "cat": 2,
#     "subcat": 2,
#     "property": 30,
#     "z": 15,
#     "center_point[]":  f"{CENTER_POINT[0]},{CENTER_POINT[1]}",
#     "distance[]": DISTANCE,
#     "isMapView": 1,
#     "page": 1
# }

params = {
"cat": 2,
"subcat": 2,
"rooms": "3-4",
"price": "6000-9000",
"z": 13,
"center_point[]": f"{CENTER_POINT[0]},{CENTER_POINT[1]}",
"distance[]": 1305,
"isMapView": 1,
"page": 1
}


if __name__ == "__main__": 
    for attempt in range(10):
        response = get_response(URL, params)
        if response and response.status_code == 200:
            print(f"Got response: {response.text}")
            items = parse_response(response.text)
            if items is not None:
                message = serialize_data(items, CENTER_POINT, 10)
                print("Sending message: ", message)
                print("attempt: ", attempt)
                send_message(message)
                break
            else:
                print("Failed to parse response")
        else:
            print('Failed to get response')
            if response:
                print(response.text)
        
        if attempt < 9:
            sleep_time = 1 + random.uniform(0, 1)
            time.sleep(sleep_time)
    else:
        print("Exceeded maximum retries. Exiting.")
        exit(1)