import bpy
# from list_extensions.py import ListBlenderExtensions

class LISTEXTENSIONS_(bpy.types.Operator):
    bl_idname = "list_extensions.export_extensions"
    bl_label = "Export"

    def execute(self, context):
        return {'FINISHED'}

class LISTEXTENSIONS_OT_exportExtensions(bpy.types.Operator):
    bl_idname = "list_extensions.export_extensions"
    bl_label = "Export"

    def execute(self, context):
        return {'FINISHED'}

class LISTEXTENSIONS_PT_Panel(bpy.types.Panel):
    bl_label = 'List Extensions'
    bl_idname = 'LISTEXTENSIONS_PT_Panel'
    bl_category = "Tool"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'

    def draw(self, context):
        layout = self.layout
        layout.label(text="Show Additional Info")
        layout.separator()
        layout.prop(context.object, "list_extensions.toggle_author", text="Author")
        layout.prop(context.object, "list_extensions.toggle_vernum", text="Version No.")
        layout.prop(context.object, "list_extensions.toggle_category", text="Category")
        layout.prop(context.object, "list_extensions.toggle_website", text="Website")
        layout.label(text="Export As")
        layout.seperator(context.object, "Filter Only Enabled Extensions")
        layout.operator("list_extensions.export_extensions")

def register():
    bpy.utils.register_class(LISTEXTENSIONS_OT_exportExtensions)
    bpy.utils.register_class(LISTEXTENSIONS_PT_Panel)

def unregister():
    bpy.utils.unregister_class(LISTEXTENSIONS_PT_Panel)
    bpy.utils.unregister_class(LISTEXTENSIONS_OT_exportExtensions)