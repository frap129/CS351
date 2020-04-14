"""
CS-351 - HW1
Joseph Maples
4/14/20
"""

def greatest_difference(nums1, nums2):
    """ (list of number, list of number) -> number
    
    Return the greatest absolute difference between numbers at corresponding
    positions in nums1 and nums2.
    
    Precondition: len(nums1) == len(nums2) and nums1 != []
    
    # # >>> greatest_difference([1, 2, 3], [6, 8, 10])
    7
    >>> greatest_difference([1, -2, 3], [-6, 8, 10])
    # # 10
    # """
    if len(nums1) != len(nums2) or nums1 == []:
        return -1

    diff = 0
    for i in range(0, len(nums1)):
    	if (nums1[i] - nums2[i]) > diff:
    		diff = nums1[i] - nums2[i]
    	elif (nums2[i] - nums1[i]) > diff:
    		diff = nums2[i] - nums1[i]

    return diff

def can_pay_with_two_coins(denoms, amount):
    """ (list of int, int) -> bool
    
    Return True if and only if it is possible to form amount, which is a 
    number of cents, using exactly two coins, which can be of any of the 
    denominatins in denoms.
    
    >>> can_pay_with_two_coins([1, 5, 10, 25], 35)
    True
    >>> can_pay_with_two_coins([1, 5, 10, 25], 20)
    True
    >>> can_pay_with_two_coins([1, 5, 10, 25], 12)
    False
    """
    for first in range(0, len(denoms)):
    	for second in range(first, len(denoms)):
    		if (denoms[first] + denoms[second]) == amount:
    			return True

    return False

def all_fluffy(s):
    """ (str) -> bool
    Return True iff every letter in s is fluffy. Fluffy letters are those that
    appear in the word 'fluffy'.
    
    >>> all_fluffy('fullfly')
    True
    >>> all_fluffy('firefly')
    False
    """
    fluffy = "fluffy"
    for letter in s:
    	if letter not in fluffy:
    		return False

    return True


def digital_sum(nums_list):
    """ (list of str) -> int
    
    Precondition: s.isdigit() holds for each string s in nums_list.
    
    Return the sum of all the digits in all strings in nums_list.
    
    >>> digital_sum(['64', '128', '256'])
    34
    >>> digital_sum(['12', '3'])
    6
    """
    for s in nums_list:
        if not s.isdigit():
            return -1

    sum = 0
    for num in nums_list:
        for digit in num:
            sum += int(digit)

    return sum

def count_collatz_steps(n):
    """ (int) -> int
    
    Return the number of steps it takes to reach 1, by applying the two steps
    of the Collatz conjecture beginning from n.
    >>> count_collatz_steps(6)
    8
    """
    steps = 0
    while (n != 1):
    	if (n % 2) == 0:
    		n = n / 2
    	else:
    		n = (n * 3) + 1
    	steps += 1

    return steps


