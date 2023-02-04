### STEP 11

- ORM

- DATABASE
    - SQL
        - 하드디스크가 비쌌기 때문에 데이터를 복제 하지 않고 하나 하나의 데이터를 저장 하는 것에 집중했다.
        - vertical scaling
            - CPU 하나로 데이터베이스를 사용 했다가 높은 사양을 사용 하기 위해서는 하드웨어 자체를 업그레이드 해야 한다. 
    - NOSQL
        - "Non SQL" or "not only SQL"
        - 개발자들이 쉽게 프로그래밍을 할 수 있으며 쿼리 질의가 빠르다.
        - Json 자료구조로 되어 있기 때문에 horizontal scaling으로 이루어져있다.
    <img width="859" alt="image" src="https://user-images.githubusercontent.com/118493627/216586372-0be64286-0a00-48f3-b384-7a0e435a6ad3.png">
     
    - SQL 
        - SQLite을 사용
    

- MODEL
    - 데이터가 저장되는 곳과 연결하는 것을 모델이라고 한다.
    - 장고는 기본적으로 CRUD를 전체적으로 서포트 하고 있다.
    - 모델 클래스는 `models.py` 에서 생성한다.

    <img width="939" alt="image" src="https://user-images.githubusercontent.com/118493627/216760461-ea63948c-837a-4b48-a867-712093e739fd.png">

    - makemigrations 
        - 모델을 생성할 장소를 만들어준다.
    - migrate
        - 데이터베이스와 내가 만든 모델이 서로 일치한지 확인한다.

     
- code
    `polls/models.py`
    ```
    from django.db import models

    class Question(models.Model) :
        question_text = models.CharField(max_length=200)
        pub_date = models.DateTimeField("date published")

    class Choice(models.Model) :
        question = models.ForeignKey(Question, on_delete=models.CASCADE)
        choice_text = models.CharField(max_length=200)
        votes = models.IntegerField(default=0) 
    ```
    - makemigrations

    <img width="361" alt="image" src="https://user-images.githubusercontent.com/118493627/216760746-1f8fef87-6c7c-4f62-bf00-feb75c8d429f.png">

    - migrate

    <img width="691" alt="image" src="https://user-images.githubusercontent.com/118493627/216760838-2afb3f71-c30e-4bf8-918c-b656ee00a872.png">



- python shell
    ```
    >>> from polls.models import Choice, Question
    >>> Question.objects.all()
    <QuerySet []>

    >>> from django.utils import timezone
    >>> q = Question(question_text = "What's new?", pub_date = timezone.now())
    >>> q.save()
    >>> Question.objects.all()
    <QuerySet [<Question: Question object (1)>]>
    >>> q.id
    1
    >>> q.question_text
    "What's new?"
    >>> q.pub_date
    datetime.datetime(2023, 2, 4, 9, 58, 51, 362076, tzinfo=datetime.timezone.utc)

    >>> q.question_text = "What's up?"
    >>> q.save
    <bound method Model.save of <Question: Question object (1)>>
    >>> q.save()
    >>> q.question_text
    "What's up?"
    ```
    - 장고를 통해 데이터를 입력하고 입력되어 있는 내용은 언제든지 수정이 가능하다.