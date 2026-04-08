from fastapi import FastAPI
from pydantic import BaseModel
from environment import CloudEnv

app = FastAPI()
env = CloudEnv()

class Action(BaseModel):
    action: str

@app.post("/reset")
def reset():
    state = env.reset()
    return {"state": state}

@app.post("/step")
def step(action: Action):
    state, reward, done = env.step(action.action)
    return {
        "state": state,
        "reward": reward,
        "done": done
    }

@app.get("/state")
def get_state():
    return {"state": env.state}

# ✅ ADD THIS PART
@app.get("/")
def home():
    return {"message": "Cloud Server Environment Running"}
