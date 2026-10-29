from typing import Literal 
from pydantic import BaseModel , Field , PositiveFloat 

class ProjectRequest(BaseModel):
    client_name : str 
    grid_type : Literal ["220V", "380V"] 
    roof_area : float = Field (gt=0)
    monthly_bills : list[PositiveFloat] = Field(min_length=1)

class ProjectResponse(ProjectRequest):
    id: int
    client_name: str
    grid_type: str
    roof_area: float
    monthly_bills: list[float] 
    average_bill: float
    max_panels: int
    recommended_inverter: str



claint1 = ProjectRequest
