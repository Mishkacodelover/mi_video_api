# Creación de tokens con python

Para crear los tokens utilizamos la librería jwt para python.
La instalamos:

pip install pyjwt

1. Hay que crear un archivo aparte de token manager donde se le dan la instrucciones para codificar la contraseña:

```python
def create_token(data: dict):
    token : str = encode(payload = data ,key = "my_secret_key", algorithm = "HS256")
    # el algoritmo de creación nos lo sugiere la librería
    return token


```

2. Se crea con una clase en el archivo main:

class User(BaseModel):
email :str
password: str

3. Y se crea una ruta de login:

```python

@app.post('/login',tags = ['auth'])
def login(user: User):
    if user.email == "admin@gmail.com" and user.password == "admin":
        token: str = create_token(user.dict())
    return JSONResponse(status_code = 200,content = token)

```

4. Creamos una instrucción en el archivo que gestiona el token, para decodificarlo también:

```python

def validate_token(token: str) -> dict:
    data: dict = decode(token, key:"my_secret_key", algorithms = ['HS256'])
    return data

```

5. Para pasar la autenticación del usuario registrado, es decir el tokem, tenemos que crear un Bearer, lo hacemos con una función asíncrona:

```python

class JWTBearer(HTTPBearer):
    async def __call__(self, request : Request):
         auth = await super().__call__(request)
         data = validate_token(auth.credentials)
         if data['email'] != "admin@gmail.com" :
             raise HTTPException(status_code = 403, detail = "Credenciales invalidas")

```

6. Después añadimos como requerimiento ese Bearer a la ruta que querramos,lo pasamos como dependecies, por ejemplo:

```python

@app.get('/movies', tags=['movies'], response_model=List[Movie],status_code=200, dependencies =[Depends(JWTBearer())] )
def get_movies() -> List[Movie]:
    return JSONResponse(status_code = 200 ,content=movies)

```

En FastApi aparecerá un candado al lado de la ruta, pinchamos sobre él y copiamos el token que hemos generado al loguearnos.
