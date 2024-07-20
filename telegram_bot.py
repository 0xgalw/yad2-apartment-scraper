import requests
TOKEN_PATH = "token.txt"

def get_token():
    with open(TOKEN_PATH, "r") as file:
        return file.read().strip()
    
def send_message(message):
    bot_token = get_token()
    chat_id = "@MyYad2testingBot"
    url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
    payload = {
        'chat_id': chat_id,
        'text': message
    }
    response = requests.post(url, data=payload)
    if response.status_code == 200:
        print('Message sent successfully')
    else:
        print('Failed to send message')
        print(response.text)

if __name__ == "__main__":
    send_message("Hello World")