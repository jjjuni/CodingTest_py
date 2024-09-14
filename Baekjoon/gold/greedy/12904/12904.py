S = input()
T = input()

def rmv_A(a):
    str = a[:len(a)-1]
    return str

def rmv_B(a):
    str = "".join(reversed(a[:len(a)-1]))
    return str

while len(S) != len(T):
    if T[-1] == "A":
        T = rmv_A(T)
    elif T[-1] == "B":
        T = rmv_B(T)

if S == T:
    print(1)
else:
    print(0)