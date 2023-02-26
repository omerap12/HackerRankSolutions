# https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem
"""
Get every ranked grade to its rank position. then get the player grade to its position by using binary search
"""


def binary_search(arr, v, indexes_arr):
    high = len(arr) - 1
    low = 0
    while low < high:
        mid = (high + low) // 2
        # for cases when [20,50] (mid is 20 , mid+1 is 50 and v is 25)
        if arr[mid] < v < arr[mid + 1]:
            return indexes_arr[arr[mid]]
        # for cases when [10,20] (mid is 20, v is 15)
        elif arr[mid - 1] < v < arr[mid]:
            return indexes_arr[arr[mid - 1]]
        elif v < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1


def climbingLeaderboard(ranked, player):
    ranked.sort(reverse=True)
    res = []
    indexes_arr = {ranked[0]: 1}
    max_val = ranked[0]
    min_val = ranked[len(ranked) - 1]
    last_used = ranked[0]
    # Get every grade to its rank
    for number in ranked:
        if number == last_used:
            continue
        else:
            indexes_arr[number] = indexes_arr[last_used] + 1
            last_used = number
    # remove duplicates and sort arr
    tmp_arr = sorted([k for k in indexes_arr.keys()])

    for p in player:
        # check if player grade is equal to rank grade or lower than the min or higher than the max
        if p in indexes_arr.keys():
            res.append(indexes_arr[p])
        elif p < min_val:
            res.append(indexes_arr[min_val] + 1)
        elif p == min_val:
            res.append(indexes_arr[min_val])
        elif p >= max_val:
            res.append(indexes_arr[max_val])
        else:
            # if the player grade is between to ranked grades use binary search for find the closest rank grade
            res.append(binary_search(tmp_arr, p, indexes_arr))
    return res
