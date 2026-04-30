from pydantic import BaseModel
from typing import List

class FacultyData(BaseModel):
    name: str
    email: str
    title: str
    department: str
    research_areas: List[str]
    university: str
    profile_url: str