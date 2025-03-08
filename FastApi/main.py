from fastapi import FastAPI

app = FastAPI()

@app.get("/Perdomeo")
def obtener_datos():
    return {
        "name": "Juan",
        "age": 30,
        "city": "Madrid",
        "profesion": "Ingeniero",
        "active": True
    }