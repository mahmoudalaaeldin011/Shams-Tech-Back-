# main.py
from fastapi import FastAPI
from routers import projects  # بنستدعي الملف اللي عملناه فوق

app = FastAPI(title="Solar System API")

# بنربط الـ router بتاع المشاريع بالـ app الرئيسي
app.include_router(projects.router)

@app.get("/")
def root():
    return {"message": "السيرفر شغال وزي الفل ومقسّم باحترافية!"}