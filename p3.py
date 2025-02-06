def count_subarrays_with_sum(arr, sum):
    if len(arr) == 0 : return 0
    counts = {}

    initial_sum = {0:1}
    result = 0
    current_sum = 0

    for val in arr:
        current_sum += val
        if current_sum - sum in initial_sum:
            result += initial_sum[current_sum - sum]
        initial_sum[current_sum] = initial_sum.get(current_sum,0) + 1

    return result

def main():
    print(count_subarrays_with_sum([], 0))
if __name__ == "__main__":
    main()
#Given a list of integers and a target sum, 
#return the number of continuous subarrays that sum to sum. 
#For example, if the input is [1,1,1] and sum=2, the output should be 2.

# Believe it or not, it is possible to do this with just one pass through the list! 
# In the brute force solution (computing every subarray sum) we end up doing a lot of repeat work,
# so our goal should be to calculate the values of subarrays only once.
# Here's the strategy. Loop over the elements of the list and:
# 1. store the `current_sum` (the sum of the first $i$ elements) in a hash table counting
# how many times that sum has appeared so far.
# 2. Use the hash table to figure out if there are any subarrays ending at the current element which sum to `k`. 
# Increment a counter if you do.
# Finally, return the number of subarrays found.