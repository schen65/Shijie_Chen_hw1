CREATE TYPE composite_example as (
    m INT,
    n TEXT
);

DO $$
DECLARE
    a SMALLINT;
    b INTEGER;
    c BIGINT;
    d NUMERIC;
    e REAL;
    f DOUBLE PRECISION;
    g VARCHAR(50);
    h CHAR(50);
    i TEXT;
    j BOOLEAN;
    k INTEGER ARRAY;
    l composite_example;
BEGIN
    a = 2;
    RAISE NOTICE 'a:%', a;
    b = 2222;
    RAISE NOTICE 'b:%', b;
    c = 2222222222;
    RAISE NOTICE 'c:%', c;
    d =  2.2;
    RAISE NOTICE 'd:%', d;
    e = 2.2;
    RAISE NOTICE 'e:%', e;
    f =222.2;
    RAISE NOTICE 'f:%', f;
    g = 'hello';
    RAISE NOTICE 'g:%', g;
    h = 'hello';
    RAISE NOTICE 'h:%', h;
    i = 'hello';
    RAISE NOTICE 'i:%', i;
    j = TRUE;
    RAISE NOTICE 'j:%', j;
    k = ARRAY[1,2,3,4,5,6,7,8];
    RAISE NOTICE 'k:%', k;
    l = (2, 'hello');
    RAISE NOTICE 'l:%', l;
END $$

CREATE TABLE mytable(
    a SMALLINT,
    b INTEGER,
    c BIGINT,
    d NUMERIC,
    e REAL,
    f DOUBLE PRECISION,
    g VARCHAR(50),
    h CHAR(50),
    i TEXT,
    j BOOLEAN,
    k INTEGER ARRAY,
    l composite_example
);


INSERT INTO mytable
VALUES (2,2222222,2222222222222,2.2,2.2,222.2,
'hello','hello','hello',true,'{1,2,3,4,5,6,7}',(2,'hello'));

SELECT * FROM mytable;


DO $$
DECLARE
    a record;
BEGIN
    SELECT * FROM mytable INTO a;
    RAISE NOTICE 'a:%', a.a;
    RAISE NOTICE 'b:%', a.b;
    RAISE NOTICE 'c:%', a.c;
END $$

DROP VIEW myview;
CREATE OR REPLACE VIEW myview as (
    select * FROM mytable
);

SELECT * FROM myview;
drop view myview;
drop table mytable;
drop type composite_example;