### STEP 7

- Templates
    - variables : {{ <variable> }} 템플릿이 렌더링 될 때 python server side에서 치환된다. 

    - filters : {{ Variable|lower }} 파이프를 사용하여 변수가 갖고 있는 값의  모양을 바꾸는 함수를 필터링 할 수 있다.
        - lower, upper
        - length
        - date : "D d M Y"
        - escape


    - tags : { % <Command> % } for문이나, if문을 컨트롤 하는 태그이다.
        - form ... in ... endfor
        - if ... elif ... else ... endif
            - ==, !=. >=, <=, >, <
            - and, or, in, not in, is, is not 
        - block & extends

    - comments : {# <Comments> #} 템플릿이 html이기 때문에 html에서 코멘트를 남겨도 된다.


    <img width="2063" alt="image" src="https://user-images.githubusercontent.com/118493627/215973985-ebceaf0f-cf6e-46e4-893e-04fcced0fb81.png">

- code
    - `polls/views.py`
        ```
        def index(request):
            ctx = {
                "greetings" : "Hello there!",
                "location" : {
                    "city" : "seoul",
                    "country" : "South Korea"
                },
                "languages" : ["Korean", "English"]
            }
            return render(request, "polls/main.html", context=ctx)
        ```

    - `polls/templates/polls/main.html`
        ```
        <h1>{{ greetings|lower }}</h1>
        <h2>I am from {{ location.city }}, {{ location.country }}</h2>
        <h2>I speaks {{ languages.0 }} and {{ languages.1 }}</h2>
        <ul>
            {% for lang in languages %}
                <li>{{ lang }}</li>
            {% endfor %}
            
            {% for lang in languages %}
                <li>
                    {% if lang == "Korean" %}
                    condition Korean!
                    {% else %}
                    condition English!
                    {% endif %}
                </li>
            {% endfor %}
        </ul>

        <ul>
            {% for k, v in location.items %}
                <li>{{ k|capfirst }}: {{ v|capfirst }}</li>
            {% endfor %}
        </ul>
        ```

