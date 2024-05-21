import yfinance as yf
import matplotlib.pyplot as plt
 
def plot_stock(symbol, start_date, end_date):
    # Retrieve stock data
    stock_data = yf.download(symbol, start=start_date, end=end_date)
 
    # Plotting
    plt.figure(figsize=(10, 6))
    plt.plot(stock_data.index, stock_data['Close'], label=symbol)
    plt.title('Stock Price Over Time')
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.legend()
    plt.grid(True)
    plt.show()
 
if __name__ == "__main__":
    # Define the stock symbol and time range
    stock_symbol = 'AAPL'  # Example: Apple Inc.
    start_date = '2020-01-01'
    end_date = '2021-01-01'
 
    # Plot the stock data
    plot_stock(stock_symbol, start_date, end_date)