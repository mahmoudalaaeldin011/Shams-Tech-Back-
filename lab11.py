from pydantic import BaseModel , Field
from typing import Literal

class ProjectArea (BaseModel):
    model: str
    roof_area : float = Field (gt=0)
    grid_type : Literal["single_phase" , "three_phase"]
    monthly_bills : list[float] = Field (min_lingth = 1)

