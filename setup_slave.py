import bpy

bpy.ops.wm.addon_enable(module="netrender")

#bpy.context.user_preferences.system.compute_device_type = 'CUDA'
#bpy.context.user_preferences.system.compute_device = 'CUDA_0'

#bpy.context.scene.cycles.device = 'GPU'

bpy.context.scene.render.tile_x = 16
bpy.context.scene.render.tile_y = 16

#bpy.ops.render.render(write_still=True)


# bpy.context.scene.network_render.mode = 'RENDER_MASTER'
# bpy.context.scene.network_render.server_port = 8000

bpy.context.scene.network_render.mode = 'RENDER_SLAVE'
bpy.context.scene.network_render.server_address = "de-adn-44qppc2.adesso.local"
bpy.context.scene.network_render.server_port = 8000

bpy.ops.render.netclientstart()
