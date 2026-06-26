import bpy
# from list_extensions import ListBlenderExtensions

class LISTEXTENSIONS_Options(bpy.types.PropertyGroup):
	toggle_author: bpy.props.BoolProperty(name="Author", default=True)
	toggle_version_num: bpy.props.BoolProperty(name="Version Number", default=True)
	toggle_category: bpy.props.BoolProperty(name="Category", default=False)
	toggle_website: bpy.props.BoolProperty(name="Website", default=False)

	toggle_enabled: bpy.props.BoolProperty(name="Only enabled extensions", default=False)
	toggle_default_extensions: bpy.props.BoolProperty(name="Include default extensions", default=False)

	export_format: bpy.props.EnumProperty(
		name="Format",
		description="Export file format",
		items=[
			('TXT', "Text", "Export as a plain text file"),
			('CSV', "CSV", "Export as comma-separated values"),
			('JSON', "JSON", "Export as JSON"),
		],
		default='TXT',
	)

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
		props = context.scene.list_extensions_props

		layout.label(text="Show Additional Info")
		layout.prop(props, "toggle_author")
		layout.prop(props, "toggle_version_num")
		layout.prop(props, "toggle_category")
		layout.prop(props, "toggle_website")

		layout.separator()

		layout.label(text="Export Options")
		layout.prop(props, "toggle_default_extensions")
		layout.prop(props, "export_format")
		layout.prop(props, "toggle_category")

		layout.operator("list_extensions.export_extensions")

def register():
	bpy.utils.register_class(LISTEXTENSIONS_Options)
	bpy.utils.register_class(LISTEXTENSIONS_OT_exportExtensions)
	bpy.utils.register_class(LISTEXTENSIONS_PT_Panel)
	bpy.types.Scene.list_extensions_props = bpy.props.PointerProperty(
		type=LISTEXTENSIONS_Options
	)

def unregister():
	del bpy.types.Scene.list_extensions_props
	bpy.utils.unregister_class(LISTEXTENSIONS_PT_Panel)
	bpy.utils.unregister_class(LISTEXTENSIONS_OT_exportExtensions)
	bpy.utils.unregister_class(LISTEXTENSIONS_Options)