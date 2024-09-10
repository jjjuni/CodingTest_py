<br>

# 🛠️ [24511 queuestack](http://www.acmicpc.net/problem/24511) <img height="27px" width="27px" src="https://static.solved.ac/tier_small/8.svg"/>

<br>

## 📖문제
한가롭게 방학에 놀고 있던 도현이는 갑자기 재밌는 자료구조를 생각해냈다. 그 자료구조의 이름은 queuestack이다.

queuestack의 구조는 다음과 같다. 1번, 2번, ... , N번의 자료구조(queue 혹은 stack)가 나열되어있으며, 각각의 자료구조에는 한 개의 원소가 들어있다.

queuestack의 작동은 다음과 같다.

 
<li>x<sub>0</sub>을 입력받는다.</li>
 
<li>x<sub>0</sub>을 1번 자료구조에 삽입한 뒤 1번 자료구조에서 원소를 pop한다. 그때 pop된 원소를 x_1이라 한다.</li>
 
<li>x<sub>1</sub>을 2번 자료구조에 삽입한 뒤 2번 자료구조에서 원소를 pop한다. 그때 pop된 원소를 x<sub>2</sub>이라 한다.</li>

<li>...</li>
 
<li>x<sub>N-1</sub>을 N번 자료구조에 삽입한 뒤 N번 자료구조에서 원소를 pop한다. 그때 pop된 원소를 x<sub>N</sub>이라 한다.</li>
 
<li>x<sub>N</sub>을 리턴한다.</li>
도현이는 길이 M의 수열 C를 가져와서 수열의 원소를 앞에서부터 차례대로 queuestack에 삽입할 것이다. 이전에 삽입한 결과는 남아 있다. (예제 1 참고)

queuestack에 넣을 원소들이 주어졌을 때, 해당 원소를 넣은 리턴값을 출력하는 프로그램을 작성해보자.

<br>

## ⌨️입력
첫째 줄에 queuestack을 구성하는 자료구조의 개수 
$N$이 주어진다. (
$1 \leq N \leq 100\,000$)

둘째 줄에 길이 
$N$의 수열 
$A$가 주어진다. 
$i$번 자료구조가 큐라면 
$A_i = 0$, 스택이라면 
$A_i = 1$이다.

셋째 줄에 길이 
$N$의 수열 
$B$가 주어진다. 
$B_i$는 
$i$번 자료구조에 들어 있는 원소이다. (
$1 \leq B_i \leq 1\,000\,000\,000$)

넷째 줄에 삽입할 수열의 길이 
$M$이 주어진다. (
$1 \leq M \leq 100\,000$)

다섯째 줄에 queuestack에 삽입할 원소를 담고 있는 길이 
$M$의 수열 
$C$가 주어진다. (
$1 \leq C_i \leq 1\,000\,000\,000$)

입력으로 주어지는 모든 수는 정수이다.

<br>

## 💻출력
수열 
$C$의 원소를 차례대로 queuestack에 삽입했을 때의 리턴값을 공백으로 구분하여 출력한다.

<br><br>

<details>
  <summary>🎈</summary>
  <br>

  <code>input()</code> 함수는 한글자씩 버퍼에 담는과정과 문자열을 변환하는 과정때문에 속도가 느려짐
  
  -> 사용 시 시간 초과

  ```python
    import sys
    N = int(sys.stdin.readline())              # input() 대신 sys.stdin.readline() 사용
    Stack = []

    for i in range(N):
    option = sys.stdin.readline().strip()      # input() 대신 sys.stdin.readline() 사용
  ```

  단, <code>sys.stdin.readline()</code> 사용 시 \n과 같은 개행문자도 포함하기 때문에 int() 또는 .strip()과 같은 처리가 필요

  <br>

## 🪄참고 자료
1. [[Python 문법] 파이썬 입력 받기(sys.stdin.readline)](https://velog.io/@yeseolee/Python-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9E%85%EB%A0%A5-%EC%A0%95%EB%A6%ACsys.stdin.readline)

2. [[Python] input보다 sys.stdin.readline의 처리 속도가 빠른 이유는?](https://green-leaves-tree.tistory.com/12)

3. [Python - String strip(), rstrip(), lstrip() 사용 방법](https://codechacha.com/ko/python-string-strip/)
</details>

<br><br>
