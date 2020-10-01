from utils import *

def display_as_percentage(val):
  return '{:.1f}%'.format(val * 100)

amazon_prices = [1699.8, 1777.44, 2012.71, 2003.0, 1598.01, 1690.17, 1501.97, 1718.73, 1639.83, 1780.75, 1926.52, 1775.07, 1893.63]
ebay_prices = [35.98, 33.2, 34.35, 32.77, 28.81, 29.62, 27.86, 33.39, 37.01, 37.0, 38.6, 35.93, 39.5]

# Write code here
# get logarithmic rates of return
def get_returns(prices):
  returns=[]
  for i in range(0,len(prices)-1):
    start_price=prices[i]
    end_price=prices[i+1]
    r=calculate_log_return(start_price,end_price)
    returns.append(r)
  return returns

amazon_returns=get_returns(amazon_prices)
ebay_returns=get_returns(ebay_prices)

print([display_as_percentage(i) for i in amazon_returns])
print('')
print([display_as_percentage(i) for i in ebay_returns])

print("Amazon's annual return is",display_as_percentage(sum(amazon_returns)))
print("Ebay's annual return is",display_as_percentage(sum(ebay_returns))+'\n')

print(calculate_variance(amazon_returns))
print(calculate_variance(ebay_returns))
print("Amazon std.dev is",display_as_percentage(calculate_stddev(amazon_returns)))
print("Ebay std.dev is",display_as_percentage(calculate_stddev(ebay_returns)))

print("The correlation between the two stocks is:",round(calculate_correlation(amazon_returns,ebay_returns
),2))
