# Esquemas

Libreria pidantyc

Nos ofrece esquemas grandes para tener datos con los que jugar.

1. Importamos libreria:

from pydantic import BaseModel

2. Se llama la clase:

class Movie(BaseModel)
id: int | None = None
title: str
overview : str
year : int
rating: float
category: str

Esta hereda de Base Model
