# Put operation means updating a record. Likewise, to delete a record we need to send a delete a request
from fastapi import FastAPI
# pydantic will be for data validation. Whever, we are sending a data, it will be trying to validate with the help of pydantic class
from pydantic import BaseModel

# Object of fastapi class
app = FastAPI()

user_db = {
    1:{"name":"anshul", "age": 30},
    2:{"name":"aggagag", "age": 78},
    3:{"name":"gshsgshg", "age": 5}
}


class User(BaseModel):
    name: str
    age: int 



@app.put("/user_db/data/v1/update/{user_id}")
def user_update(user_id:int, user:User):
    if user_id in user_db:
        user_db[user_id] = user.dict()
        print(user_db)
        return{"message": "User Updated succesfully", "user":user_db[user_id]}
    else:
        return {"message":"user not found"}
    


@app.delete("/user_db/data/v1/update/{user_id}")
def delete_user(user_id:int):
    if user_id in user_db:
        del user_db[user_id]
        print(user_db)
        return{"message": "User Deleted succesfully"}
    else:
        return {"message":"user not found"}
    
