import yfinance as yf
import matplotlib.pyplot as plt
 
def plot_stocks(symbols, start_date, end_date):
    plt.figure(figsize=(10, 6))
    for symbol in symbols:
        stock_data = yf.download(symbol, start=start_date, end=end_date)
        plt.plot(stock_data.index, stock_data['Close'], label=symbol)
 
    plt.title('Stock Price Over Time')
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.legend()
    plt.grid(True)
    plt.show()
 
if __name__ == "__main__":
    # Define the stock symbols and time range
    stock_symbols = ['MSFT', 'AMZN', 'GOOGL', 'IBM', 'ORCL', 'BABA', 'CRM', 'VMW']
    start_date = '2020-01-01'
    end_date = '2024-01-01'
 
    # Plot the stock data
    plot_stocks(stock_symbols, start_date, end_date)