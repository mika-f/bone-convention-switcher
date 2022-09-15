# ----------------------------------------------------------------------------------------------------
#  Copyright (c) Natsuneko. All rights reserved.
#  Licensed under the GPLv3 License. Please read the https://docs.natsuneko.moe/en-US/limited-license
# ----------------------------------------------------------------------------------------------------

import typing

from bpy.types import Panel
from .operator import BoneConventionSwitcherOperator

class BoneConventionSwitcherUI(Panel):
  bl_idname: str = "UI_PT_BoneConventionSwitcher"
  bl_label: str = "Bone Convention Switcher"
  bl_space_type: typing.Union[int, str] = "VIEW_3D"
  bl_region_type: typing.Union[int, str] = "UI"
  bl_category: str = "Bone Convention Switcher"

  def draw(self, context):
    layout = self.layout

    column = layout.column()
    column.operator(BoneConventionSwitcherOperator.bl_idname, text="Switch Naming Convention")