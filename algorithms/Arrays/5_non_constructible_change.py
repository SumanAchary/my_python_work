#  "coins": [5, 7, 1, 1, 2, 3, 22]
# write the function, which would find the minimum amount of
# change that cannot be created from the above given chnage.


def nonConstructibleChange(coins):
    coins.sort()
    # 	[1, 1, 2, 3, 5, 7, 22]
    currentChangeCreated = 0
    for coin in coins:
        if coin > currentChangeCreated + 1:
            return currentChangeCreated + 1
        currentChangeCreated += coin
    return currentChangeCreated + 1
