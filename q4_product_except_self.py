def product_except_self(nums):
    n = len(nums)
    answer = [1] * n

    # Calculate prefix products for each element
    prefix = 1
    for i in range(n):
        answer[i] = prefix
        prefix *= nums[i]

    # Calculate suffix products and multiply with prefix products
    suffix = 1
    for i in range(n - 1, -1, -1):
        answer[i] *= suffix
        suffix *= nums[i]

    return answer


# Example usage
nums = [1, 2, 3, 4]
print(product_except_self(nums))
