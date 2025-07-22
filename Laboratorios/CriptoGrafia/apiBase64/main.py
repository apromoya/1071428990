
import uvicorn


def start():
    uvicorn.run(
        "apibase64:app",
        host="127.0.0.1",
        port=8070,
        reload=True
    )

def starss1():
    uvicorn.run(
    "apibase64:app",
    host="127.0.0.1",
    port=8070,
    reload=True,
    ssl_keyfile="key.pem",
    ssl_certfile="cert.pem"
    )

if __name__ == '__main__':
    #start()
    starss1()
