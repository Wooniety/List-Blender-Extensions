import bpy
import os
from .list_extensions import LISTBLENDEREXTENSIONS_Utilities

class LISTEXTENSIONS_Options(bpy.types.PropertyGroup):
	toggle_author: bpy.props.BoolProperty(name="Author", default=True)
	toggle_description: bpy.props.BoolProperty(name="Description", default=True)
	toggle_extensions_version_num: bpy.props.BoolProperty(name="Extension Version Number", default=True)
	toggle_blender_version_num: bpy.props.BoolProperty(name="Blender Version Number", default=True)
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
	
	filepath: bpy.props.StringProperty(subtype='FILE_PATH')
	filter_glob: bpy.props.StringProperty(default="*.csv;*.txt;*.json", options={'HIDDEN'})

	def invoke(self, context, event):
		self.props = context.scene.list_extensions_props

		self.extension_utils = LISTBLENDEREXTENSIONS_Utilities()	
		self.extension_utils.setFiletype(self.props.export_format.lower())
		self.filepath = self.extension_utils.setFilename()

		bpy.context.window_manager.fileselect_add(self)
		return {'RUNNING_MODAL'}

	def execute(self, context):
		# Set filters
		self.props = context.scene.list_extensions_props
		self.extension_utils.setToggleAuthor(self.props.toggle_author)
		self.extension_utils.setToggleExtensionVer(self.props.toggle_version_num)
		self.extension_utils.setToggleCategory(self.props.toggle_category)
		self.extension_utils.setToggleWebsite(self.props.toggle_website)
		self.extension_utils.setToggleEnabled(self.props.toggle_enabled)
		self.extension_utils.setToggleDefaultExtensions(self.props.toggle_default_extensions)
		self.extension_utils.setFiletype(self.props.export_format.lower())

		self.extension_utils.loadListOfAddons()

		self.extension_utils.printAddonList()
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
		layout.prop(props, "toggle_description")
		layout.prop(props, "toggle_extensions_version_num")
		layout.prop(props, "toggle_blender_version_num")
		layout.prop(props, "toggle_category")
		layout.prop(props, "toggle_website")

		layout.separator()

		layout.label(text="Export Options")
		layout.prop(props, "toggle_enabled")
		layout.prop(props, "toggle_default_extensions")
		layout.prop(props, "export_format")

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