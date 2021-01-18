#!/usr/bin/python3

def find_two_sum(array: list[int], target: int):
    st = set()
    for num in array:
        remain = target - num
        if (remain in st):
            return remain * num
        st.add(num)
    return None

def find_three_sum(array: list[int], target: int):
    l = len(array)
    for idx, num in enumerate(array):
        ans = find_two_sum(array[idx+1:], target - num)
        if (ans):
            return ans * num
    return None

if __name__ == "__main__":
    file = "input.txt"
    data = [int(num[:-1]) for num in open(file).readlines()]
    print("ans is {}".format(find_three_sum(data, 2020)))
