""" Input size of list; Input space separated items of list.
    The function calculates the ratio of positives, negatives, and zeroes in the list.
"""

def plusMinus(arr):
    length = n
    if n != len(arr):
        length = len(arr)
        print(f"The list size provided  ( {n} ) was incorrect. Using correct list size now ( {length} )")

    if not check_constraints(arr, length):
        return

    positives = sum(1 for num in arr if num > 0)
    negatives = sum(1 for num in arr if num < 0)
    zeroes = sum(1 for num in arr if num == 0)

    pos_ratio = positives / length
    neg_ratio = negatives / length
    zero_ratio = zeroes / length

    print(f'Positive ratio: {"{:.6f}".format(pos_ratio)}')
    print(f'Negative ratio: {"{:.6f}".format(neg_ratio)}')
    print(f'Zero ratio: {"{:.6f}".format(zero_ratio)}')

def check_constraints(arr, length):
    length = len(arr)
    if length == 0:
        print("The list is empty")
        return False

    elif length > 100:
        print("The list is too long")
        return False

    disproportionate = sum(1 for num in arr if num > 100 or num < -100)
    if disproportionate > 0:
        print(f"An item is disproportionately sized. Items must be less than 101 and greater than -101")
        return False
    return True 


if __name__ == '__main__':
    n = int(input("Provide length of list\n").strip())
    arr = list(map(int, input("Provide space-separated items in list\n").rstrip().split()))
    plusMinus(arr)