from fastapi import FastAPI

app = FastAPI()

list_of_user = []

@app.get("/home/{user_name}")
def write_name(user_name: str):
    return {
        "Name" : user_name,
        "Age" : 94
    }

@app.put("/username/{user_name}")
def put_data(user_name: str):
    list_of_user.append(user_name)
    return{
        "usernames": user_name
    }

@app.post("/postdata")
def post_data(user_name: str):
    list_of_user.append(user_name)
    return {
        "usernames": list_of_user
    }

@app.delete('/deletedata/{user_name}')
def delete_data(user_name: str):
    list_of_user.remove(user_name)
    return{
        "usernames": list_of_user
    }

@app.api_route("/alldata",methods=['GET','PUT','POST','DELETE'])
def handle_alldata(username: str):
    return{
        "username": username
    }