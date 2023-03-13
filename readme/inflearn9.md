# STEP 9

## API View
<img width="999" alt="image" src="https://user-images.githubusercontent.com/118493627/224674280-4976471b-b6b7-4bc6-b92c-df8fa3adaac7.png">

- Viewset은 APIView와 달리 Model에 대해 특화 되어 있고, 상태와 상호작용 하는 API를 사용 할 때 Viewset을 사용하면 편리하다.

- URL config 과정을 Viewset을 사용하면서 자동으로 핸들링 할 수 있다.

<img width="1041" alt="image" src="https://user-images.githubusercontent.com/118493627/224675107-5c39d428-7015-4bb7-abbf-633901fc1973.png">

- Viewset으로 리팩토링 할 때, 필수 인자 값은 `queryset`과 `serializer`이다.

- List와 Retrieve 과정만 필요한 기능이기 때문에 ReadOnlyModelViewSet을 상속 받는다.

<img width="1051" alt="image" src="https://user-images.githubusercontent.com/118493627/224675700-50a40e58-d777-4ad4-97fd-2e1e9f143a62.png">

- 이 처럼, List, Create, Retrive, Update, Destroy 등 기능에 따라 ModelViewSet을 상속 받을 수 있다.

- 글을 작성할 때 작성자를 인증 해야 하기 때문에, ReadOnly 클래스에서 추가적으로 `permission_class`를 인자로 넘겨줌으로 유저 인증을 사용할 수 있다.

### Router
<img width="993" alt="image" src="https://user-images.githubusercontent.com/118493627/224676494-88de5605-39aa-4e72-b288-016a4e7c4b08.png">

- Url routing을 이용할 때, 기존에는 매뉴얼 방식으로 지정 해줬지만, DRF의 라우터를 이용하면 http method들을 자동화 할 수 있다.


### Difference API View and View Set
<img width="927" alt="image" src="https://user-images.githubusercontent.com/118493627/224679312-d10b7668-49ba-4bf3-8ea2-fb08a9138818.png">

- Model에 대해서 Retrive, Create, Update를 이용 하려면 View Set을 이용해야한다.

- API View를 사용하면 커스텀 로직을 사용할 때 편리하다.

- Http method에 집중 되어있다. 
    - Get, Put, Delete, Patch ...

<img width="1178" alt="image" src="https://user-images.githubusercontent.com/118493627/224680045-b8912f6e-58c7-4c57-86e4-5280b0ef2bc0.png">

- CBVs
    - APIView 상속
- FBVs
    - api_view, permission_classees 등 데코레이터 사용



## View Set
<img width="904" alt="image" src="https://user-images.githubusercontent.com/118493627/224680582-8a33b115-a8a1-4b43-abf3-fbe57816998f.png">

- DRF에서 보다 더 간결하게 코드를 작성 하기 위해 만든 것이기 때문에, 여러개의 Generic View를 상속 받고 있다.

- Model에 대한 CRUD Operation에 가장 알맞게 짜여진 프레임워크이다.
    - 다른 프레임워크에서는 리소스 또는 컨트롤러라고 부른다.

<img width="1103" alt="image" src="https://user-images.githubusercontent.com/118493627/224680977-1b2d4f50-4a91-4a68-a725-35f15ea8a5a4.png">

- Url은 라우터를 이용하면 빠르게 자동으로 만들 수 있다.

