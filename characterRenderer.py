bl_info = {
	"name": "Character renderer for 2d games",
	"description": "Character renderer for 2d games",
	"author": "Denis Cera",
	"version": (1, 0),
	"blender": (2, 69, 0),
	"location": "Toolshelf",
	"warning": "", # used for warning icon and text in addons panel
	"wiki_url": "",
	"category": "Render"}

import bpy
from bpy.props import *
from math import radians
from os.path import join

bpy.types.Scene.save_path = StringProperty(
	name = "Save Path",
	default = "//SAVE_PATH")
	
bpy.types.Scene.camera_angles = IntProperty(
	name = "Camera Angles", 
	description = "Enter number of render directions",
	default = 8)

bpy.types.Scene.rig_name = StringProperty(
	name = "Rig Name", 
	description = "Enter name of the rig that will be rendered",
	default = "rig")
	
class RenderAllActions(bpy.types.Operator):
	bl_idname = "scene.render_allactions"
	bl_label = "Character Renderer"
	bl_options = {'REGISTER', 'UNDO'}
	
	def execute(self, context):
		scn = context.scene
		S = bpy.context.scene

		renderFolderInitial = scn.save_path

		startFrame = 0
		endFrame  = 0 # frames
		numAngles = scn.camera_angles
		rotAngle  = 360 / numAngles
		all_render_layers = S.render.layers
		render_layers = []
		
		for layer in all_render_layers:
			if layer.use == True:
				render_layers.append(layer)
		
		selection_names = bpy.context.selected_objects
		print (selection_names)
		
		all_actions = bpy.data.actions
		render_actions = []
		
		for action in all_actions:
			if action.use_fake_user == True:
				render_actions.append(action)
				
		for action in render_actions:
			S.objects.active = bpy.data.objects[scn.rig_name]
			
			rig = bpy.data.objects[scn.rig_name]
			
			S.objects.active = bpy.data.objects[scn.rig_name]
			
			rig.animation_data.action = bpy.data.actions.get(action.name)
			
			camParent = bpy.data.objects['Empty']
			
			endFrame = int(action.frame_range[1])-1
			renderFolderAction = "{}/{}/".format(renderFolderInitial,action.name)

			for layer in render_layers:
				layer.use = True
					
				for i in range(numAngles):
					angle = i * rotAngle
					camParent.rotation_euler.z = radians( angle )
					renderFolder = "{0}angle_{1}/{2}".format(renderFolderAction, angle, layer.name)

					for f in range(startFrame,endFrame + 1):
						S.frame_set( f )

						frmNum   = str( f-startFrame ).zfill(3) 
						fileName = "{l}_angle_{a}_frm_{f}".format( l = layer.name, a = angle, f = frmNum)
						fileName += S.render.file_extension
						S.render.filepath = join( renderFolder, fileName )

						bpy.ops.render.render(write_still = True)
				layer.use = False
			
		camParent.rotation_euler.z = 0
		return {'FINISHED'}

class FakeAllActions(bpy.types.Operator):	
	bl_idname = "scene.fake_all_actions"
	bl_label = "FakeAllActions"
	bl_options = {'REGISTER', 'UNDO'}
	
	def execute(self, context):
		for action in bpy.data.actions:
			action.use_fake_user = True
		return {'FINISHED'}

class UnfakeAllActions(bpy.types.Operator):	
	bl_idname = "scene.unfake_all_actions"
	bl_label = "UnfakeAllActions"
	bl_options = {'REGISTER', 'UNDO'}
	
	def execute(self, context):
		for action in bpy.data.actions:
			action.use_fake_user = False
		return {'FINISHED'}
		
class EnableAllRenderLayers(bpy.types.Operator):	
	bl_idname = "scene.enable_all_render_layers"
	bl_label = "EnableAllRenderLayers"
	bl_options = {'REGISTER', 'UNDO'}
	
	def execute(self, context):
		for layer in bpy.context.scene.render.layers:
			layer.use = True
		return {'FINISHED'}
		
class DisableAllRenderLayers(bpy.types.Operator):	
	bl_idname = "scene.disable_all_render_layers"
	bl_label = "DisableAllRenderLayers"
	bl_options = {'REGISTER', 'UNDO'}
	
	def execute(self, context):
		for layer in bpy.context.scene.render.layers:
			layer.use = False
		return {'FINISHED'}

class CreateRenderAllActionsPanel(bpy.types.Panel):
	bl_label = "Character Renderer"
	bl_space_type = "VIEW_3D"
	bl_region_type = "TOOLS"
	bl_category = "Character Renderer"
		
	def draw(self, context):
		layout = self.layout
		ob = context.active_object
		scn = context.scene
		view = context.space_data
		layout.prop(scn, 'save_path')
		layout.prop(scn, 'rig_name')
		layout.prop(scn, 'camera_angles')

		layout.operator("scene.fake_all_actions", text="Fake All Actions")
		layout.operator("scene.unfake_all_actions", text="Unfake All Actions")
		layout.separator()
		layout.operator("scene.enable_all_render_layers", text="Enable All Render Layers")
		layout.operator("scene.disable_all_render_layers", text="Disable All Render Layers")
		layout.separator()
		layout.operator("scene.render_allactions", text="Render Fake Actions")
		

def register():
	bpy.utils.register_module(__name__)
	
def unregister():
	bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
	register()			