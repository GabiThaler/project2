from serrver import server1

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("serrver.server1:app", host="127.0.0.1", port=8001)
