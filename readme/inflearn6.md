# STEP 6

## SERIALIZERS FBVs 방식으로 구현 해보기
<img width="1065" alt="image" src="https://user-images.githubusercontent.com/118493627/224542689-87615f59-d60b-414d-ab96-c6a2cb1123b0.png">
- queryset & model instance를 파이썬의 데이터 타입을 변경 시키는 것 Byte type -> JSON,XML

- Django Model Form과 유사하다.
    - Model Serializer 또한, Meta class에 model, field를 연결 하면, Create와 Update을 할 수 있다.

## Serializer / Deserializer Process
<img width="1108" alt="image" src="https://user-images.githubusercontent.com/118493627/224543068-932ebbb9-819e-428a-bcde-527cf6a73eec.png">

### SER
1. Serializer를 사용하기 위해, Model Instance를 Serializer에 추가
2. Serializer를 통해 translate 실행
3. translate된 데이터는 python native datatype으로 변환
4. render 를 사용하여 JSON으로 return

### DES
1. input JSON
2. Data Parse -> Python native datatype 
3. Translate -> Model instance

<img width="1184" alt="image" src="https://user-images.githubusercontent.com/118493627/224543259-f2791fc2-1f5f-436f-aac2-8623f3d4b948.png">

<img width="1142" alt="image" src="https://user-images.githubusercontent.com/118493627/224543408-f6259e46-8798-4d7e-90b5-97a4464f7536.png">

### ABOUT CODE
- `snippets/models.py`
    ```
    from django.db import models
    from pygments.lexers import get_all_lexers
    from pygments.styles import get_all_styles

    LEXERS = [item for item in get_all_lexers() if item[1]]
    LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
    STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


    class Snippet(models.Model):
        created = models.DateTimeField(auto_now_add=True)
        title = models.CharField(max_length=100, blank=True, default='')
        code = models.TextField()
        linenos = models.BooleanField(default=False)
        language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
        style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

        owner = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE)
        highlighted = models.TextField()

        class Meta:
            ordering = ['created']
    ```
- `settings.py`
    - Installed Apps
        ```
        INSTALLED_APPS = [
            "django.contrib.admin",
            "django.contrib.auth",
            "django.contrib.contenttypes",
            "django.contrib.sessions",
            "django.contrib.messages",
            "django.contrib.staticfiles",
            "rest_framework",
            "drf_spectacular",
            "api.apps.ApiConfig",
            "snippets"
        ]
        ```
- `snippets/serializers.py`
    ```
    from rest_framework import serializers
    from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


    class SnippetSerializer(serializers.Serializer):
        id = serializers.IntegerField(read_only=True)
        title = serializers.CharField(required=False, allow_blank=True, max_length=100)
        code = serializers.CharField(style={'base_template': 'textarea.html'})
        linenos = serializers.BooleanField(required=False)
        language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
        style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')


        def create(self, validated_data):
            """
            Create and return a new `Snippet` instance, given the validated data.
            """
            return Snippet.objects.create(**validated_data)

        def update(self, instance, validated_data):
            """
            Update and return an existing `Snippet` instance, given the validated data.
            """
            instance.title = validated_data.get('title', instance.title)
            instance.code = validated_data.get('code', instance.code)
            instance.linenos = validated_data.get('linenos', instance.linenos)
            instance.language = validated_data.get('language', instance.language)
            instance.style = validated_data.get('style', instance.style)
            instance.save()
            return instance
    ```
- `snippets/views.py`
    ```
    from django.shortcuts import render
    from django.http import HttpResponse, JsonResponse
    from django.views.decorators.csrf import csrf_exempt
    from snippets.models import Snippet
    from rest_framework.parsers import JSONParser
    from snippets.serializers import SnippetSerializer

    @csrf_exempt
    def snippet_list(request):
        """
        List all code snippets, or create a new snippet.
        """
        if request.method == 'GET':
            snippets = Snippet.objects.all()
            serializer = SnippetSerializer(snippets, many=True)
            return JsonResponse(serializer.data, safe=False)

        elif request.method == 'POST':
            data = JSONParser().parse(request)
            serializer = SnippetSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=201)
            return JsonResponse(serializer.errors, status=400)

    @csrf_exempt
    def snippet_detail(request, pk):
        """
        Retrieve, update or delete a code snippet.
        """
        try:
            snippet = Snippet.objects.get(pk=pk)
        except Snippet.DoesNotExist:
            return HttpResponse(status=404)

        if request.method == 'GET':
            serializer = SnippetSerializer(snippet)
            return JsonResponse(serializer.data)

        elif request.method == 'PUT':
            data = JSONParser().parse(request)
            serializer = SnippetSerializer(snippet, data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data)
            return JsonResponse(serializer.errors, status=400)

        elif request.method == 'DELETE':
            snippet.delete()
            return HttpResponse(status=204)
    ```
    - Serializer가 여러개 값을 갖고 있으면 인자 값으로 `Many = True`를 사용 해야한다.

- `urls.py`
    - `snippets/urls.py`
        ```
        urlpatterns = [
            path('snippets/', views.snippet_list),
            path('snippets/<int:pk>/', views.snippet_detail),
        ]
        ```
    - `app/urls.py`
        ```
        urlpatterns = [
            path('snippets/', views.snippet_list),
            path('snippets/<int:pk>/', views.snippet_detail),
        ]
        ```

