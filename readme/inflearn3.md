# STEP 3

## REDIRECT VIEW
<img width="797" alt="image" src="https://user-images.githubusercontent.com/118493627/223631766-2328d222-af21-4728-9067-1358189d25de.png">
- endpoint to endpoint로, redirect가 필요한 부분에 사용되며 공식 documentation에서도 given to url이라고 나와있기 때문에 `urls.py`에서 페이지를 컨트롤 할 수 있다.


### ABOUT CODE
- `dealershop/dealershop/urls.py`
    ```
    from django.views.generic.base import RedirectView

    path("", RedirectView.as_view(url = "inventory/")),
    ```
---

## Class Meta
<img width="893" alt="image" src="https://user-images.githubusercontent.com/118493627/223632716-d08774c6-50c0-4f46-a1d5-9d27ccea4e3f.png">

- Meta
    - ordering = 오브젝트를 호출 할 때 순서를 결정하는 옵션이며, SQL에서 order by와 같은 역할을 한다. 
        - [-year] : descending

    - abstract = Database table을 생성하지 않는 옵션, 클래스에 속성을 많이 지정하는데 다른 클래스에 상속 할 때 불필요한 테이블을 생성하는 것을 방지할 수 있고, `True`로 설정 된 경우 기본 추상 클래스가 된다.

    - db_table = table 이름 옵션을 설정하지 않으면, 기본적으로 snake case - all lower case로 테이블 이름이 결정 되는데, 이 때 테이블 이름을 커스터마이징 할 수 있는 옵션이다.

    - get_latest_by = Manager의 latest(), earliest()에서 사용 될 기본 필드를 지정한다.
        ```
        # 오름차순 order_date 기준 최신
        get_latest_by = "order_date"

        # 우선 순위 내림차순, order_date 오름차순으로 최신
        get_latest_by = ['-priority', 'order_date']
        ```
    - managed = `managed = False`를 하게 되면, Legacy code에 대해 스키마가 없지만 장고에서 사용하고 싶을 때 Migration을 해도 내부에서 테이블을 건들지 않고 사용할 수 있다.
    
<img width="869" alt="image" src="https://user-images.githubusercontent.com/118493627/223636811-e1182815-fb72-41c4-bb77-381de1028dba.png">

    - Index : RDBMS 에서 검색 속도를 향상 시키는 기술
        - Table의 컬럼을 따로 파일로 저장하여서, 검색시 해당 Table의 레코드를 full scan하는 것이 아니라, 저장한 Index 파일을 검색하여서 검색 속도를 빠르게한다.

        - 일반적으로 테이블에 Index를 작성하면 테이블 데이터와 별개로 Index용 데이터가 저장장치에 만들어진다. 이때 이진트리 데이터 구조로 작성될 수 있다.

        - Index가 많아지면 검새 속도가 떨어지고, 테이블이 정규화 되지 않는다. 그렇기 때문에 Index를 잘 사용 하면 속도에서 많은 이점을 가져갈 수 있다.

    - Unique together : 지정한 컬럼은 항상 값이 유니크한 형태인 컬럼으로 지정할 수 있다.
    - Index together : 지정한 컬럼은 유니크와 같이 인덱스 컬럼으로 생성할 수 있다.
    - Verbose name : 사용자가 읽을 때 이름을 정하는 것,
    - Verbose name plural : 오브젝트가 여러 개 있을 때 어떤 방식으로 보여줄지 결정(복수 단어)
    