# [SQL](https://www.w3schools.com/sql)

## Grundlagen

### [NoSQL (Not only SQL)](https://en.wikipedia.org/wiki/NoSQL)

### [ACID](https://en.wikipedia.org/wiki/ACID)

* **A**tomicity
* **C**onsistency
* **I**solation
* **D**urability

### [CAP theorem](https://en.wikipedia.org/wiki/CAP_theorem)

* **C**onsistency
* **A**vailability
* **P**artition tolerance


## [Normalisierung](https://de.wikipedia.org/wiki/Normalisierung_(Datenbank))

Ziel: Konsistenzerhöhung durch Redundanzvermeidung


### [Erste Normalform (1NF)](https://de.wikipedia.org/wiki/Normalisierung_(Datenbank)#Erste_Normalform_(1NF))

Jedes Attribut der Relation muss einen **atomaren Wertebereich** haben, und die Relation muss **frei von Wiederholungsgruppen** sein

> Lösung: atomare Attributwertebereiche
* Felder (Spalten) mit zusammengesetzten Typen aufspalten -> atomaren Wertebereich
* -> Aus Datenbankeinträgen mit Listen (Wiederholungsgruppen) können mehrere Einträge werden


### [Zweite Normalform (2NF)](https://de.wikipedia.org/wiki/Normalisierung_(Datenbank)#Zweite_Normalform_(2NF))

Nichtschlüsselattribute müssen von **allen** Schlüsseln vollständig abhängen

> Lösung: Tabellen aufteilen


### [Dritte Normalform (3NF)](https://de.wikipedia.org/wiki/Normalisierung_(Datenbank)#Dritte_Normalform_(3NF))

Keine funktionalen Abhängigkeiten der Nichtschlüssel-Attribute untereinander (transitive Abhängigkeiten)

> Lösung: Tabellen weiter aufteilen


## [Quick Reference](https://www.w3schools.com/sql/sql_quickref.asp)

### CREATE TABLE

```
CREATE TABLE table_name
(
column_name1 data_type,
column_name2 data_type,
column_name3 data_type,
)
```

### INSERT INTO
```
INSERT INTO table_name
(column1, column2, column3,...)
VALUES (value1, value2, value3,....)
```

### UPDATE
```
UPDATE table_name
SET column1=value, column2=value,...
WHERE some_column=some_value
```

### SELECT + [WHERE](https://www.w3schools.com/sql/sql_where.asp)
```
SELECT column_names
FROM table_name
WHERE column_name operator value
```

### [SQL Operators](https://www.w3schools.com/sql/sql_operators.asp)

#### Logical Operators

* AND, OR, NOT
* *ANY, SOME, IN, ALL*

#### Comparison Operators

* =, >, <, >=, <=, <>

#### Arithmetic Operators

* +, -, \*, /, %

#### [Date/Time-Functions](https://www.w3schools.com/SQL/func_mysql_now.asp)

z.B.
`NOW()`

### SELECT + [DISTINCT](https://www.w3schools.com/sql/sql_distinct.asp) + LIMIT
```
SELECT (DISTINCT) column_names
FROM table_name
WHERE conditions
(LIMIT n)
```


### SELECT + [ORDER BY](https://www.w3schools.com/sql/sql_orderby.asp)
```
SELECT column_names
FROM table_name
WHERE column_name operator value
ORDER BY column1, column2, ... ASC|DESC;
```


### SELECT + WHERE + [LIKE](https://www.w3schools.com/sql/sql_like.asp)

```
SELECT column_names
FROM table_name
WHERE column_name LIKE pattern
```

#### [Wildcards](https://www.w3schools.com/sql/sql_wildcards.asp)

| Wildcard | Bedeutung |
| -------- | --------- |
| **%** | Ein oder mehrere beliebige Zeichen |
| **_** | Ein einzelnes Zeichen |
| [weitere](https://www.w3schools.com/sql/sql_wildcards.asp) ||


### [SELECT + GROUP BY](https://www.w3schools.com/sql/sql_groupby.asp) (+ [HAVING](https://www.w3schools.com/sql/sql_having.asp))
```
SELECT column_names, aggregate_function(column_name)
FROM table_name
WHERE column_name operator value
GROUP BY column_name
(HAVING condition)
```

#### [Aggregate Functions](https://www.w3schools.com/sql/sql_aggregate_functions.asp)
MIN(), MAX(), COUNT(), SUM(), AVG()


### JOIN
```
SELECT column_name(s)
FROM table_name1
INNER JOIN table_name2
ON table_name1.column_name=table_name2.column_name
```


### [Joins](https://www.w3schools.com/sql/sql_join.asp)

![](https://www.w3schools.com/sql/img_inner_join.png)
![](https://www.w3schools.com/sql/img_left_join.png)
![](https://www.w3schools.com/sql/img_right_join.png)
![](https://www.w3schools.com/sql/img_full_outer_join.png)


#### [Natural Join](https://www.w3resource.com/sql/joins/natural-join.php)



## SQL Injections

* [Beispiel](https://github.com/johannesloetzsch/LF7/tree/main/src/examples/rest/python)
* [SQL Injection Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html)
* [CTF](https://juice-shop.herokuapp.com/) [doc/src](https://owasp.org/www-project-juice-shop/)
