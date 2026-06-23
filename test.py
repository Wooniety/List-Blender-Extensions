import bpy
import addon_utils

print("trying")
for addon in addon_utils.modules():
    try:
        name = addon.__name__
        enabled = addon.__addon_enabled
        print(f"{name}")
        print(enabled)
        print(addon_utils.module_bl_info(addon))
    except:
        pass
print("complete")
