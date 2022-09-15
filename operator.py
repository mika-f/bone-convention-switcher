# ----------------------------------------------------------------------------------------------------
#  Copyright (c) Natsuneko. All rights reserved.
#  Licensed under the GPLv3 License. Please read the https://docs.natsuneko.moe/en-US/limited-license
# ----------------------------------------------------------------------------------------------------
import typing

import re
import bpy
from bpy.types import Operator

# Unity -> MMD
bone_convention: dict[str, str] = {
  "Hips" : "下半身",
  "Spine": "上半身",
  "Chest": "上半身2",
  "Neck": "首",
  "Head": "頭",
  "Shoulder.L": "左肩",
  "UpperArm.L": "左腕",
  "UpperArm.L.001": "左腕捩",
  "LowerArm.L": "左ひじ",
  "LowerArm.L.001": "左手捩",
  "Hand.L": "左手首",
  "UpperLeg.L": "左足",
  "LowerLeg.L": "左ひざ",
  "Foot.L": "左つま先",
  "Toes.L": "左足先EX",
  "LegIKP_L": "左足IK親",
  "LegIK_L": "左足ＩＫ",
  "ToeIK_L": "左つま先ＩＫ",
  "Shoulder.R": "右肩",
  "UpperArm.R": "右腕",
  "UpperArm.R.001": "右腕捩",
  "LowerArm.R": "右ひじ",
  "LowerArm.R.001": "右手捩",
  "Hand.R": "右手首",
  "UpperLeg.R": "右足",
  "LowerLeg.R": "右ひざ",
  "Foot.R": "右つま先",
  "Toes.R": "右足先EX",
  "LegIKP_R": "右足IK親",
  "LegIK_R ": "右足ＩＫ",
  "ToeIK_R": "右つま先ＩＫ",
  "Thumb Proximal.L": "左親指０",
  "Thumb Intermediate.L": "左親指１",
  "Thumb Distal.L": "左親指２",
  "Index Proximal.L": "左人指１",
  "Index Intermediate.L": "左人指２",
  "Index Distal.L": "左人指３",
  "Middle Proximal.L": "左中指１",
  "Middle Intermediate.L": "左中指２",
  "Middle Distal.L": "左中指３",
  "Ring Proximal.L": "左薬指１",
  "Ring Intermediate.L": "左薬指２",
  "Ring Distal.L": "左薬指３",
  "Little Proximal.L": "左小指１",
  "Little Intermediate.L": "左小指２",
  "Little Distal.L": "左小指３",
  "Thumb Proximal.R": "右親指０",
  "Thumb Intermediate.R": "右親指１",
  "Thumb Distal.R": "右親指２",
  "Index Proximal.R": "右人指１",
  "Index Intermediate.R": "右人指２",
  "Index Distal.R": "右人指３",
  "Middle Proximal.R": "右中指１",
  "Middle Intermediate.R": "右中指２",
  "Middle Distal.R": "右中指３",
  "Ring Proximal.R": "右薬指１",
  "Ring Intermediate.R": "右薬指２",
  "Ring Distal.R": "右薬指３",
  "Little Proximal.R": "右小指１",
  "Little Intermediate.R": "右小指２",
  "Little Distal.R": "右小指３",
}

caches: dict[str, re.Pattern] = {}

class BoneConventionSwitcherOperator(Operator):
  bl_idname: str = "object.bone_convention_switcher_operator"
  bl_label: str = "Bone Convention Switcher Operator"

  def is_match(self, key: str, name: str) -> bool:
    if key in caches:
      return caches[key].match(name)

    regex = re.compile("^" + key + "$", re.IGNORECASE)
    caches[key] = regex

    return self.is_match(key, name)

  def is_unity_name(self, name: str) -> bool:
    for key in bone_convention.keys():
      if self.is_match(key, name):
        return True

    return False

  def convert_unity_to_mmd(self, name: str) -> str:
    for key, value in bone_convention.items():
      if self.is_match(key, name):
        return value

    return name

  def convert_mmd_to_unity(self, name: str) -> str:
    candidates = [k for k, v in bone_convention.items() if v == name]
    if len(candidates) == 1:
      return candidates[0]
    return name

  def execute(self, context):
    bones = bpy.context.object.pose.bones

    for bone in bones:
      if hasattr(bone, "name"):
        old_name = bone.name

        if self.is_unity_name(old_name):
          bone.name = self.convert_unity_to_mmd(old_name)
        else:
          bone.name = self.convert_mmd_to_unity(old_name)

    return {'FINISHED'}