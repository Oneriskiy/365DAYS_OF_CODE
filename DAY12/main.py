from fastapi import FastAPI, HTTPException
import uvicorn
from pydantic import BaseModel


class Name(BaseModel):
    name: str


class Monument(BaseModel):
    title: str
    price: int


app = FastAPI()

monuments = {
        "granite": 15000,
        "marble": 35000,
        'limestone': 54000
     }


name = {
    "name": "guest"
    }


@app.get("/",
         summary="Username here",
         description="Returns the username",
         tags=['main', 'main_get']
         )
def main_get():
    if not name:
        raise HTTPException(status_code=404, detail='Not Found')
    return name


@app.post("/",
            summary="Username here",
            description="Gets the username",
            tags=['main', 'main_post']
)
def main_post(user: Name):
    name["name"] = user.name
    return {'message': f"Welcome! {name['name']}"}


@app.get("/monuments",
         summary='monuments here',
         description='gets all monuments',
         tags=['monuments', 'monuments_get'])
def func_monument():
    if not monuments:
        raise HTTPException(status_code=404, detail='Not found')
    return monuments


@app.post("/monuments",
            summary="monuments here",
            description = "receives all the monuments",
            tags=['monuments', 'monuments_post']
          )


def add_monument(monument: Monument):
    monuments[monument.title] = monument.price
    return {"message": f"Monument '{monument.title}' added", "monuments": monuments}


@app.put("/monuments/{title}")
def updater_monument(title: str, monument: Monument):
    if not title in monuments:
        raise HTTPException(status_code=404, detail="Not found")
    monuments[title] = monument.price
    return {'message': f"update! {title}, {monuments}"}


if __name__ == "__main__":
    uvicorn.run("main:app",
                host = '127.0.0.1',
                port = 5000,
                reload=True)

