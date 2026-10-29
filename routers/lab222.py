from fastapi import APIRouter , HTTPException , status , Depends
from pydantic import BaseModel , Field 
from typing import Literal , Optional

router = APIRouter (
    prefix = "/projects" , 
    tags = ["projectssss"]
)
projects_dp = []

class ProjectCreate(BaseModel):
    client_name: str
    grid_type: Literal["220V", "380V"]
    roof_area: float = Field(gt=0)
    monthly_bills: list[float] = Field (min_length=1)

def get_existing_project (project_id : int):
    for index , project in enumerate(projects_dp):
        if project["id"] == project_id :
            return {"project":project , "index" : index}
    raise HTTPException (
        status_code = status.HTTP_404_NOT_FOUND , 
        detail= f"المشروع غير موجود {project_id}"
    )



@router.post("/",status_code = status.HTTP_201_CREATED)
def created_projects (project : ProjectCreate):
    new_project = {
        "id" : len(projects_dp) +1 ,
        "claient_name" : project.client_name , 
        "gride_type" : project.gride_type ,
        "roof_area" : project.roof_area , 
        "monthly_bills" : project.monthly_bills
    }
    projects_dp.append(new_project)
    return {"meesage" : "project was append :" ,"project" : new_project} 

@router.get("/")
def list_project(gride_type : Optional [Literal["220V" , "380V"]] = None):
    if gride_type :
        filterd =[p for p in projects_dp if p["gride_type"] == gride_type ]
        return{"count": len(filterd) , "projects" : filterd}
    return{"count": len(projects_dp) , "projects" :projects_dp }

@router.get("/{project_id}")
def get_project_by_id(data : dict=Depends(get_existing_project)):
            return data["project"]
    
    

"""
@router.put("/{project_id}")
def update_project(project_id : int , updated_data : ProjectCreate):
    for index , project in enumerate(projects_dp):
        if project["id"] == projects_dp :
            projects_dp[index]={
                "id": project_id,
                "client_name": updated_data.client_name,
                "grid_type": updated_data.grid_type,
                "roof_area": updated_data.roof_area,
                "monthly_bills": updated_data.monthly_bills
            }
            return {"message": "تم تحديث المشروع بنجاح", "project": projects_dp[index]}
    raise HTTPException(
        status_code= status.HTTP_404_NOT_FOUND,
        detail= f"المشروع رقم {project_id} غير موجود لتعديله!"
    )

@router.delete ("/{project_id}" , status_code=status.HTTP_204_NO_CONTENT)
def delete_project (project_id : int):
    for index, project in enumerate(projects_db):
        if project["id"] == project_id:
            projects_db.pop(index)
            return
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"المشروع رقم {project_id} غير موجود لحذفه!"
    )
"""

@router.put("/{project_id}")
def update_project (updated_data :ProjectCreate , data : dict =Depends(get_existing_project)):
     index = data["index"]
     project_id = data["project"]["id"]
     projects_dp [index] ={
        "id" : project_id,
        "client_name": updated_data.client_name,
        "grid_type": updated_data.grid_type,
        "roof_area": updated_data.roof_area,
        "monthly_bills": updated_data.monthly_bills
     }
     return {"message": "تم تحديث المشروع بنجاح", "project": projects_dp[index]}

@router.delete("/{project_id}" , status_code=status.HTTP_204_NO_CONTENT)
def delete_project(data : dict = Depends(get_existing_project)):
     index =data["index"]
     projects_dp.pop(index)
     return 