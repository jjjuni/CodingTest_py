<br>

# 🛠️ [2164 카드2](http://www.acmicpc.net/problem/2164) <img height="27px" width="27px" src="https://static.solved.ac/tier_small/7.svg"/>

<br>

## 📖문제
>N장의 카드가 있다. 각각의 카드는 차례로 1부터 N까지의 번호가 붙어 있으며, 1번 카드가 제일 위에, N번 카드가 제일 아래인 상태로 순서대로 카드가 놓여 있다.
>
>이제 다음과 같은 동작을 카드가 한 장 남을 때까지 반복하게 된다. 우선, 제일 위에 있는 카드를 바닥에 버린다. 그 다음, 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮긴다.
>
>예를 들어 N=4인 경우를 생각해 보자. 카드는 제일 위에서부터 1234 의 순서로 놓여있다. 1을 버리면 234가 남는다. 여기서 2를 제일 아래로 옮기면 342가 된다. 3을 버리면 42가 되고, 4를 밑으로 옮기면 24가 된다. 마지막으로 2를 버리고 나면, 남는 카드는 4가 된다.
>
>N이 주어졌을 때, 제일 마지막에 남게 되는 카드를 구하는 프로그램을 작성하시오.

<br>

## ⌨️입력
>첫째 줄에 정수 N(1 ≤ N ≤ 500,000)이 주어진다.

<br>

## 💻출력
>첫째 줄에 남게 되는 카드의 번호를 출력한다.

<br><br>

<details>
  <summary>🎈</summary>
  <br>
  
  >반복문 안에서 <code>pop()</code> 사용 시 시간복잡도가 O(n<sup>2</sup>) 으로 위 문제에서는 시간 초과가 뜸
  >
  >끝자리에 요소를 추가하는 <code>append()</code> 와 달리 <code>pop(n)</code> 은 탐색 알고리즘이 포함되어 시간복잡도가 O(n)이다
  > 
  >
  >따라서, 
  >```python
  >from collections import deque
  >import sys
  >
  >Q = deque = deque()
  >
  >...중략...
  >
  >while len(Q) != 1:
  >  Q.popleft() 
  >  Q.append(Q.popleft())
  >
  >...중략
  >```
  >위와 같이 deque를 사용하여 queue를 이용해야 함

  <br><br>

  ## 🪄참고자료
  >1. [Python list 연산에 따른 시간 복잡도](https://hyun-am-coding.tistory.com/entry/Python-list-%EC%97%B0%EC%82%B0%EC%97%90-%EB%94%B0%EB%A5%B8-%EC%8B%9C%EA%B0%84-%EB%B3%B5%EC%9E%A1%EB%8F%84)
  >
  >2. [[Python] Dequeue 사용하기](https://ooeunz.tistory.com/31)
  
</details>

<br><br>
