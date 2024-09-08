result = ""                                 # 최종 값을 출력 할 문자열

def pre_order(node, list):                  # 전위 순회
    global result                           # 함수 내에서 전역 변수 사용 선언
    result = result + node

    if list[node][0] != '.':
        pre_order(list[node][0], list)

    if list[node][1] != '.':
        pre_order(list[node][1], list)


def in_order(node, list):                   # 중위 순회
    global result                           # 함수 내에서 전역 변수 사용 선언

    if list[node][0] != '.':
        in_order(list[node][0], list)

    result = result + node

    if list[node][1] != '.':
        in_order(list[node][1], list)

def post_order(node, list):                 # 후위 순회
    global result                           # 함수 내에서 전역 변수 사용 선언

    if list[node][0] != '.':
        post_order(list[node][0], list)

    if list[node][1] != '.':
        post_order(list[node][1], list)
        
    result = result + node

N = int(input())

tree = {}

for _ in range(N):
    a, b, c = input().split()
    tree[a] = [b, c]

pre_order("A", tree)
print(result)
result = ""

in_order("A", tree)
print(result)
result = ""

post_order("A", tree)
print(result)