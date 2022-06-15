# DRF_day1
DRF 특강 1일차 과제


 1. args, kwargs를 사용하는 예제 코드 짜보기
  - args_kwargs.py 참조  

 2. mutable과 immutable은 어떤 특성이 있고, 어떤 자료형이 어디에 해당하는지 서술하기
  - mutable : 수정 가능한 객체 (list, dict)
  - immutabel : 수정 불가능한 객체 (int, float, str, tuple)

 3. DB Field에서 사용되는 Key 종류와 특징 서술하기
 (1) Key(Index) 가장 일반적인 Key 는 DB 의 Index 와 동의어이다. Database 는 데이터의 검색을 위해 Index 를 색인으로 사용하므로 중요한 역할을 한다. 중복을 허용하며 NULL 등의 허용도 가능하지만 NULL 이 허용될 경우... 색인에 있어 비약적인 성능 저하를 가져오므로 일반적으로 Nullable 한 데이터의 경우 Indexing 하지 않는다. 단순히 Key, 즉 Index 로만 지정할 경우에는 별도에 제약조건(Constraint)을 가지지 않기 때문에 테이블 내에 데이터에 대해 엄격한 정합성이 요구될 경우에는 적합하지 않다.
 (2) Primary Key 일반적인 Key 는 Index 를 지칭하지만, 일반적으로 DB 설계를 할 때 Key 라고 하면 보통 PK 를 의미한다. NULL 을 허용하지 않고, Unique 성질을 지니므로 NOT NULL & UNIQUE 옵션이 포함되며 테이블 당 단 하나의 정의만 가질 수 있다. 즉, PK 로 단 하나의 칼럼이 지정되어 있다면 해당 칼럼의 데이터는 Table 내에서 유일성이 보장되며  여러 개가 PK 로 지정되어 있다면 해당 Key 들의 조합에 대해 유일성이 보장된다. 따라서 PK 는 같은 PK 를 갖는 행을 테이블 내에서 고유하게 만든다. 기본적으로 Index 성질 역시 보장되기 때문에 검색 시 색인의 Key 가 되며, Constraint 를 갖기 때문에 다른 테이블과 JOIN 을 할 때 기준 값으로 사용된다. RDB 의 특징적인 데이터 정합성의 보장과 Key 값의 성질을 갖기 때문에 일반적인 설계에서도 가장 선호되는 Key 타입이다.
 (3) Unique Key Unique Key 는 Uniqueness 를 지닌 Index를 말하며, Unique Index 라 부르기도 한다. PK 와 마찬가지로 중복성이 허용되지 않지만 NULL 에 대한 허용이 가능하다. 테이블 당 여러개를 가질 수 있다.
 (4) Foreign Key Foreign Key 란 JOIN 등으로 다른 DB 와의 Relation 을 맺는 경우, 다른 테이블의 PK를 참조하는 Column 을 FK 라고 한다. 여기서 Foreign Key Relation 을 맺는 다는 의미는 논리적 뿐 아니라 물리적으로 다른 테이블과의 연결까지 맺는 경우를 말하며, 이 때 FK 는 제약조건(Constraint)으로의 역할을 한다. Foreign Key Restrict 옵션을 줄 수 있고 다음과 같은 옵션들이 있다.  
 - RESTRICT : FK 관계를 맺고 있는 데이터 ROW 의 변경(UPDATE) 또는 삭제(DELETE) 를 막는다.  
 - CASCADE : FK 관계를 맺을 때 가장 흔하게 접할 수 있는 옵션으로, FK 와 관계를 맺은 상대 PK 를 직접 연결해서 DELETE 또는 UPDATE 시, 상대 Key 값도 삭제 또는 갱신시킨다.  이 때에는 Trigger 가 발생하지 않으니 주의하자.  
 - SET NULL : 논리적 관계상 부모의 테이블, 즉 참조되는 테이블의 값이 변경 또는 삭제될 때 자식 테이블의 값을 NULL 로 만든다. UPDATE 쿼리로 인해 SET NULL 이 허용된 경우에만 동작한다.  
 - NO ACTION : RESTRICT 옵션과 동작이 같지만, 체크를 뒤로 미룬다.  
 - SET DEFAULT : 변경 또는 삭제 시에 값을 DEFAULT 값으로 세팅한다.
 
 주로 PK 가 설계 시 많이 이용되지만, 정합성이 중요하지 않은 경우 Index 만 이용해서 테이블을 설계하기도 한다.UNIQUE Index 는 주로 복잡한 테이블에서 부분적인 정합성을 살리기 위해 많이 이용된다.
 FK 의 물리적 연결은 서버의 안정성을 위해 지양하는 편이 많다.상황에 알맞게 적합한 Key 를 잡아 설계하는 것이 최선의 튜닝 기법이라고 생각된다.


 4. django에서 queryset과 object는 어떻게 다른지 서술하기
  - Queryset : 데이터베이스에서 전달받은 객체들의 list. 리스트와 구조는 같지만 파이썬 기본 자료구조가 아니므로 자료형 변환이 필요하다.
  - 


 

 
   
