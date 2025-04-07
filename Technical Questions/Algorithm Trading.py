import pandas as pd

data = pd.read_csv(r'C:\Users\User\Desktop\Programming Files\ShareForce Technical Assessments\data.csv')

#print(data)

#def minMaxMean(data):

#while not at the end of the list, check if the value has dropped by 3% or more from previous value. 
#If so save that value, move 5 spaces forward and sell. Calculate overall percentage increase or decrease

def trading_algorithm_sol(data):

    i = 1
    #count = 0
    overall_percentage_increase = 0

    sol_data = data[data['ticker'] == 'sol-za']

    sol_data_list = sol_data['close'].tolist()

    while i < len(sol_data_list):
        if sol_data_list[i] <= sol_data_list[i-1] * (1-0.03):
            buy = sol_data_list[i]
            sell = sol_data_list[i+5]
            percentage_increase = (sell - buy) / buy * 100
            #count+=1
            #print(f"Buy at {buy} and sell at {sell} for a percentage increase of {percentage_increase:.2f}% \n {count}")
            overall_percentage_increase += percentage_increase
        i += 1
    
    return overall_percentage_increase

print(f"Overall percentage increase/decrease of SOL-ZA is {trading_algorithm_sol(data):.2f}% \n ")

#Creating algorithm trader function that works for all tickers


def trading_algorithm(data, ticker = "sol-za",  percentage_dec = 0.03, hold_period = 5):

    i = 1
    overall_percentage_increase = 0
    ticker_data = data[data['ticker'] == ticker]
    ticker_data_list = ticker_data['close'].tolist()

    while i < len(ticker_data_list):
        if ticker_data_list[i] <= ticker_data_list[i-1] * (1-percentage_dec):
            buy = ticker_data_list[i]
            #If index out of bound, break out of while loop
            if i+hold_period >= len(ticker_data_list):


                break
            else:
                sell = ticker_data_list[i+hold_period] 

            percentage_increase = (sell - buy) / buy * 100
            overall_percentage_increase += percentage_increase
        i += 1
    
    return overall_percentage_increase


# Calling trading algorithm for all tickers
unique_tickers = data['ticker'].unique().tolist()

for ticker in unique_tickers:
    overall_percentage_increase = trading_algorithm(data,ticker)
    print(f"Overall percentage increase/decrease of {ticker} is {overall_percentage_increase:.2f}%")

print("\n")

# Calling trading algorithm for all tickers with -4% drop rate for buy in
for ticker in unique_tickers:
    overall_percentage_increase = trading_algorithm(data,ticker, 0.04)
    print(f"Overall percentage increase/decrease of {ticker} with 4% drop is {overall_percentage_increase:.2f}%")

print("\n")

# Calling trading algorithm for all tickers with 10 day waiting period before selling
for ticker in unique_tickers:
    overall_percentage_increase = trading_algorithm(data,ticker, 0.03, 10)
    print(f"Overall percentage increase/decrease of {ticker} with 10 day waiting period is {overall_percentage_increase:.2f}%")

print("\n")

# create a function to calculate minimum, maximum, and average return for all tickers/companies
def minMaxMean(data, ticker):
   
    i=0
    counter = 0
    overall_percentage_increase = 0

    max,min,mean = 0,0,0

    ticker_data = data[data['ticker'] == ticker]
    ticker_data_list = ticker_data['close'].tolist()
    
    while i < len(ticker_data_list):    
        if ticker_data_list[i] <= ticker_data_list[i-1] * (1-0.03):
            buy = ticker_data_list[i]

            if i+5 >= len(ticker_data_list):
                break
            else:
                sell = ticker_data_list[i+5]
                counter+=1

            percentage_increase = (sell - buy) / buy * 100

            if percentage_increase >= max:
                max = percentage_increase
            if percentage_increase <= min:
                min = percentage_increase   

            overall_percentage_increase += percentage_increase
            mean = overall_percentage_increase/counter

        i += 1

    print(f"Minimum percentage increase/decrease of {ticker} is {min:.2f}%")
    print(f"Maximum percentage increase/decrease of {ticker} is {max:.2f}%")
    print(f"Mean percentage increase/decrease of {ticker} is {mean:.2f}% \n")

for ticker in unique_tickers:
    minMaxMean(data, ticker)