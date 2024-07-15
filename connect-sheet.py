import gspread as gs
from alpha_vantage.timeseries import TimeSeries

gc = gs.service_account(filename="credentials.json")
api_key = "LKJKAJZ5EG24M8L0"

def get_latest_price(ticker):
    # Initialize Alpha Vantage API client
    alpha_vantage = TimeSeries(key=api_key, output_format='json')

    try:
        # Get latest data for the stock ticker
        data, meta_data = alpha_vantage.get_quote_endpoint(symbol=ticker)
        # print(data, meta_data)
        # Extract latest price from the data
        latest_price = data['05. price']
        return latest_price

    except Exception as e:
        print(f"Error fetching data for {ticker}: {str(e)}")
        return None


# stock_symbol = input("Send a ticker ") + ".SA"  # PETR4.SA
# price = get_latest_price(stock_symbol)
#
# if price is not None:
#     print(f"Latest price of {stock_symbol}: {price}")
# else:
#     print(f"Failed to retrieve the latest price of {stock_symbol}.")

sheet = gc.open("Automatic Quantitative Analysis").get_worksheet(0)

first_row_values = sheet.row_values(1)

# Iterate over the row values excluding the first cell
for col_index, cell in enumerate(first_row_values[1:], start=2):  # start=2 to account for 1-based index in Google Sheets
    if cell:
        price = get_latest_price(cell + ".SA")
        print(price)
        # Write the price to the next row in the same column
        sheet.update_cell(2, col_index, price)


def dy10(stock):
    return int(stock) * 0.1


# print(bbas3_price)
# print(gare11_price)
#
# sheet.update_acell("b3", dy10(bbas3_price))
# sheet.update_acell("c3", dy10(gare11_price))

# set the first row of your loop
row = 2
# set the limit
limit = 4

# create your while loop, increment by 1 at the end of each loop
while row <= limit:
    data = sheet.acell(f"c{row}").value
    print(data)
    row += 1


print("status: 200.")
