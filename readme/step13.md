### STEP 13

- UPDATE MODEL

    <img width="1009" alt="image" src="https://user-images.githubusercontent.com/118493627/216772602-dd4e2a7d-0a94-499d-b8b8-e9046e1d8578.png">

    - `models.py`에서 만든 Field는 value가 지정되어 있지 않기 때문에 Null True, Blank 등 값을 넣어줘야 한다.

    - ROLLBACK 
        - 테이블을 잘못 만들었을 때 롤백 하는 방법

    - VALIDATORS
        - 대부분 front-end에서 filter를 하기 때문에 자주 사용되지는 않지만 한 번 훑어보는 정도로 알아보는 메소드이고 사용자의 입력을 컨틀로 할 수 있다.

    - UPDATE RECORD
        - 업데이트 할 기존의 레코드를 찾고 내용을 입력 한 후 save하면 내용이 업데이트 된다.

    - DELETE QUERY
        - 프라이머리 키를 통해 내용을 읽고 delete 메소드를 통해 지울 수 있다.

- code
    - Update column
    `polls/models.py`
    - 추가 된 내용
        ```
        from django.core.validators import MaxLengthValidator, MinLengthValidator

        owner = models.CharField(
        max_length=200,
        blank=True,
        validators=[MinLengthValidator(3),
        MaxLengthValidator(10)])
        ```

        ```
        python manage.py migrations
        ```

        <img width="558" alt="image" src="https://user-images.githubusercontent.com/118493627/216773419-bff6a5d3-d629-457f-81c1-9d3d5c1ba256.png">

        ```
        python manage.py migrate

        ```

    - ROLLBACK
        ```
        python manage.py migrate polls 0001_initial
        ```
        
        - 장고는 쉽게 과거 데이터 취합 전 상황을 되돌릴 수 있다. 마치 깃 허브 처럼.


    - validator full_clean
    ```
    >>> from django.utils import timezone
    >>> from polls.models import Question
    >>> now = timezone.now()
    >>> q = Question(question_text = "how old are you?", owner = "1", pub_date = now)
    >>> q.full_clean(
    ```
    - owner는 최소 글자 길이 3, 최대 글자 길이가 10인 validators 옵션을 적용한 field이다. 그렇기 때문에 현재 숫자 1만 적힌 오너의 컬럼은 당연히 에러가 날 수 밖에 없다. 이 코드를 고쳐보자.

    ```
    >>> q = Question(question_text = "how old are you?", owner = "juhwan", pub_date = now)
    >>> q.full_clean()

    >>> q.save()

    >>> Question.objects.all()
    <QuerySet [<Question: What's up?>, <Question: how old are you?>]>
    ```

    - delete
    ```
    >>> q = Question.objects.get(pk = 1)
    >>> q
    <Question: What's up?>
    >>> q.delete()
    (1, {'polls.Question': 1})
    >>> q = Question.objects.all()
    ```