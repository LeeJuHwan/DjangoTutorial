### STEP 5

- REVERSE URL
    - urlpatterns에 있는 name의 사용 방법
        - path에 있는 name을 하드 코드를 이용하지 않고 name을 사용해서 리다이렉션을 사용 할 수 있다.
        <img width="1707" alt="image" src="https://user-images.githubusercontent.com/118493627/215967270-ab45f375-d3bb-4add-a461-33d622b5753d.png">

    - reverse function을 이용하여 name으로 리다이렉션 할 수 있고, 함수 내에 인자를 arguments를 받을 수 있다.

    - overview
        <img width="1389" alt="image" src="https://user-images.githubusercontent.com/118493627/215967673-67cee3ff-1d63-4ea1-9cad-cd76207a31c1.png">

    - code
        - args를 이용한 방법
            ```
                return HttpResponseRedirect(
                    reverse("detail", args = [1])
                )
            ```

        - kwargs를 이용한 방법
            ```
            return HttpResponseRedirect(
                reverse("detail", kwargs={"question_id" : 1})
            )
            ```
