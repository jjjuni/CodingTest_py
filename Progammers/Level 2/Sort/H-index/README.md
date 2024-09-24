<br>

# 🛠️ [H-Index](https://school.programmers.co.kr/learn/courses/30/lessons/42747?language=python3)　level 2

<br>

## 📖 문제 설명
>H-Index는 과학자의 생산성과 영향력을 나타내는 지표입니다. 어느 과학자의 H-Index를 나타내는 값인 h를 구하려고 합니다. 위키백과1에 따르면, H-Index는 다음과 같이 구합니다.
>
>어떤 과학자가 발표한 논문 n편 중, h번 이상 인용된 논문이 h편 이상이고 나머지 논문이 h번 이하 인용되었다면 h의 최댓값이 이 과학자의 H-Index입니다.
>
>어떤 과학자가 발표한 논문의 인용 횟수를 담은 배열 citations가 매개변수로 주어질 때, 이 과학자의 H-Index를 return 하도록 solution 함수를 작성해주세요.

<br><br>

## ❗제한 사항
> - 과학자가 발표한 논문의 수는 1편 이상 1,000편 이하입니다.
> - 논문별 인용 횟수는 0회 이상 10,000회 이하입니다.

<br><br>

<details>

  <summary> 
  
  ## 🎈 참고
  </summary>
  <br>

## 📄 로직
> 논문 `n`편 중, `h`번 이상 인용된 논문이 `h`편 이상이면 되기 때문에 논문 배열(`citations`)을 내림차순 정렬 하고 `citations[h] > h`를 만족하는 h의 최댓값을 찾으면 된다. `h = 0`부터 `h`를 1씩 증가시키며 위 조건이 맞지 않을 때까지 반복하여 값을 얻어낸다.
> 
> 단, 이때 `h`의 값이 `n`(논문의 수, 즉, 배열의 길이)을 넘기지 않도록 주의‼️
<br>

</details>

<br><br>
