Title: Tipos de comandos SQL
Date: 2023-01-09 21:00
Category: SQL
Authors: Juan Manuel Díaz Nevado
Summary: Los comandos SQL pueden dividirse en 5 sub-lenguajes, los revisamos.


SQL (Structured Query Language) es el estándar de facto en lenguajes de
SGBD (Sistemas de Gestión de Bases de Datos).

Los tipos de comandos normalmente se estructuran en 5 categorías:

- DDL – Data Definition Language (Lenguaje de definición de datos)
- DQL – Data Query Language (Language de consulta de datos)
- DML – Data Manipulation Language (Lenguaje de manipulación de datos)
- DCL – Data Control Language (Lenguaje de control de datos)
- TCL – Transaction Control Language (Lenguaje de control de transacción)

![Sublanguage squema]({static}/images/sql-commands.png)

Algunos autores solo tienen en cuenta 3 categorías:

- DDL
- DML, donde se incluye el SELECT, este está en realidad un poco aparte,
ya que permite en algunos motores modificar estructuras o datos, pero
normalmente solo accede a los datos sin afectarlos. Una explicación
más detallada de esto se puede encontrar en
[esta](https://community.oracle.com/tech/developers/discussion/2451336/select-is-dml-or-dql)
respuesta del foro de Oracle.
- DCL, aquí se incluirían los comandos de control de transacciones, si bien es cierto
que podemos entender las acciones sobre transacciones como control de los datos,
ya que no los modificamos, controlamos si las modificaciones tienen efecto o no.
Aun así tienen poco que ver con los otros dos comandos, GRANT y REVOQUE, que gestionan
los permisos para ejecutar comandos de los otros lenguajes.



Visto esto es normal que algunos autores le den su propia "caja" al SELECT y
que separen GRANT y REVOQUE de COMMIT, ROLLBACK,...

## Recursos para saber mas

### DBA Dixit
Este blog tiene una miriada de artículos con todo lo que hay que saber
sobre SQL.

- [Ir](https://dbadixit.com/)

### w3Schools
Una de las paginas mas grandes con tutoriales gratuitos sobre casi todo los lenguajes.

- [Ir](https://www.w3schools.com/sql/)