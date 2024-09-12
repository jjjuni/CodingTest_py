<br>

# 🛠️ [28278 스택 2](http://www.acmicpc.net/problem/28278) <img height="27px" width="27px" src="https://static.solved.ac/tier_small/7.svg"/>

<br>

## 📖문제
>정수를 저장하는 스택을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.
>
>명령은 총 다섯 가지이다.
>
><li>1 X: 정수 X를 스택에 넣는다. (1 ≤ X ≤ 100,000)</li>
><li>2: 스택에 정수가 있다면 맨 위의 정수를 빼고 출력한다. 없다면 -1을 대신 출력한다.</li>
><li>3: 스택에 들어있는 정수의 개수를 출력한다.</li>
><li>4: 스택이 비어있으면 1, 아니면 0을 출력한다.</li>
><li>5: 스택에 정수가 있다면 맨 위의 정수를 출력한다. 없다면 -1을 대신 출력한다.</li> <br>

<br>

## ⌨️입력
>첫째 줄에 명령의 수 N이 주어진다. (1 ≤ N ≤ 1,000,000)
>
>둘째 줄부터 N개 줄에 명령이 하나씩 주어진다.
>
>출력을 요구하는 명령은 하나 이상 주어진다.

<br>

## 💻출력
>출력을 요구하는 명령이 주어질 때마다 명령의 결과를 한 줄에 하나씩 출력한다.

<br><br>

<details>
  <summary>🎈</summary>
  <br>

  ><code>input()</code> 함수는 한글자씩 버퍼에 담는과정과 문자열을 변환하는 과정때문에 속도가 느려짐
  >
  >-> 사용 시 시간 초과
>
>  ```python
>    import sys
>    N = int(sys.stdin.readline())              # input() 대신 sys.stdin.readline() 사용
>    Stack = []
>
>    for i in range(N):
>    option = sys.stdin.readline().strip()      # input() 대신 sys.stdin.readline() 사용
>  ```
>
  >단, <code>sys.stdin.readline()</code> 사용 시 \n과 같은 개행문자도 포함하기 때문에 int() 또는 .strip()과 같은 처리가 필요

  <br>

## 🪄참고 자료
>1. [[Python 문법] 파이썬 입력 받기(sys.stdin.readline)](https://velog.io/@yeseolee/Python-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9E%85%EB%A0%A5-%EC%A0%95%EB%A6%ACsys.stdin.readline)
>
>2. [[Python] input보다 sys.stdin.readline의 처리 속도가 빠른 이유는?](https://green-leaves-tree.tistory.com/12)
>
>3. [Python - String strip(), rstrip(), lstrip() 사용 방법](https://codechacha.com/ko/python-string-strip/)
</details>

<br><br>
