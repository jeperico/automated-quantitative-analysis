import gspread as gs

gc = gs.service_account(filename="credentials.json")

sheet = gc.open("Automatic Quantitative Analysis").get_worksheet(0)

bbas3_price = sheet.acell("b2").value
gare11_price = sheet.acell("c2").value


def dy10(stock):
    return int(stock) * 0.1


print(bbas3_price)
print(gare11_price)

sheet.update_acell("b3", dy10(bbas3_price))
sheet.update_acell("c3", dy10(gare11_price))

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
