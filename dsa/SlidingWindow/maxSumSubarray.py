"""Given an array of integer&#x73;**&#x20;arr[]&#xA0;**&#x20;and a numbe&#x72;**&#x20;k**. Return the maximum sum of a subarray of size k.
**Note:** A subarray is a contiguous part of any given array.
**Examples:**
**Input:** arr[] = [100, 200, 300, 400], k = 2 **Output:&#x20;**&#x37;00 **Explanation:&#x20;**&#x61;rr2 + arr3 = 700, which is maximum.
**Input:&#x20;**&#x61;rr[] = [1, 4, 2, 10, 23, 3, 1, 0, 20], k = 4 **Output:&#x20;**&#x33;9 **Explanation:&#x20;**&#x61;rr1 + arr2 + arr3 + arr4 = 39, which is maximum.\
**Input:** arr[] = [100, 200, 300, 400], k = 1 **Output:&#x20;**&#x34;00 **Explanation:&#x20;**&#x61;rr3 = 400, which is maximum.
**Constraints:**
arr.size() ≤ 106\
0 ≤ arr[i] ≤ 106\
1 ≤ k ≤ arr.size()\"""



def max_sum_subarray(arr, k):
    window_sum = sum(arr[:k])
    max_sum = window_sum

    for right in range(k, len(arr)):
        window_sum += arr[right]
        window_sum -= arr[right - k]
        max_sum = max(max_sum, window_sum)

    return max_sum
