
import uvicorn


def start():
    uvicorn.run(
        "apibase64:app",
        host="10.13.181.194",
        port=8070,
        reload=True
    )

if __name__ == '__main__':
    start()