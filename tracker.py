import requests
import time

api_key = 'd5155771-1c73-4d94-a1d4-08a8d9d478e4'
bot_token = '1765394551:AAEmwld7lkTMxpf0dtzt0X-QjVmRN1mT6wI'
chat_id = '1789035481'
threshold = 30000
time_interval = 5 * 60 

def get_btc_price():
    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
    headers = {
        'Accepts' : application/json,
        'X-CMC_PRO_API_KEY' : api_key
        }

    # requesting data through request model then converting to JSON file
    response = requests.get(url, headers=headers)
    response_json = response.json()

    #retrieving specifically bitcoin price while parsing irrelevant data
    btc_price = response_json ['data'][0]
    return btc_price['quote']['USD']['price']

    #message function to telegram_app
def send_mesage(chat_id, msg):
    url= f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={msg}"
    requests.get(url)


def main():
    price_list =[]

    while True:
        price = get_btc_price()
        price_list.append(price)
        if price <threshold:
            send_message(chat_id, msg=f'BTC PRICE DROP ALERT: {price}')
        if len(price_list) >= 6:
            send_message(chat_id=chat_id, msg=price_list)
            price_list=[]

        time.sleep(time_interval)

        if __name__ == '__main__':
            main()

    