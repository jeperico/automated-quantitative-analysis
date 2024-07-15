import yfinance as yf

# ticker_input = input("Send a Ticker: ")
ticker = yf.Ticker("AMZN")

print(ticker.actions)
