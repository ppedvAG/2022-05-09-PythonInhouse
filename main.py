from typing import Optional
from fastapi import FastAPI, HTTPException

from pydantic import BaseModel

class User(BaseModel):
    user_id: str
    user_name: str
    user_email: Optional[str] = None


app = FastAPI()

userDict = {}


# Der Pfad über den wir die API ansprechen
@app.get("/greet")
async def root():
    return {"message": "Hello World"}

@app.get("/ids/{id}")
async def get_id(id: int):
    return {"id": id}
# Reihenfolge der Pfade ist wichtig
# Wenn wir /users/me und /users/user_id vertauschen wird immer die Rückgabe von /users/user_id zurückkommen
# da der Pfad als erstes gematcht wird
@app.get("/users/me")
async def get_user_me():
    return {"user_id" : "du"}

@app.get("/users/{user_id}")
async def get_user(user_id: str):
    user = userDict.get(user_id, 404)
    if user == 404:
        raise HTTPException(status_code=404, detail="User not found")
    else:
        return user

@app.post("/users/", status_code=201)
async def create_user(user: User):
    newUser = {
        "user_id": user.user_id,
        "user_name": user.user_name,
        "user_email": user.user_email
    }
    userDict.update({user.user_id : newUser})
    return user

@app.put("/users/update/{user_id}")
async def update_user(user_id: str, user: User):
    currentUser = userDict.get(user_id, 404)
    if currentUser == 404:
        raise HTTPException(status_code=404, detail="User not found")
    else:
        currentUser["user_name"] = user.user_name
        currentUser["user_email"] = user.user_email
        userDict.update({user_id : currentUser})
        return currentUser
    

@app.delete("/users/delete/{user_id}")
async def delete_user(user_id: str):
    del userDict[user_id]

