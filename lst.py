# def lucky_number(lst):
#     counter = 0
#     num = lst[0]

#     for i in lst:
#         curr = lst.count(i)
#         if curr > counter:
#             counter = curr
#             num = i

#     return num


# lstr = [1, 2, 2, 2, 2, 3, 4, 1, 5, 3, 1, 2, 5, 6, 2, 5, 6, 7, 2]

# print(lucky_number(lstr))


# def val(s: str) -> bool:
#     if s == "(){}[]" or s == "({[]})" or s == "{[()]}" or s == "[{()}]":
#         return True
#     else:
#         return False


# if __name__ == "__main__":
#     line = input("line: ")
#     if val(line):
#         print(True)
#     else:
#         print(False)


def find_it(seq):
    num = seq[0]

    for i in seq:
        odd = seq.count(i)
        if odd % 2 != 0:
            num = i
    return num


lst = [1, 2, 3, 6, 4, 7, 6, 8, 1, 3, 2, 4, 5, 9, 7, 1, 4, 3, 5, 9]
print(find_it(lst))
