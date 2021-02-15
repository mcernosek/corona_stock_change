import numpy as np 

ticker_hi_low = [["IDXX",290.97,182.94], ["CRWD",66.04,33.01], ["TTD",315.43,144.39], ["NFLX",386.19,298.84], ["MKC",167.08,113.83], ["ZM",103.93,151.70], ["ASML",317.39,196.99], ["MAR",146.84,63.81], ["TSLA",901.00,361.22], ["MSFT",187.28,135.98], ["SWKS",122.59,67.90], ["NVDA",308.70,196.40], ["APPN",62.07,31.36], ["ISRG",618.29,394.19], ["TDOC",117.24,163.56], ["MA",344.45,203.30], ["SHOP",535.58,322.29], ["WORK",28.44,17.04]]
ticker_change = np.array([["IDXX",0.0], ["CRWD",0.0], ["TTD",0.0], ["NFLX",0.0], ["MKC",0.0], ["ZM",0.0], ["ASML",0.0], ["MAR",0.0], ["TSLA",0.0], ["MSFT",0.0], ["SWKS",0.0], ["NVDA",0.0], ["APPN",0.0], ["ISRG",0.0], ["TDOC",0.0], ["MA",0.0], ["SHOP",0.0], ["WORK",0.0]])



for i in range(len(ticker_hi_low)):
    hi = ticker_hi_low[i][1]
    low = ticker_hi_low[i][2]
    change = round((((low - hi) / hi) * 100), 2)
    ticker_change[i][1] = change

sorted_ticker_change = ticker_change[ticker_change[:,1].argsort()]

for i in range(len(sorted_ticker_change)):
    print(sorted_ticker_change[i])
    
