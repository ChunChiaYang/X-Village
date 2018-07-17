def func(m):
    if m==4:
        raise IndexError("list index out of range!!!")

try:
    func(4)
except IndexError as e:
    print(e)
else:
    print("success")