from app import app as fastapi_app

def main():
    return fastapi_app

if _name_ == "_main_":
    import uvicorn
    uvicorn.run("server.app:app", host="0.0.0.0", port=7860)
