<br>

# 🛠️ [11725 트리의 부모 찾기](http://www.acmicpc.net/problem/11725) <img height="27px" width="27px" src="https://static.solved.ac/tier_small/9.svg"/>

<br>

## 📖문제
>루트 없는 트리가 주어진다. 이때, 트리의 루트를 1이라고 정했을 때, 각 노드의 부모를 구하는 프로그램을 작성하시오.

<br>

## ⌨️입력
>첫째 줄에 노드의 개수 N (2 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N-1개의 줄에 트리 상에서 연결된 두 정점이 주어진다.

<br>

## 💻출력
>첫째 줄부터 N-1개의 줄에 각 노드의 부모 노드 번호를 2번 노드부터 순서대로 출력한다.

<br><br>

<details>
  <summary>🎈</summary>
  <br>

>파이썬의 기본 재귀 한계 = 100회

``` python
import sys
sys.setrecursionlimit(10**6)
```

>위 코드를 통해 기본 재귀 한계 조정
  
</details>

<br><br>
