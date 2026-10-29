from fastapi import FastAPI , status , HTTPException 
from pydantic import BaseModel , Field 
from typing import Literal 
from fastapi.middleware.cors import CORSMiddleeare

app = FastAPI()

app.add_middleware(
     CORSMiddleeare,
    allow_origins=["*"], # مين مسموح ليه؟
    allow_credentials=True,
    allow_methods=["*"], # أنواع الطلبات (GET, POST, PUT, DELETE...) مسموح بيها كلها
    allow_headers=["*"], # الـ Headers كلها مسموحة
)

class ProjectCreate(BaseModel):
    client_name: str
    grid_type: Literal["220V", "380V"]
    roof_area: float = Field(gt=0)
    monthly_bills: list[float] = Field (min_length=1)

class ProjectResponse(BaseModel):
        project_id: int
        client_name: str
        estimated_kw: float


@app.get("/")
def home():
    return {"meesage" : "شغال "}

@app.get("/panels")
def get_panels ():
    return [
        {"brand": "Jinko", "watt": 550},
        {"brand": "Canadian Solar", "watt": 600}
    ]

@app.post("/create-project")
def create_projectt():
    return {"status": "success", "message": "تم استلام المشروع بنجاح!"}

@app.get("/projects/{project_id}")
def get_project(project_id : int):
    if project_id!= 1 :
         raise HTTPException(
              status_code=404 ,
              detail= "عفواً، هذا المشروع غير موجود!"
         )
    return {"Meesage": f"انت طلبت  {project_id}"}

@app.get ("/search-panels")
def search_panels(city : str = "cairo"):
    return {"Search in :" : city}


@app.post ("/projectss", response_model =  ProjectResponse ,status_code=status.HTTP_201_CREATED )
def create_project (project : ProjectCreate):
    calculated_kw = project.roof_area * 0.15
    return ProjectResponse(
        project_id=1,
        client_name=project.client_name,
        estimated_kw=calculated_kw
    )
