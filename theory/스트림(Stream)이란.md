기존의 컬렉션들을 순회할때 for문이나 foreach문을 사용했는데 순회를 하면서 처리 코드가 복잡해질 수 있다는 단점이 있다.<br></br>
그래서 스트림(데이터의 흐름)으로 컬렉션에 람다식을 적용시켜 코드를 간결하게 만들 수 있다.(컬렉션 이외에도 다른 일회성 자원에도 적용가능하다.ex) 네트워크 자원...(이 부분은 좀 더 공부해야 될꺼같다.)
그러나 iterator처럼 스트림도 일회성이다. 나름대로 이유를 찾아보니 컬렉션을 순회하는 경우는 그 컬렉션 데이터가 고의로 지우지 않는 이상 그대로 남아 있어 stream을 재사용하면 되지 않나 라고 생각했다. <br></br>근데 설계자들이 스트림을 처음 고안할 때 스트림은 컬렉션만을 위한 것이 아니라서(일회성 자원 = 네트워크 자원) 한번 순회한 요소가 그대로 남아있지 않을 경우도 있다.   
그래서 재사용이 가능하지 않게 만들었다고 한다.(이 부분 솔직히 이해는 되는데 일회성 자원들을 다뤄본 경험이 없어서 막 와닿지는 않는다. 좀 더 공부해야 알 거 같다.)<br></br>

-------
## 내가 이해한 대로 그려 본 스트림 그림.
![image](https://user-images.githubusercontent.com/92637789/224049878-8ed87e4d-aae0-48a0-ae6f-34281b8897a7.png)
