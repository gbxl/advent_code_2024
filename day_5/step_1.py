from typing import Dict

def build_rules(rules) -> Dict:
    rule_book = {}
    for first, second in rules:
        rule_book[first] = rule_book.get(first, set())
        rule_book[first].add(second)
    return rule_book


def validate_list_order(rule_book, order_list):
    # Create a mapping of each number's index in the list
    index_map = {num: idx for idx, num in enumerate(order_list)}
    
    # Check each constraint
    for num, constrained_nums in rule_book.items():
        # If the number is in the list, check its constraints
        if num in index_map:
            for constrained_num in constrained_nums:
                if constrained_num in index_map:
                    # Ensure num comes before constrained_num
                    if index_map[num] >= index_map[constrained_num]:
                        return False
    
    return True

def middle(numbers) -> int:
    return numbers[len(numbers)//2]

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
    counter = 0
    rule_book = build_rules(rules)
    for number_list in updates:
        if validate_list_order(rule_book, number_list):
            counter += middle(number_list)

    print(counter)


if __name__ == '__main__':
    main()