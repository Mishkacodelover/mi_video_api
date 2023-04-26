from fastapi import FastAPI ,Body, Path, Query, Request, Depends ,HTTPException
from fastapi.responses import HTMLResponse , JSONResponse 
from pydantic import BaseModel, Field
from typing import Optional , List
from jwt_manager import create_token, validate_token
from fastapi.security import HTTPBearer

#la palabra Field importada es para añadir requerimientos a los campos, como puede ser
#un mínimo o máximo de caracteres, así como un número menor que (le)


app = FastAPI()
app.title = "Mi aplicación con FastAPI"
app.version = "0.0.1"

class JWTBearer(HTTPBearer):
    async def __call__(self, request : Request):
         auth = await super().__call__(request)
         data = validate_token(auth.credentials)
         if data['email'] != "admin@gmail.com" :
             raise HTTPException(status_code = 403, detail = "Credenciales invalidas")

class User(BaseModel):
    email :str
    password: str

class Movie(BaseModel):
    id: Optional[int]= None
    title: str = Field(min_lemgth=5,max_length=15)
    overview : str= Field(min_lemgth=5,max_length=50)
    year : int = Field( le= 2022)
    rating: float= Field( le= 10, ge=1)
    category: str= Field(min_lemgth=5,max_length=15)

    #si decidimos crear otra clase Config dentro de Movie de configuración de los campos, entonces no tenemos que
    # especificar en la clase Movie los default values de field(default="Mi película"), sino tan solo las restricciones
    class Config:
        schema_extra = {
            "example": {
                "id":1,
                "title": "Mi película",
                "overview": "Descripción peli",
                "year": 2022,
                "rating": 9.80, 
                "category":"Acción"
            }
        }

movies = [
    {
        'id': 1,
        'title': 'Avatar',
        'overview': "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        'year': '2009',
        'rating': 7.8,
        'category': 'Acción'    
    } ,
     {
        'id': 2,
        'title': 'Avatar',
        'overview': "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        'year': '2009',
        'rating': 7.8,
        'category': 'Acción'    
    } 
]

@app.get('/',tags=['Home'])
# los tags son para cambiar la palabraa 'default' que aparece que nuestro servidor cuando lo arrancamos en
#el navegador, sirve para agregar rutas también.
def message():
    return HTMLResponse('<h1>Hello world</h1>')

@app.post('/login',tags = ['auth'])
def login(user: User):
    if user.email == "admin@gmail.com" and user.password == "admin":
        token: str = create_token(user.dict())
    return JSONResponse(status_code = 200,content = token)

@app.get('/movies', tags=['movies'], response_model=List[Movie],status_code=200, dependencies =[Depends(JWTBearer())] )
def get_movies() -> List[Movie]:
    return JSONResponse(status_code = 200 ,content=movies)

@app.get('/movies/{id}',tags=['movies'], response_model=Movie)
def get_movie(id: int = Path(ge=1,le=2000)) -> Movie:
    for item in movies:
        if item["id"] == id:
            return JSONResponse(content= item)
    return JSONResponse(status_code = 404 ,content=[])

#si no le pasamos un parámetro en la url, entonces automáaticamente lo detecta como
#valor de query
# @app.get('/movies/', tags =['movies'])
# def get_movies_by_category(category:str, year: int):
#     return category

@app.get('/movies/', tags =['movies'],response_model=List[Movie])
def get_movies_by_category(category:str = Query(min_length=5, max_length=15)) -> List[Movie]:
   data = [item for item in movies if item['category']== category]
   return JSONResponse(content= data)

# @app.get('/movies/', tags =['movies'])
# def get_movies_by_category(category:str = Query(min_length=5, max_length=15)):
#     return [item for item in movies if item['category']== category]

# @app.post('/movies',tags=['movies'])
# def create_movie(id:int= Body(), title:str= Body(),overview:str= Body(),year:int= Body(),category:str= Body(), rating:float= Body()):
#     movies.append({
#         "id":id,
#         "title":title,
#         "overview":overview ,
#         'year': year,   
#         'rating': rating,
#         'category': category  
#    })
#     return movies
 #con el punto append, nos permite modificar el json en la api y por lo tanto añadir
 #o crear una nueva película.

# @app.put('/movies/{id}', tags=['movies'] )
# def update_movie(id:int, title:str= Body(),overview:str= Body(),year:int= Body(),category:str= Body(), rating:float= Body()):
#     for item in movies:
#         if item ["id"] == id:
#             item['title']  == title,     
#             item['overview']  == overview,     
#             item['year']  == year,     
#             item['category']  == category,     
#             item['rating']  == rating,
#             return movies  

@app.delete('/movies/{id}', tags=['movies'],response_model=dict, status_code = 200 )  
def delete_movie(id:int) -> dict:
    for item in movies:
        if item["id"] == id:
            movies.remove(item)
            return JSONResponse(status_code = 200,content={"message" : "Se ha eliminado la película"})

              
# @app.post('/movies',tags=['movies'])
# def create_movie(movie: Movie):
#     movies.append(movie)
#     return movies

@app.post('/movies',tags=['movies'],response_model=dict, status_code = 201 )
def create_movie(movie: Movie) -> dict:
    movies.append(movie)
    return JSONResponse(status_code = 201 ,content={"message" : "Se ha registrado la película"})

@app.put('/movies/{id}', tags=['movies'],response_model=dict , status_code = 200)
def update_movie(id:int, movie: Movie) -> dict:
    for item in movies:
        if item ["id"] == id:
            item['title']  == movie.title    
            item['overview']  == movie.overview     
            item['year']  == movie.year     
            item['category']  == movie.category    
            item['rating']  == movie.rating
            return JSONResponse(status_code = 200,content={"message" : "Se ha modificado la película"})