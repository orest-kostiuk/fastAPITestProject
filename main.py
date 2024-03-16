from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/str_counter/{string}")
async def say_hello(string: str):
    chars = sum(c.isalpha() for c in string)
    numbers_count = sum(c.isdigit() for c in string)
    return {"message": f"String has {chars} characters and {numbers_count} numbers"}
