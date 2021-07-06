import uvicorn
from app import get_app

app = get_app()

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=9966)
