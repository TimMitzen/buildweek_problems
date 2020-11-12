from typing import List

class Solution: #o(n)
    def contains_duplicate(nums: List[int]) -> bool:#makes nums a list
        numbers = {}#empty dict
        for num in nums:#loops over the list
            print("nums",nums)
            print("numbers before", numbers)
            print("loop", num)
            if num not in numbers: #if the number not in numbers
                print("num", num)
                numbers[num] = num
                print('numbers after',numbers)
            else:
                print('else', num)
                return True
        print('num',num)
        return False

    print(contains_duplicate([0, 0]))

class Solution_Set:
    def contains_duplicate(nums: List[int]) -> bool:  # makes nums a list
        numbers = set(nums) #duplicateds for set
        for num in nums:
            print("1 num",num)
            print("1 set",numbers)
            print("1 nums", nums)
            if num not in numbers:
                print("before add", numbers)
                numbers.add(num)
                print("after add", numbers)
            else:
                print('else',numbers)
                return True
        return False

    print(contains_duplicate([ 0]))


