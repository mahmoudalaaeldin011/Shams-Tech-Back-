# routers/projects.py
from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, Field
from typing import Literal, Optional

# بنعمل راوتر خاص بالمشاريع بدل app القديمة
router = APIRouter(
    prefix="/projects",  # بيثبت إن كل المسارات دي بتدأ بـ /projects أوتوماتيك
    tags=["Projects"]    # بتنظم شكل الـ Swagger بتخليهم تحت قسم واحد
)

# لستة مؤقتة للتخزين
projects_db = []

class ProjectCreate(BaseModel):
    client_name: str
    grid_type: Literal["220V", "380V"]
    roof_area: float = Field(gt=0)
    monthly_bills: list[float] = Field(min_length=1)

# مسار إنشاء مشروع
@router.post("/", status_code=status.HTTP_201_CREATED)
def create_project(project: ProjectCreate):
    new_project = {
        "id": len(projects_db) + 1,
        "client_name": project.client_name,
        "grid_type": project.grid_type,
        "roof_area": project.roof_area,
        "monthly_bills": project.monthly_bills
    }
    projects_db.append(new_project)
    return {"message": "تم إنشاء المشروع بنجاح", "project": new_project}

# مسار عرض الكل مع فلتر
@router.get("/")
def list_projects(grid_type: Optional[Literal["220V", "380V"]] = None):
    if grid_type:
        filtered = [p for p in projects_db if p["grid_type"] == grid_type]
        return {"count": len(filtered), "projects": filtered}
    return {"count": len(projects_db), "projects": projects_db}

# مسار جلب مشروع بالـ ID
@router.get("/{project_id}")
def get_project_by_id(project_id: int):
    for project in projects_db:
        if project["id"] == project_id:
            return project
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"المشروع رقم {project_id} غير موجود!"
    )