import time

def check_list_order(number_list, rules):
    # Check each adjacent pair
    for i in range(len(number_list) - 1):
        for rule in rules:
            if number_list[i] == rule[1] and number_list[i+1] == rule[0]:
                return False
    return True

def sort_list_by_constraints(number_list, rules):
    sorted_list = number_list.copy()
    
    # Try to bubble swap elements to respect constraints
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(sorted_list) - 1):
            # Check if this pair needs to be swapped
            for rule in rules:
                if (sorted_list[i] == rule[0] and 
                    sorted_list[i+1] == rule[1]):
                    # Swap the elements
                    sorted_list[i], sorted_list[i+1] = sorted_list[i+1], sorted_list[i]
                    swapped = True
                    break
    
    return sorted_list

def main():            
    rules = []
    updates = []
    with open('/Users/lucasg/work/advent_code_2024/day_5/input.txt', 'r') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            if '|' in line:
                rules.append(tuple(map(int, line.split('|'))))
            elif ',' in line:
                updates.append(list(map(int, line.split(','))))
    v_counter = 0
    i_counter = 0
    for number_list in updates:
        # Check original order
        is_valid = check_list_order(number_list, rules)
        if is_valid:
            v_counter += number_list[len(number_list)//2]
        else:
            sorted_list = sort_list_by_constraints(number_list, rules)
            i_counter += sorted_list[len(sorted_list)//2]

    print(v_counter)
    print(i_counter)


if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print(f"Took {end - start:.2f} s")  