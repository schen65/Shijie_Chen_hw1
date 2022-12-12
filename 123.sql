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

DROP TABLE IF EXISTS mytable;
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
    SELECT * FROM a INTO a;
    RAISE NOTICE 'a:%', a.a;
    RAISE NOTICE 'b:%', a.b;
    RAISE NOTICE 'c:%', a.c;
END $$

CREATE OR REPLACE VIEW myview as (
    select * FROM mytable
);

SELECT * FROM myview;
drop view IF EXISTS myview;
drop table mytable;
drop type composite_example;

drop TABLE if EXISTS a;
CREATE TABLE a (
    id int,
    var_1 int,
    var_2 INT
);

INSERT into a (id,var_1,var_2)
VALUES (1,2,3),(2,5,6),(3,5,8),(4,11,12);

SELECT * FROM a;

SELECT * FROM a WHERE id =2;

SELECT * from a where id =2 and var_1 =5;

update a set var_1 = var_1 + 100
where id =1;
SELECT * FROM a;

UPDATE a set (var_1, var_2) = (var_1 + 100, var_2 + 100)
where id = 2;
SELECT * FROM a;


UPDATE a set (var_1, var_2) = (SELECT var_1 + 100, var_2 +200 FROM a WHERE id =3)
WHERE id =4;

DELETE FROM a WHERE id = 1;

ALTER TABLE a ADD COLUMN var_3 INT;
SELECT * FROM a;

UPDATE a set var_3 = var_1 + var_2;

alter TABLE a DROP COLUMN var_3;

SELECT * FROM a;

DROP TABLE a;


CREATE TABLE a (
    col_a int,
    col_b int
);

INSERT into a (col_a, col_b)
VALUES (1,2), (2,3),(4,5), (5,6);


DO $$
DECLARE
    counter int = 0;
BEGIN 
    Loop
        counter = counter + 1;
        CONTINUE WHEN counter =5;
        RAISE NOTICE '%', counter;
        EXIT WHEN counter = 20;
    end Loop;
END $$;

DO $$
DECLARE
    counter int =0;
BEGIN
    WHILE counter <10 LOOP
        counter = counter + 1;
        CONTINUE WHEN counter =5;
        RAISE NOTICE '%', counter;
    END LOOP;
END $$;

DO $$
DECLARE 
    rec record;
BEGIN
    FOR rec IN (SELECT * FROM a) LOOP
        RAISE NOTICE  '% . %', rec.col_a,rec.col_b;
    END LOOP;
END $$;


DO $$
DECLARE
    val TEXT;
    col TEXT;
    query TEXT;
BEGIN
    FOR col IN (SELECT column_name
                FROM information_schema.columns
                WHERE table_name = 'a') LOOP
        query = 'SELECT DISTINCT ' || col || ' FROM a';
        FOR val IN EXECUTE query LOOP
            RAISE NOTICE '% %', col,val;
        END LOOP;
    END LOOP;
END $$;



DO $$
DECLARE
    counter int;
BEGIN
    FOREACH counter IN ARRAY ARRAY[1,2,3,4] LOOP
        RAISE NOTICE '%', counter;
    END LOOP;
END $$;


drop table if EXISTS c;

CREATE TABLE c ( a int ARRAY);
INSERT into c VALUES (ARRAY[1,2,3,4,5,6,7]);

DO $$
DECLARE
    counter int;
BEGIN
    FOREACH counter in ARRAY(SELECT * FROM c) LOOP
        RAISE NOTICE '%', counter;
    END LOOP;
END $$;





DROP TABLE IF EXISTS a;
DROP TABLE IF EXISTS b;
DROP TABLE IF EXISTS c;
CREATE TABLE a (id INT,col_a INT);
CREATE TABLE b (id INT,col_b INT);
CREATE TABLE c (id INT,col_c INT);
INSERT INTO a VALUES (1,100),(2,200),(3,300);
INSERT INTO b VALUES (2,400),(3,500),(4,600);
INSERT INTO c VALUES (1,700),(3,800),(4,900);


SELECT * FROM a;
SELECT * FROM b;
SELECT * FROM c;


SELECT * FROM a
INNER JOIN b ON a.id = b.id;

SELECT * FROM a
LEFT OUTER JOIN b ON a.id = b.id;

SELECT * FROM a
RIGHT OUTER JOIN b ON a.id = b.id;


SELECT INTERVAL '1 year 5 days'