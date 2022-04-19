# fibonacci_api

### Requirements
- fastapi 0.75.1
- uvicorn 0.17.6

### Setup project
Create a virtual environment  
`python3 -m venv fibonacci_api`  

Activate virtual environment  
`source fibonacci_api/bin/activate`

Install dependencies  
`pip3 install -r requirements.txt` or `pip3 install fastapi==0.75.1 uvicorn==0.17.6`

### RUN server  
We need to move into fibonacci_api directory and execute the follow command:  
`uvicorn main:app`

#### API Doc
The API documentation is displayed visiting the following url:  
`http:127.0.0.1:8000/redoc`

### Endpoint
- http://127.0.0.1:8000/api/v1/fibonacci/

#### Test the API
For test the API, we need you make a request to `http://127.0.0.1:8000/api/v1/fibonacci/{index}` with a GET http method, followed of a index as documentation mentioned it.

###### Notes
1. La seria de Fibonacci comienza con los dígito 0 y 1, se repite el 1 y los siguientes es la suma de los dos elementos anteriores 0, 1, 1, 2, 3, 5, 8, 13, 21 ...
2. Puedo emplear una función recursiva que me permita obtener los primeros n elementos de la serie dado un número
3. Si deseo obtener el valor correspondiente a un índice, necesito trabajar con listas, tuplas
4. Podría utilizar funciones lambda?
5. Me gustaría implementar fastAPI ya que implementa documentación de api automáticamente, no es una tecnología que domine pero sería bueno aprovecharla para este ejercicio.
6. La creación de función de fibonacci debería de incluir una lista o comprenhension de listas
7. Estuve investigando y puedo implementar lambda y reduce or map, de esa manera obtengo un iterable y puedo acceder a sus elementos a través de un índice, además, con reduce ya obtengo el acumulativo de los dos elementos anteriores en la serie.
8. Decidí utilizar lambda y reduce
9. La función funciona correctamente, ahora debo exponer la API para pasar un indice y obtener el valor de esa posición
10. Para probar la API voy a usa Postman y el navegador Google Chrome

##### Test Ouput
- url: http://127.0.0.1:8000/api/v1/fibonacci/5/
- response: __{"fibonacci_value": 5}__  
  
- url: http://127.0.0.1:8000/api/v1/fibonacci/6/
- response: __{"fibonacci_value": 8}__
  
- url: http://127.0.0.1:8000/api/v1/fibonacci/3/
- response: __{"fibonacci_value": 2}__