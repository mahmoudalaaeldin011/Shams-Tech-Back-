from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware

from schemas import ProjectRequest, ProjectResponse
from logic import calculate_solar_plan

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

projects_db = []


@app.post("/projects", response_model=ProjectResponse, status_code=status.HTTP_201_CREATED)
def create_project(request: ProjectRequest):
    if request.roof_area < 2.5:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Roof area is too small to install any solar panel."
        )

    plan = calculate_solar_plan(
        bills=request.monthly_bills,
        roof_area=request.roof_area,
        grid_type=request.grid_type
    )

    new_id = len(projects_db) + 1
    new_project = {
        "id": new_id,
        "client_name": request.client_name,
        "grid_type": request.grid_type,
        "roof_area": request.roof_area,
        "monthly_bills": request.monthly_bills,
        "average_bill": plan["average_bill"],
        "max_panels": plan["max_panels"],
        "recommended_inverter": plan["recommended_inverter"]
    }

    projects_db.append(new_project)
    return new_project


@app.get("/projects", response_model=list[ProjectResponse], status_code=status.HTTP_200_OK)
def get_all_projects(grid_type: str | None = None):
    if grid_type:
        filtered_projects = [p for p in projects_db if p["grid_type"] == grid_type]
        return filtered_projects
    return projects_db


@app.get("/projects/{project_id}", response_model=ProjectResponse, status_code=status.HTTP_200_OK)
def get_project_by_id(project_id: int):
    for project in projects_db:
        if project["id"] == project_id:
            return project

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Project with ID {project_id} not found."
    )