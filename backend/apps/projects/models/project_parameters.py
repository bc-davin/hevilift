from typing import Optional
from datetime import datetime
from projects import ProjectBase


class ProjectParameters(ProjectBase):
    def __init__(self, project_rev_id, project_id, project_name, location, city, client):
        super().__init__(project_rev_id, project_id, project_name, location, city, client)

        self.revision_description: Optional[str] = None
        self.uom: Optional[str] = None
        self.udom_weight: Optional[str] = None
        
        self.sim_time:Optional[datetime] = None
        self.acpo_is_running: bool = False
        self.asico_is_running: bool = False

        self.mat_install_remove_cost_per_fts: Optional[float] = None
        self.mat_rental_cost_per_fts2:Optional[float] = None
        self.ground_prep_cost_per_fts2:Optional[float] = None

        self.delete_previous_data: bool = False
        self.bypass_boundary_offset: bool = False

        self.rl_n_epsiodes:Optional[float] = None
        self.rl_num_features: Optional[float] = None
        self.rl_update_hop:Optional[float] = None
        self.rl_pp_mode:Optional[str] = None
        self.run_rl_continue:bool= False