from typing import Dict, Optional
from datetime import datetime

class ProjectBase:
    def __init__(self, project_rev_id: int, project_id: int, project_name: str, location: str, city:str, client: str):
        self.project_rev_id = project_rev_id
        self.project_id = project_rev_id
        self.project_name = project_name
        self.location = location
        self.city = city
        self.client = client

        #flexible storage for other columns
        self.additional_columns = Dict(str, str)= {}
    
    