try:
    with open('note.txt','w+') as f:
        date = input('輸入日期:')
        event = input('輸入事件:')
        description = input('輸入心得:')

        f.write(date +'\n')
        f.write(event +'\n')
        f.write(description +'\n')
        print(f.read())
except FileExistsError:
    print("File does not exist!")
except FileNotFoundError:
    print("File does not found!")

with open('note.txt') as f:
    print(f.read())


# wrtie a file 'note.txt'