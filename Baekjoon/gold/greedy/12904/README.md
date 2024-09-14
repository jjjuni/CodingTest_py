<br>

# 🛠️ [12904 A와 B](http://www.acmicpc.net/problem/12904) <img height="27px" width="27px" src="https://static.solved.ac/tier_small/11.svg"/>
<br>

## 📖문제
>수강신청의 마스터 김종혜 선생님에게 새로운 과제가 주어졌다. 
>
>김종혜 선생님한테는 Si에 시작해서 Ti에 끝나는 N개의 수업이 주어지는데, 최소의 강의실을 사용해서 모든 수업을 가능하게 해야 한다. 
>
>참고로, 수업이 끝난 직후에 다음 수업을 시작할 수 있다. (즉, Ti ≤ Sj 일 경우 i 수업과 j 수업은 같이 들을 수 있다.)
>
>수강신청 대충한 게 찔리면, 선생님을 도와드리자!

<br><br>

## ⌨️입력
>첫 번째 줄에 N이 주어진다. (1 ≤ N ≤ 200,000)
>
>이후 N개의 줄에 S<sub>i</sub>, T<sub>i</sub>가 주어진다. (0 ≤ S<sub>i</sub> < T<sub>i</sub> ≤ 10<sup>9</sup>)

<br>

## 💻출력
>강의실의 개수를 출력하라.

<br><br>

<details>
  <summary>🎈</summary>
  <br>
  
## 🗂️파이썬 Heapq
> ### 1. <code>heap</code> 이란?
> * 우선순위 큐를 위해 만들어진 자료구조로, 완전 이진트리의 일종
> * 여러 값 중 최대/최소 값을 빠르게 찾아내도록 만들어진 반정렬 상태
> * <code>heap</code>은 중복값을 허용!
>> ### 우선순위 큐?
>> 들어간 순서와 상관 없이 높은 우선순위를 가진 원소는 낮은 우선순위를 가진 원소보다 먼저 처리
>> 
>> 만약 두 원소가 같은 우선순위를 가진다면 큐에서 그들의 순서에 의해 처리
> ### 2. <code>heapq</code> 란?
> * 파이썬 내장 모듈로, 우선순위 큐 알고리즘인 힙을 제공
> * 내부적으로 최소 힙의 형태로 정렬
>> #### <code>heap</code>함수
>> * <code>heappush()</code>
>>    - <code>heap</code>에 <code>item</code>추가 후 최소 힙으로 정렬
>> * <code>heappop()</code>
>>    - <code>heap</code>에서 가장 작은 원소 제거 및 반환

<br>

## 📄로직
> A강의가 B강의보다 먼저 시작 할 때
> * (B강의 시작 시간) ≥ (A강의 종료 시간) -> 겹치지 않는 강의
> * (B강의 시작 시간) < (A강의 종료 시간) -> 겹치는 강의
> 
> -> 먼저 시작한 강의는 시작 시간은 알 필요가 없다!
>   
> 따라서, <code>heap</code>에는 강의의 종료시간만 저장하여 다른 강의의 시작시간과 비교
>
> ### 전체 로직
> * <code>heap</code>에 각 강의의 종료시간을 저장
> * 시간표 리스트에서 강의 시작 시간과 <code>heappop()</code> 값을 비교 (<code>heappop()</code>를 하면 가장 작은 값, 즉, 가장 먼저 끝나는 강의의 종료시간 반환)
>   - (현재 강의 시작 시간) ≥ <code>heappop()</code>(겹치지 않는 강의) : <code>heap</code>에 저장되어 있던 강의 종료시간 <code>heappop()</code> 및 현재 강의 종료시간<code>heappush()</code>
>   - (현재 강의 시작 시간) < <code>heappop()</code>(겹치는 강의) : 현재 강의의 종료시간만 추가로 <code>heappush()</code>
>
> ### 코드 진행
> 1. 강의 시간표를 입력받아 리스트(<code>inf[]</code>)에 저장
> 2. <code>inf[]</code>를 강의 시작시간(오름차순)으로 정렬
> 3. 첫번째 강의 종료시간을 <code>heap</code>에 <code>push</code>
> 4. 강의 시간표 리스트를 돌며 각 강의 시작시간과 현재 <code>heap</code>에 있는 가장 작은 수와 비교
> 5. 겹치지 않는다면 <code>heap</code>에서 끝난 강의 <code>pop()</code> 및 현재 강의 <code>push</code>
> 6. $N$번 반복 후 <code>len(heap)</code> 출력



## 🪄참고자료
>[파이썬으로 데이터 정렬하기 : sort(), sorted(). key](https://rnrmffj.tamchart.com/74)
>
>[[파이썬]sorted() 이해 및 활용법 (key 매개변수 사용법)](https://gusugi.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC-sorted-%ED%95%A8%EC%88%98-%EC%9D%B4%ED%95%B4-%EB%B0%8F-%ED%99%9C%EC%9A%A9%EB%B2%95-key-%EB%A7%A4%EA%B0%9C%EB%B3%80%EC%88%98-%ED%99%9C%EC%9A%A9%EB%B2%95)
>
><br>
>
>[[자료구조] 파이썬 힙큐(heapq) 모듈로 힙(heap) 다루기](https://velog.io/@yeonsubaek/%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%ED%9E%99%ED%81%90heapq-%EB%AA%A8%EB%93%88%EB%A1%9C-%ED%9E%99heap-%EB%8B%A4%EB%A3%A8%EA%B8%B0)

</details>

<br><br>

