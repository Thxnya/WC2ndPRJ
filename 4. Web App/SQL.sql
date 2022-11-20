-- member (멤버 테이블)
---- id (아이디, PK)
---- pwd (패스워드)


-- exchange_type (환율 종류 테이블)
---- exc_type (환율 종류, PK)


-- exchange (환율 테이블)
---- idx (인덱스, PK)
---- exc_type (환율 종류, FK)
---- exc_date (날짜)
---- exc (환율)


CREATE TABLE member (
    id VARCHAR2(10) PRIMARY KEY,
    pwd VARCHAR2(12) NOT NULL
);

CREATE TABLE exchange_type (
    exc_type VARCHAR2(20) PRIMARY KEY
);

CREATE TABLE EXCHANGE 
(
  IDX NUMBER(7, 0) NOT NULL 
, EXC_TYPE VARCHAR2(20 BYTE) 
, EXC_DATE DATE 
, EXC FLOAT(126) 
, CONSTRAINT EXCHANGE_PK PRIMARY KEY 
  (
    IDX 
  ));

ALTER TABLE EXCHANGE
ADD CONSTRAINT EXCHANGE_FK1 FOREIGN KEY
(
  EXC_TYPE 
)
REFERENCES EXCHANGE_TYPE
(
  EXC_TYPE 
)
ENABLE;

INSERT INTO member(
    id, pwd
) values (
    'user_sys', 'qwerty123'
);

INSERT INTO exchange_type (exc_type) values ('USDKRW');
INSERT INTO exchange_type (exc_type) values ('EURKRW');
INSERT INTO exchange_type (exc_type) values ('JPYKRW');
INSERT INTO exchange_type (exc_type) values ('CNYKRW');
INSERT INTO exchange_type (exc_type) values ('USDPHP');
INSERT INTO exchange_type (exc_type) values ('USDLAK');
INSERT INTO exchange_type (exc_type) values ('USDMMK');
INSERT INTO exchange_type (exc_type) values ('USDVND');

COMMIT;