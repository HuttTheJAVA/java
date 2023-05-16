### JDBC란?

JDBC는 여러 다른 DBMS를 조작하기 위한 방식을 명세한 인터페이스이다. 이말은, "자바에서 이러한 방식으로 DBMS를 조작하는   
명세를 제공하니, 자신의 DBMS를 자바 개발자들이 사용할 수 있게 하려면 이 명세에 맞춰 JDBC DRIVER를 구현하면 됩니다."라는 의미이다.   
정리하면 JDBC는 DBMS를 조작하는 표준 명세이며, JDBC DRIVER는 이 표준에 맞게 실제 DBMS별로 이 DBMS를 조작할 수 있게 구현한 클래스이다.   
보통 DRIVER는 외부의 장치(여기서는 DBMS, 운영체제에서는 마우스,키보드,프린터 등등..)와 소통할 수 있는 통역사라고 이해하면 좀 더 이해가 쉬울 것 같다.   

### JDBC 작동 방식

DRIVER들을 관리하는 DRIVER 매니저가 있는데 자바 개발자가 DBMS의 특정 조작을 코드로 짜면 (예를 들어 DBMS와의 연결) DRIVER 매니저는   
해당 DBMS에 맞는 JDBC DRIVER(메모리에 로드된)의 명령을 참고해서 DBMS에 내린다. 즉, DRIVER 매니저는 DBMS의 명령문을 몰라도   
그냥 메모리에 로드된 JDBC DRIVER의 명령문들 중 개발자가 요구한 명령과 일치하는 것을 찾아 DBMS로 명령을 하달한다.

#### JDBC DRIVER 사용법 ####

1. 먼저 JDBC DRIVER를 메모리에 로드해야 한다. 이것은 "Class.forName()" 메서드를 이용하면 된다. (괄호 안에 들어가는 매개변수는 DBMS에 따라 다르다.)
(1번을 수행 했으면 JDBC DRIVER가 메모리에 로드된 상태일 것이다.)<br></br>

2. 다음으로 데이터베이스 연결을 설정한다. 코드는 DriverManager.getConnection(). getConnection안에 3개의 매개변수   
가 들어가는데 1.데이터 베이스의 URL,2.데이터 베이스 이름(또는 사용자 이름이라고도 부름.),3.데이터 베이스 비밀번호.   
(여기까지 했으면 데이터 베이스에 접속했으며 데이터 베이스에 참조 변수를 통해 접근할 수 있는 상태가 된다.)<br></br>

3. SQL 질의문을 적는다.<br></br> (SELECT,INSERT,UPDATE,DELETE,TRUNCATE 등..)

4. SQL 질의문을 실행한다.<br></br> Statement나 PreparedStatement를 사용해서 쿼리문을 실행한다.

5. 결과를 처리한다.<br></br> 리턴 값이 있는 SQL문이면 (예를 들어 SELECT) ResultSet 인터페이스 변수를 이용한다.

6.데이터 베이스 연결을 종료.<br></br><br></br>

 <p align = "center"><img src = "https://github.com/HuttTheJAVA/java/assets/92637789/65f388fd-ec96-4867-96e6-8c8910e749e7" height = 480x weight = 500x></p>
(JDBC를 잘 표현한 그림인 거 같아서 넣어봤다.)
