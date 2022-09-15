# ----------------------------------------------------------------------------------------------------
#  Copyright (c) Natsuneko. All rights reserved.
#  Licensed under the GPLv3 License. Please read the https://docs.natsuneko.moe/en-US/limited-license
# ----------------------------------------------------------------------------------------------------

bl_info = {
    "name": "Bone Convention Switcher",
    "author": "Natsuneko",
    "description": "Blender add-on for switching Blender Bones Naming Conventions between Unity and MMD",
    "blender": (3, 0, 0),
    "version": (1, 0, 0),
    "location": "3D View > Sidebar > Bone Convention Switcher",
    "warning": "",
    "category": "Generic"
}

if "bpy" in locals():
    import importlib
    importlib.reload(operator)
    importlib.reload(ui)
else:
    from . import operator
    from . import ui

    import bpy


classes = [
    operator.BoneConventionSwitcherOperator,
    ui.BoneConventionSwitcherUI
]


def register():
    for c in classes:
        bpy.utils.register_class(c)


def unregister():
    for c in classes:
        bpy.utils.unregister_class(c)


if __name__ == "__main__":
    register()
