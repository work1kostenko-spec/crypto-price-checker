import requests

coins = ["bitcoin", "ethereum", "binancecoin"]

for coin in coins:
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=usd"
    price = requests.get(url).json()[coin]["usd"]
    print(f"{coin.capitalize()}: ${price}")
