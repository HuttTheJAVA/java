## Adapter(중개인 또는 적응자)
![image](https://github.com/HuttTheJAVA/java/assets/92637789/e92b68d0-c71f-47c0-bc0f-d98872c0f62e)

Adapter 패턴의 UML는 위 그림과 같다. 그림만 봐도 adapter가 target(interface)와 adaptee(class) 사이에서 중개하는 역할을 할 것으로 보여진다.   
Adapter의 목적은 이미 만들어진 함수를 다른 쪽(Target)에서 접근할 수 있도록 중개인 역할을 하는게 목적이다.   
(**client**:adapter를 이용하는 쪽(Main 함수), Target(adaptee에 구현된 함수를 접근하고자 하는 쪽), adaptee(원하는 함수가 다 구현되어 있는 곳), adapter(Target과 adaptee를 연결하는 중개인)
일단 adapter는 target과 adaptee 둘과 연관이 되어있어야 한다.target쪽은 implement하고 adaptee는 함수가 필요하니까 상속한다.   
adapter는 target을 implement하면 되는데 일일이 다 implement하는 것이 아닌 상속받은 adaptee의 함수를 가져다 쓰면 된다.   
그 후 코드상으로는 adapter를 생성하고 추상적인 Target을 변수로 바인딩한다. 그리고 Target의 추상적인 메소드를 호출하면   
adapter를 통해 adaptee의 실제 구현체가 호출된다.   

## 생각정리
------------------
사실 이해는 되지만 간단한 예제로는 adapter의 용이성이 크게 와닿지는 않는다. 실제 서비스에서 사용되는 코드를 보면 더 와닿지 않을까 싶다.   
내가 이해한 adapter의 의의는 이미 구현된 함수(adaptee 함수)를 다른 접점(인터페이스 타입 인터페이스 말고..)에서 접근하고 싶을 때 중개인인 adapter를 통해   
가져다 쓴다(adapter가 구현체를 중개해준다)~ 라는 취지로 이해했다. 비유를 하자면 이미 만들어진 바퀴를 또 만들지 않고 만들어져 있는 것을 가져다 쓴다~라고 비유할 수 있을 것 같다.
