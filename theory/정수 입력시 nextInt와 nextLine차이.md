## 정수 입력시 nextInt와 nextLine 차이

### 정수 int 값을 scanner 객체의 nextInt( )를 통해 입력 받을 때
> Scanner scanner = new Scanner(System.in)   
> 
> int num = scanner.nextInt( )     // ParseInt를 할 필요가 없다(정수 그 자체이므로) == 간단하다.

<br></br>

### 정수 int 값을 scanner 객체의 nextLine( )를 통해 입력 받을 때
> Scanner scanner = new Scanner(System.in)   
> 
> String str = scanner.nextLine( )   
> 
> int num = Integer.ParseInt(str) // 스트링 자료의 str을 int형태로 파싱해준다. <= nextInt( )보다 복잡.

<br></br>

### nextLine( )을 왜 쓸까?
> 번거롭게 nextLine( )을 쓰는 이유는 입력을 받는 코드가 반복문안에 있게 될 경우 nextInt( )는 연속적으로 입력을 받기 어렵다.(에러가 나기 쉽다.)   
> 
> 즉, 단 한번의 입력값만 받을 경우는 nextInt( )가 좋고, 여러 입력값을 받아야 하는 경우는 번거롭더라도, nextLine( )을 이용하는것이 좋다.

<br></br>
