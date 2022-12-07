# TRABAJO PRACTICO FINAL PROGRAMACION ORIENTADA A OBJETOS

## INTRODUCCION

### **Bases de datos**:

Precios claros es un conjunto de datasets realizado a partir de los precios provistos por el gobierno de los productos en las distintas cadenas de supermercados. Este parte de la iniciativa de la Dirección Nacional de Defensa del Consumidor de que los consumidores cuenten con mayor información a la hora de tomar decisiones con respecto a los productos que adquieren. Particularmente estos dataset pertenecen al año 2020, lo cual es importante tener en consideracion a la hora de mirar los precios dada su elevada diferencia con la actualidad.

La base de datos seleccionada cuenta con 6 datasets: uno de productos, uno con las sucursales y 3 con los precios de abril en distintos periodos, los cuales fueron relevados de la página del gobierno mediante técnicas de scraping por Open Data Córdoba, y por otro lado uno adicional que contiene las provincias y codigos de las mismas.

**Link**: <https://www.kaggle.com/datasets/tinnqn/precios-claros-precios-de-argentina?select=sucursales.csv>

### **Variables:**
A continuacion se da una breve definicion de cada variable en el dataset precios claros, el cual se utilizara a lo largo de toda la investigacion.

**Producto**
- `id` , `productos_id`: numero de identificacion del producto.
- `categoria`: categoria del producto (nuestros productos son los que forman parte de la canasta basica: Agua, Leche, Arroz, Harinas y Pastas).
- `marca`: marca del producto.
- `presentacion`: presentacion del producto en cantidad (numeros).
- `unidad_presentacion`: unidad de medida de la presentacion (cc, lt, kg o gr).
- `precio`: precio del producto en el 2020.

**Sucursal/Comercio**
- `sucursal_id`: numero de identificacion de la sucursal del producto.
- `sucursalTipo` , `tipo_comercio`: tipo de comercio de la sucursal (Supermercado, Hipermercado o Autoservicio).
- `cadena`: es la cadena de supermercado en la que se vende el producto. Este es el target de nuestro modelo, por ello seleccionamos 3 cadenas con distintas categorias: Disco dirigido a personas de alto poder adquisitivo, que es de alta categoria, Hipermercado Carrefour a personas poder adquisitivo medio y Supermercados DIA de menor poder adquisitivo).


**Variable dependiente ->** es el target mencionado, el cual depende del resto de variables: `cadena`

**Variables independientes ->** son las variables que nos van a permitir predecir el target, es decir, todo el resto de variables mencionadas: `categoria`, `marca`, `presentacion`, `unidad_presentacion`, `precio` y `tipo_comercio`.

### **Objetivo:**
El objetivo de este trabajo es poder analizar los precios de los diferentes tipos de productos de la canasta basica, teniendo en cuenta la categoria, marca, tipo de cadena, presentacion y cadena en el que se realiza la venta del producto, para poder evaluar en que comercios y que marcas tienen los productos mas baratos.

Ademas, la idea es crear un modelo de regresion logistica que nos permita predecir en base a las variables a cual cadena pertenece el producto, ya sea Disco, Hipermercado Carrefour o Supermercados DIA. Dado que pertenecen a diferentes categorias de supermercados, sus consumidores objetivo son distintos, por lo que sus precios tambien varian.

Es por eso que el objetivo del modelo es predecir a cual de ellos pertenece el producto.

### **Hipotesis:**
Respecto a las variables seleccionadas se espera poder ver que en el comercio de Disco, dado que es una cadena dirigido a personas de alto poder adquisitivo, sus productos tambien tendran mayores precios. Lo mismo sucedera son Supermercados DIA que al ser una cadena dirigida a consumidores de menor poder adquisitivo que los anteriores, se espera encontrar que sus precios tambien son menores, mientras que en Carrefour se espera encontrar un precio intermedio que en los dos anteriores.

### **Tranformaciones a realizar:**
- **Load & Merge**
En primera instancia se van a cargar todos los datasets, para luego poder unirlos y filtrarlos segun los datos necesarios para el analisi, en este caso, las categorias de productos de canasta basica: Agua, Leche, Arroz, Harinas y Pastas, y la cadena de comercio: Disco, Hipermercado Carrefour y Supermercados Dia. Ademas, como para nuestro modelo necesitamos la columna de presentacion separado de la unidad en la que esta medido, separaremos la columna en esta instancia. El dataframe resultante es el que sera utilizado para el trabajo, el cual se llamara `precios_claros`.


- **Preprocesamiento**
Una vez listo el dataset es necesario realizar un preprocesamiento de los datos. En esta instancia se evaluaran los posibles nulos en nuestras variables realizar el tratamiento adecuado de los mismos (drop, imputer, etc), y se evaluaran tambien los podibles duplicados y outliers.

- **Analisis Inicial**
Se muestar un analisis de nuestros datos, evaluando tendencias, frequencias, etc, con el objetivo de tener un mejor conocimiento de los datos a tratar.

- **Escalado**
Se escalan las variables numericas `precio` y `presentacion` para que sean comparables entre si, a pesar de que su rango de datos en primera instancia sea distinto.

- **Encoding**
Se tratan las variables categorias, creando distintas columnas binarias con la presencia o no de la variable en el producto. Esto es fundamental para el modelo bucado. Ademas, aplicamos el encoding a la variable target.

- **Modelo**
Realizamos el primer modelo de regresion logistica y obtenemos un score mediante un cross validation, el cual se irá mejorando mediante diferentes métodos para lograr un accuracy mas elevado. Haremos una matriz de confusion y veremos accuracy, precision y recall.
Ademas haremos la prediccion de una instancia que no existe para probarlo.

