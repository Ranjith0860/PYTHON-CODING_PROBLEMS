# buy a stock in list where buyed stock and sell stock get profit
# where profit=buyed stock should be less than sell stock so we get profit


s_p=[2,1,3,4,5,7]
profit=0
buy_price=s_p[0]

for price in s_p[1:]: #beacuse we took first price is max
    if price<buy_price:
        buy_price=price
    profit=max(profit,price-buy_price)
print(f"price:💲{price}  \nbuyed for:💲{buy_price} \ntotal profit 💲{profit} 😁")
