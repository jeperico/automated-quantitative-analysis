from alpha_vantage.timeseries import TimeSeries

api_key = "LKJKAJZ5EG24M8L0"


def get_latest_price(ticker):
    # Initialize Alpha Vantage API client
    alpha_vantage = TimeSeries(key=api_key, output_format='json')

    try:
        # Get latest data for the stock ticker
        data, meta_data = alpha_vantage.get_quote_endpoint(symbol=ticker)
        print(data, meta_data)
        # Extract latest price from the data
        latest_price = data['05. price']
        return latest_price

    except Exception as e:
        print(f"Error fetching data for {ticker}: {str(e)}")
        return None


if __name__ == "__main__":
    stock_symbol = input("Send a ticker ")  # PETR4.SA
    price = get_latest_price(stock_symbol)

    if price is not None:
        print(f"Latest price of {stock_symbol}: {price}")
    else:
        print(f"Failed to retrieve the latest price of {stock_symbol}.")
