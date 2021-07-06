import uvicorn
from app import get_app

app = get_app()

if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=9966)
