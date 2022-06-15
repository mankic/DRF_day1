# DRF_day1
DRF 특강 1일차 과제


 1. args, kwargs를 사용하는 예제 코드 짜보기
  - args.py와 kwargs.py 참조  


 2. mutable과 immutable은 어떤 특성이 있고, 어떤 자료형이 어디에 해당하는지 서술하기
  - mutable : 수정 가능한 객체 (list, dict). 하나의 주소값을 갖는다.
  - immutabel : 수정 불가능한 객체 (int, float, str, tuple). 재할당되면 주소값이 바뀌어버린다.


 3. DB Field에서 사용되는 Key 종류와 특징 서술하기
  - Primary key : 데이터베이스 테이블 내에서 유일하게 구분되는 키이다. 유일한 값이기에 중복된 값을 가질 수 없을 뿐 아니라 NULL값을 가질 수 없고 하나의 키만 존재한다.
  - Foreign key : 다른 테이블과 관계를 형성하는 경우 다른 테이블의 키를 참조하는 열을 FK 라고 한다. 자식 테이블에 FK가 포함됨
  - Unique key : pk 와 마찬가지로 중복을 허용하지 않는다. 해당 column 에 입력되는 데이터의 중복을 막기위해 사용하며 각각 column마다 지정가능하다, NULL 값을 허용한다.
 
 
 4. django에서 queryset과 object는 어떻게 다른지 서술하기
  - Queryset : 데이터베이스에서 전달받은 객체들의 list. 리스트와 구조는 같지만 파이썬 기본 자료구조가 아니므로 자료형 변환이 필요하다.
  - object : 모델 속성을 가지고 생성된 객체


 

 
   
