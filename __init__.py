import bpy
# from list_extensions.py import ListBlenderExtensions

class LISTEXTENSIONS_OT_hello(bpy.types.Operator):
    bl_idname = "list_extensions.say_hello"
    bl_label = "Say Hello"
    bl_description = "Prints a message to the console"

    def execute(self, context):
        self.report({'INFO'}, "Hello from Blender Addon!")
        print("Hello from Blender Addon!")
        return {'FINISHED'}

class LISTEXTENSIONS_PT_Panel(bpy.types.Panel):
    bl_label = 'List Extensions'
    bl_id = 'LISTEXTENSIONS_PT_Panel'
    bl_category = "Tool"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'

    def draw(self, context):
        layout = self.layout
        layout.operator("LISTEXTENSIONS.say_hello")

def register():
    bpy.utils.register_class(LISTEXTENSIONS_OT_hello)

def unregister():
    bpy.utils.unregister_class(LISTEXTENSIONS_OT_hello)