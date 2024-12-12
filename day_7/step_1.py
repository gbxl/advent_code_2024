def process(tups):
    total_sum = 0
    for total, nums in tups:
        # print(f"{total=} -- {nums=}")
        num = nums.pop(0)
        if can_equate(total, nums, num):
            total_sum += total
    return total_sum


def can_equate(total, nums, curr) -> bool:
    if len(nums) == 0:
        return curr == total
    num = nums[0]  # Take the first number without modifying the list
    rest = nums[1:]  # Create a new list with the remaining elements
    mult = can_equate(total, rest, curr * num)
    # print(f"{mult=} -- {total=}, {nums=}, {curr=} * {num=}")
    addit = can_equate(total, rest, curr + num)
    # print(f"{addit=} -- {total=}, {nums=}, {curr=} + {num=}")
    return mult or addit


def main():
    with open('/Users/lucasg/work/advent_code_2024/day_7/input_b.txt', 'r') as file:
        lines = file.readlines()
    tups = []
    for line in lines:
        res = int(line.split(":")[0])
        nums = [int(n) for n in line.split(":")[1].strip().split(" ")]
        
        tups.append((res, nums))
    result = process(tups)
    print(result)


if __name__ == '__main__':
    main()