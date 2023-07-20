## Iterator(반복자)
![image](https://github.com/HuttTheJAVA/java/assets/92637789/f434c36f-91f5-4028-bb92-dd8d5b2e9726)

--------------------------
<br></br>
반복자는 자료구조(Array,List,Tree,Trie,Graph,Map)의 자료 전체를 순회할 때 사용되는 패턴이다.

### Aggregate(집합체) - 인터페이스
> Aggregate는 Iterator를 만드는 메소드가 추상화된 인터페이스이다. 더 설명하자면 반복자를 만드는 메소드가 실제로 구현되지 않고 추상적으로 선언된 것이다.<br></br>
이 메소드는 Iterator를 리턴 타입으로 가진다. 즉 이 메소드를 실행하면 Iterator를 리턴(생성)받는다.
이렇게 추상화된 메소드는 Aggregate를 implement하는 ConcreteAggregate에서 구현한다. 쉽게 말하자면 ConcreteAggregate는 탐색의 대상이 되는 자료구조이고, 탐색이 되는 자료구조는 저마다 자기를 탐색해줄 반복자를 생성하는 메소드를 구현해야 한다.(반복자를 구현하는 것이 아니고 반복자를 생성하는 메소드를 구현하는 것이다. 반복자 구현은 ConcreteIterator에서 할 일이다.)
### ConcreteAggregate(구체적 집합체) - 클래스
> ConcreteAggregate는 Aggregate에서 추상적으로 명시한 반복자 생성 메소드를 구현한다. 이 메소드 안에서 ConcreteIterator를 생성하고 리턴한다.
### Iterator(반복자) - 인터페이스
> 반복자가 제공해야할 메소드들을 추상적으로 정의한 인터페이스 보통 hasNext()와 next()를 추상 메소드로 가진다.
### ConcreteIterator(구체적 반복자) - 클래스
> Iterator 인터페이스를 구현한 것으로 ConcreteIterator별로 다르게 구현할 수 있다. 서로 다른 자료구조에 대한 ConcreteIterator를 그 자료구조 특성에 맞게 Iterator의 추상 메소드들을 구현할 수 있다.
<br></br>

생각정리
-------
> 처음에는 그냥 for문을 써서 탐색하면 안되나?라고 생각했다. 인터넷에 검색해보니 배열같이 캐시메모리에 적합한 자료구조에는 for문을 써서 탐색하는 것이 더 효율적이다.
> 배열의 탐색 시간 복잡도는 O(1)이다.<br></br>
> n 번째 index의 주소값 = 배열 초기 주소값 + 배열 데이터형 사이즈 * index 로 간단한 연산으로 특정 n번째 주소를 쉽게 조회할 수 있다.
> 그러나 연결 리스트나 그래프, 트리 등 index 친화적이지 않은 자료구조들의 특정 index 조회는 배열과 같이 간단하지 않다. 이러한 자료구조들은 같은 자료구조에 속한다고,
> 메모리에 연속적으로 존재하지 않을 수 있기 때문이다. 따라서 이러한 자료구조들을 탐색하기 위해서는 iterator가 필요하다.
