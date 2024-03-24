
def pivotInteger(n):
    left = 0
    right = n-1

    vals = [_ for _ in range(1, n+1)]
    # print(vals)

    while left != n-1 and right != 0:
        left_vals_to_check = []
        right_vals_to_check = []

        if left == 0:
            left_vals_to_check = [vals[0]]
        else:
            left_vals_to_check = vals[0:left]

        if right == n-1:
            right_vals_to_check = [vals[n-1]]
        else:
            right_vals_to_check = vals[right:n]

        print(left, right, left_vals_to_check, right_vals_to_check)
        print(sum(left_vals_to_check), sum(right_vals_to_check))
        print('-')
        if sum(left_vals_to_check) < sum(right_vals_to_check):
            left += 1
        else:
            right -= 1

        if left_vals_to_check[-1] == right_vals_to_check[0] and sum(left_vals_to_check) == sum(right_vals_to_check):
            return left_vals_to_check[-1]
    return -1



# print(pivotInteger(8))
# print(pivotInteger(1))
print(pivotInteger(12))