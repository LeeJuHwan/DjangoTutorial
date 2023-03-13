# STEP 7

## REQUEST, RESPONSE
<img width="1060" alt="image" src="https://user-images.githubusercontent.com/118493627/224552686-c20ce2dd-8ef6-46f9-aae6-b2bd74f84400.png">

- HttpRequest : Static한 방식, 장고 중간에서 변경이 불가능

- TemplateResponse : Lazy한 방식으로 장고 중간에서 변경이 가능하다

- `@api_view` : 데코레이터 함수로, FBVs 타입으로 작성 된 코드에 실행 하며 그 부분을 API format으로 변환 할 때 사용한다.

- `APIVIEW` : CBVs로 상속 시켜 DRF에서 response, reqeust를 사용 하여 Request를 받거나, 값을 return 할 수 있다.


## CBV
<img width="1007" alt="image" src="https://user-images.githubusercontent.com/118493627/224553326-56074b6d-4a65-47a2-9fa4-f858542d0e35.png">

- CBVs를 사용하게 되면 Http method를 깔끔하게 분리 할 수 있다.

- 데코레이터를 사용하지 않고 기존 클래스를 상속 받을 수 있다.

### CBVs에서 코드를 간결하게 작성하는 과정

<img width="855" alt="image" src="https://user-images.githubusercontent.com/118493627/224553437-f2cae80f-754f-4749-818d-f60567620dcf.png">

<img width="1110" alt="image" src="https://user-images.githubusercontent.com/118493627/224553469-856b8847-9b04-4b0c-9a00-cd15cb114579.png">

<img width="927" alt="image" src="https://user-images.githubusercontent.com/118493627/224553530-50dafba0-af5a-493b-a158-f98d86850ce1.png">

<img width="1217" alt="image" src="https://user-images.githubusercontent.com/118493627/224553586-939120eb-8c36-4c8a-a470-d794576ee4a4.png">

- FBVs를 사용하는 쪽 일수록 더 섬세한 커스터마이징이 가능하지만, Http method 처리 방식을 지정 해줘야한다.

- 제너릭한 CBV를 이용할 수록 간결해지지만 제공해주는 기능에 의존해야한다.

## ATHENTICATION & PERMISSION
<img width="995" alt="image" src="https://user-images.githubusercontent.com/118493627/224611446-8ee8507d-79eb-40e8-9120-f9680936b36c.png">

- 데이터를 입력 할 때 인증을 거치는 단계

- Permission을 통해서, 글을 작성한 작성자만 업데이트가 가능하도록 설정
    - 인증 되지 않은 요청은 읽기 권한만 부여
---

<img width="872" alt="image" src="https://user-images.githubusercontent.com/118493627/224611998-380cdfb9-7802-4821-b39d-f2676601f99a.png">

<img width="1203" alt="image" src="https://user-images.githubusercontent.com/118493627/224612171-4d1d9aa7-3caf-4d0b-8e12-6d10db5ab77a.png">

