import uvicorn
from app import app

# rebuild   👈 you add this line

def main():
    uvicorn.run("app:app", host="0.0.0.0", port=8000)

if _name_ == "_main_":
    main()
