from collections import defaultdict

# filename = 'demo.txt'
filename = 'input.txt'
sep = ','
numbers = open(filename).readline().strip().split(sep)
numbers = [int(number) for number in numbers]

def part(stop):
    look_up_round_number = dict()
    look_up_number_round = defaultdict(list)
    numbers_cnt = len(numbers)
    for round in range(stop):
        current_number = 0
        if round < numbers_cnt:
            look_up_round_number[round] = numbers[round]
            current_number = numbers[round]
        else:
            last_number = look_up_round_number[round - 1]
            if len(look_up_number_round[last_number]) == 1:
                look_up_round_number[round] = 0
                current_number = 0
            else:
                diff = look_up_number_round[last_number][-1] - look_up_number_round[last_number][-2]
                look_up_round_number[round] = diff
                current_number = diff
        look_up_number_round[current_number].append(round)
        if round % 10000 == 0:
            print(f'round: {round + 1}, number: {current_number}')
    print(f'ans: {look_up_round_number[stop - 1]}')


def main():
    # part(2020)
    part(30000000)


if __name__ == '__main__':
    main()