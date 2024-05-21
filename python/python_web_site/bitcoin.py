import requests
import matplotlib.pyplot as plt
 
def fetch_data_from_api():
    # CoinGecko API endpoint for fetching historical cryptocurrency prices
    url = 'https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=usd&days=30'
 
    # Sending GET request to the API endpoint
    response = requests.get(url)
 
    # Parsing JSON response
    data = response.json()
 
    # Extracting prices from the response
    prices = data['prices']
 
    # Converting timestamps to milliseconds
    timestamps_ms = [entry[0] for entry in prices]
 
    # Converting timestamps to seconds and prices to USD
    timestamps = [timestamp / 1000 for timestamp in timestamps_ms]
    prices_usd = [entry[1] for entry in prices]
 
    return timestamps, prices_usd
 
def plot_data(timestamps, prices_usd):
    # Plotting the data
    plt.plot(timestamps, prices_usd)
    plt.title('Bitcoin Prices Over the Last 30 Days')
    plt.xlabel('Timestamp (Unix Time)')
    plt.ylabel('Price (USD)')
    plt.xticks(rotation=45)  # Rotating x-axis labels for better readability
    plt.show()
 
if __name__ == "__main__":
    # Fetch data from the CoinGecko API
    timestamps, prices_usd = fetch_data_from_api()
 
    # Plot the data
    plot_data(timestamps, prices_usd)
 