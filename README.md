# Challenge-LATAM-CM

Este repositorio contigo codigos (Carpeta SRC), que miden el tiempo y uso de memoria de 3 funciones, como parte de mi proceso de postulacion para un cargo laboral en LATAM.

Este poryecto contempla los siguientes ejercicios con ciertas condiciones:

1. Las top 10 fechas donde hay más tweets. Mencionar el usuario (username) que más publicaciones tiene por cada uno de esos días.
1.1 Debe incluir las siguientes funciones:
```python
def q1_time(file_path: str) -> List[Tuple[datetime.date, str]]:
```
```python
def q1_memory(file_path: str) -> List[Tuple[datetime.date, str]]:
```
```python
Returns: 
[(datetime.date(1999, 11, 15), "LATAM321"), (datetime.date(1999, 7, 15), "LATAM_CHI"), ...]
```

2. Los top 10 emojis más usados con su respectivo conteo.
  2.1 Debe incluir las siguientes funciones:   
```python
def q2_time(file_path: str) -> List[Tuple[str, int]]:
```
```python
def q2_memory(file_path: str) -> List[Tuple[str, int]]:
```
```python
Returns: 
[("✈️", 6856), ("❤️", 5876), ...]
```

3. El top 10 histórico de usuarios (username) más influyentes en función del conteo de las menciones (@) que registra cada uno de ellos.
  3.1 Debe incluir las siguientes funciones:
```python
def q3_time(file_path: str) -> List[Tuple[str, int]]:
```
```python
def q3_memory(file_path: str) -> List[Tuple[str, int]]:
```
```python
Returns: 
[("LATAM321", 387), ("LATAM_CHI", 129), ...]
```


En la carpeta "SRC", se encuentran para cada ejercicio, denominados Q1, Q2 y Q3, los codigos de las funciones. En el archivo Challange, se encuentras estos mismo, corridos para evaluar resultados.
