### STEP 12

- DB CONFIGURATION

    <img width="740" alt="image" src="https://user-images.githubusercontent.com/118493627/216761200-26d162ea-2c3a-46ab-aefc-adcb7a788180.png">

    - Engine : sqlite라는 데이터베이스에 저장
    - Name : sqlite가 저장이 되는 경로

    - 다른 DB 연결

        <img width="652" alt="image" src="https://user-images.githubusercontent.com/118493627/216761247-7d5ddf5a-ec82-4239-84ac-e16498bcb9df.png">

- SELECT QUERY

    <img width="1065" alt="image" src="https://user-images.githubusercontent.com/118493627/216761445-f6452030-be56-43b6-a355-6170d997d363.png">
    
    - GET
        - 오브젝트를 1개만 요청할 때 쓸 수 있다.
        - 만약 데이터가 없거나 1개 보다 많으면 에러가 난다.
        - e.g
            ```
            Question.objects.get(pk=1)
            ```
            - primary key가 1인 경우를 조회


    - Filter
        - 오브젝트를 호출하지만 리스트로 반환한다.
        - 데이터가 없더라도 반환값이 리스트기 때문에 에러가 나지 않는다.
        - e.g
            ```
            Question.objects.filter(id=1)
            ```
            - id 값이 1인 경우를 조회
    - 차이점
        - 반환 하는 자료구조가 다르다.

    
- FIELD LOOKUP
    <img width="1059" alt="image" src="https://user-images.githubusercontent.com/118493627/216761830-adeeeaa7-ea28-4474-b75f-fe87039fa172.png">

    - SQL의 where clause
        - e.g
            ```
            field__lookup = 'value'
            ```

- COMPLEX LOOKUP
    - AND | OR
        <img width="1012" alt="image" src="https://user-images.githubusercontent.com/118493627/216762406-237019d8-d463-4679-be9a-32223f80e4fd.png">

    - Q를 활용한 complex lookup 구문이 generic한 구문보다 우선 순위로 작성 해야 에러가 나지 않는다. 

- EVALUATION 
    - 장고에서는 특이하게 Evaluation 기능이 지원된다. 이 기능은 evaluation 조건에 맞는 상황일 때에 실행 되고, 그 때 그 때 실행되지 않고 모든 상황이 끝난 후 마지막 return이 나오게 된다.

    - For loop 같은 반복되는 구문
        - 필터 값을 변수에 담은 후 반복문을 사용 할 때 
    - strides
        - 슬라이싱
    - pickle
    - repr(str) or len
        - 나온 값의 길이를 셀 때 
        - 이럴 때는 count를 이용하는 것이 속도 측면에서 이점이 있다.
    - list()로 감싼 구문
    - if 구문

- code
    `polls/models.py``
    ```
    class Question(models.Model) :
        def __str__(self):
        return self.question_text
    ```
    - class의 call을 명시하게 되면 shell을 통해 쿼리를 작성하여 return 받는 값이 일치하는 값의 개수 였지만, 그 고유의 값으로 return 되는 것을 확인할 수 있다.
        ```
        # __str__ 적용 전
        >>> Question.objects.all()
        <QuerySet [<Question: Question object (1)>]>

        # __str__ 적용 후
        >>> Question.objects.all()
        <QuerySet [<Question: What's up?>]>
        >>> Question.objects.filter(id=1)
        <QuerySet [<Question: What's up?>]>
        ```
    
    - filter 명령어가 아닌 get으로 입력하고 없는 값의 인덱스를 지정하면 `Question matching query does not exist.`에러가 나타난다.

    QUERY E.G
    ```
    # SELECT * FROM question WHERE question_text LIKE '%What%';
    >>> Question.objects.filter(question_text__contains="What")
    <QuerySet [<Question: What's up?>]>


    >>> from django.utils import timezone
    >>> current_year = timezone.now().year
    >>> Question.objects.get(pub_date__year = current_year)
    <Question: What's up?>
    ```