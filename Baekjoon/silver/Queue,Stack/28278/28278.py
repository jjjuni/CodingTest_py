import sys

N = int(sys.stdin.readline())
Stack = []

for i in range(N):
    option = sys.stdin.readline().strip()

    if option[0] == "1":
        a = option.split()
        Stack.append(a[1])

    elif option == "2":
        if len(Stack) != 0:
            print(Stack.pop())
        else:
            print(-1)

    elif option == "3":
        print(len(Stack))

    elif option == "4":
        if len(Stack) == 0:
            print("1")
        else:
            print("0")

    elif option == "5":
        if len(Stack) != 0:
            print(Stack[-1])
        else:
            print("-1")