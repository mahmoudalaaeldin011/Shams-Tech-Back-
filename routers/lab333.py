from fastapi import FastAPI 
import lab222
from config import settings
app = FastAPI(
    title = settings.app_name ,
    version = "1.0.0"

      )

app.include_router(lab222.router)

@app.get("/system_info")
def root():
    
    return {
        "app_name" : settings.app_name,
        "database_location" : settings.database_url,
        "message": "السيرفر شغال وزي الفل ومقسّم باحترافية!"}