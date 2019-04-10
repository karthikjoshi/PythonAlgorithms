from itertools import combinations
import heapq

## This function initializes an array with  [0,1,2,3,4...up to uppermost denomination of coins]
def assignList(number):
    retList = [0]*number
    for i in range(0,number):
        retList[i] = i+1
    return retList

## In this permutation, we would like to consider every possible coin starting from 1 up to 50 cents
valueList = assignList(50)

## We would like to make all combination of above 50 coins in 4 groups.  (It is 50c4  combinations)
comb = combinations(valueList, 4)

#Heap stores the score
heap = []

## Our aim is to make change for 100 cents - using 4 coins between 1 and 50
amount = 100
bestCaseArray = [ 0,
                  5,0,0,0,5,0,0,0,0,5,
                  0,0,0,0,5,0,0,0,0,5,
                  0,0,0,0,5,0,0,0,0,5,
                  0,0,0,0,0,0,0,0,0,5,
                  0,0,0,0,0,0,0,0,0,5,
                  5,0,0,0,0,0,0,0,0,5,
                  0,0,0,0,0,0,0,0,0,5,
                  0,0,0,0,0,0,0,0,0,5,
                  0,0,0,0,0,0,0,0,0,5,
                  0,0,0,0,0,0,0,0,0,0, 0 ]
## The above code lets us create custom distribution of scoring to specific change groups.
## For eg, the above code is biased towards, 1, 5, 10,15,20,25,30,40,50,51,60,70,
## 80,90
## the resulting coin suggestion is [1, 5, 20, 30]  - with cost score of  1.45  average coins, with below list of minimum coin count array for
## 1 to 100 cent changes.
## [0, 1, 2, 3, 4, 1, 2, 3, 4, 5, 2, 3, 4, 5, 6, 3, 4, 5, 6, 7, 1, 2, 3, 4, 5, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 2, 3, 4, 5, 6, 2, 3, 4, 5, 6, 3, 4, 5, 6, 7, 2, 3, 4, 5, 6, 3, 4, 5, 6, 7, 2, 3, 4, 5, 6, 3, 4, 5, 6, 7, 3, 4, 5, 6, 7, 4, 5, 6, 7, 8, 3, 4, 5, 6, 7, 4, 5, 6, 7, 8, 3, 4, 5, 6, 7, 4, 5, 6, 7, 8, 4]
## As you can see, 20 and 30 cents coins showed up to help minimize average coin count.

## If we are worried about uniform distribution, then please uncomment below line of code,
#bestCaseArray = [1]*101

for coinT in comb:
    #Lets assume that we got coins as {a, b, c, d} belongs to a set of numbers in the set (1,50)
    coins = list(coinT)
    ## Initialize array with higher value. Our aim is not to find all possibility of arriving at a cent value -
    # We are interested in arriving at a chaange using only the minimum number of coins
    result = [9999]*(amount+1)
    result[0] = 0

    for j in range(1,amount+1):
        for coin in coins:
            if(j >= coin):
                coinDiff = j-coin
                if coinDiff >=0:
                    result[j] = min(result[j], result[coinDiff]+1)
    sum = 0
    ## Average cost of one combination of 4 coins is to sum the total coins required to make every change {from 1 to 100 cents - using the a, b, c, d coins}
    ## and dividing it by 100 to get average
    for i in range(1, len(result)):
        sum = sum + result[i]*bestCaseArray[i]
    ## Push the score to heap - also push the coins in question
    heapq.heappush(heap, (sum/100.0, (result, coins)))
## Pop the minimum score - and corresponding coin set
(score, (changes,coins))  = heapq.heappop(heap)
print("Score is "+str(score) + " and change matrix is ")
print(changes)
print(coins)




