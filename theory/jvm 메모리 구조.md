## 자바의 프로그램 실행 구조

![execute_structure](https://velog.velcdn.com/images%2Fshin_stealer%2Fpost%2F2b05aec3-0719-482f-a6f0-e4e1ae92f7f1%2Fimage.png)

## JVM 의 전체적인 구조

![jvmStructure](https://velog.velcdn.com/images%2Fshin_stealer%2Fpost%2F8e500340-258e-4150-85c0-455921663229%2Fimage.png)

* Source Code (.java) 파일을 Java Compiler를 통해서 Byte Code(.Class)파일로 변환한다. (컴퓨터가 이해할 수 있는 코드로 변환)

* Byte Code로 변환된 파일을 JVM의 Class Loader 로 보낸다.

* Class Loader는 말 그대로 Class 파일을 불러와서 메모리에 저장하는 역할을 한다.

* Execution Engine 은 Class Loader에 저장된 Byte Code를 명령어 단위로 분류하여 하나씩 실행하게 하는 엔진이다.

* Garbage Collector 는 사용하지 않거나 필요없는 객체들을 메모리에서 소멸시키는 역할을 한다.

* Runtime Data Area (Memory Area) 는 JVM이 프로그램을 수행하기위해 운영체제로부터 할당받은 메모리 공간이다.

### Runtime Data Area(Memory Area)의 구조

![runtimeDataArea](https://velog.velcdn.com/images%2Fshin_stealer%2Fpost%2F024b42b8-85fa-4393-9668-6ef15227a0d0%2Fimage.png)

1) Method Area

* JVM이 실행되면서 생기는 공간이다.
* Class 정보, 전역변수 정보, Static 변수 정보가 저장되는 공간이다.
* Runtime Constant Pool 에는 말 그대로 '상수' 정보가 저장되는 공간이다.
* 모든 스레드에서 정보가 공유된다.

2) Heap

* new 연산자로 생성된 객체, Array와 같은 동적으로 생성된 데이터가 저장되는 공간
* Heap에 저장된 데이터는 Garbage Collector 가 처리하지 않는한 소멸되지 않는다.
* Reference Type 의 데이터가 저장되는 공간
* 모든 스레드에서 정보가 공유된다.

3) Stack

* 지역변수, 메소드의 매개변수와 같이 잠시 사용되고 필요가 없어지는 데이터가 저장되는 공간
* Last In First Out, 나중에 들어온 데이터가 먼저 나간다
* 만약, 지역변수 이지만 Reference Type일 경우에는 Heap 에 저장된 데이터의 주소값을 Stack 에 저장해서 사용하게 된다.
* 스레드마다 하나씩 존재한다.

4) PC Register

* 스레드가 생성되면서 생기는 공간
* 스레드가 어느 명령어를 처리하고 있는지 그 주소를 등록한다.
* JVM이 실행하고 있는 현재 위치를 저장하는 역할

5) Native Method Stack

* Java 가 아닌 다른 언어 (C, C++) 로 구성된 메소드를 실행이 필요할 때 사용되는 공간

-------
## 출처
* https://velog.io/@shin_stealer/%EC%9E%90%EB%B0%94%EC%9D%98-%EB%A9%94%EB%AA%A8%EB%A6%AC-%EA%B5%AC%EC%A1%B0
