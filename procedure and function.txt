
-- procedure and Function

CREATE TABLE stud_marks(rollno number, name VARCHAR2(25),total_marks NUMBER);



CREATE TABLE result(roll_number NUMBER , name VARCHAR2(25), class VARCHAR2(30));


CREATE OR REPLACE PROCEDURE procedure_1 ( roll_no IN NUMBER, name IN VARCHAR2 ,marks IN NUMBER) AS
        BEGIN
                IF (marks<=1500 and marks>=990) THEN
                        DBMS_OUTPUT.PUT_LINE ('DISTINCTION');
                        INSERT INTO result VALUES (roll_no,name,'DISTINCTION');
                ELSIF (marks<=989 and marks>=900) THEN
                        DBMS_OUTPUT.PUT_LINE ('FIRST CLASS');
                        INSERT INTO result VALUES (roll_no,name,'FIRST CLASS');
                ELSIF (marks<=899 and marKs>825) THEN
                        DBMS_OUTPUT.PUT_LINE('HIGHER SECOND CLASS');
                        INSERT INTO result VALUES (roll_no,name,'HIGHER SECOND CLASS');
                ELSE
                        DBMS_OUTPUT.PUT_LINE ('FAIL');
                        INSERT INTO result VALUES (roll_no,name,'FAIL');

            END IF;
            INSERT INTO stud_marks VALUES (roll_no,name,marks);
    END procedure_1;
    /



    
CREATE OR REPLACE FUNCTION func_1(r IN NUMBER, n IN VARCHAR2,m IN NUMBER) RETURN VARCHAR2 AS
BEGIN
                procedure_1(r,n,m);
                return 'SUCCESSFULL';
END;
/







DECLARE
        name VARCHAR2(25);
        roll_no NUMBER;
        marks NUMBER;
        class VARCHAR2(25);

BEGIN
        roll_no:=&roll_no;
        name:='&name';
        marks:=&marks;
        class := func_1(roll_no,name,marks);
        dbms_output.put_line(class);
END;
/