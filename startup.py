import os
import bpy.ops
import logging

logger = logging.getLogger()
logger.setLevel(20)

bpy.ops.wm.addon_enable(module="netrender")
bpy.context.scene.render.engine = 'NET_RENDER'

# NONE, CUDA, OPENCL
deviceType = os.getenv('RENDER_DEVICE_TYPE', 'NONE')
bpy.context.user_preferences.addons['cycles'].preferences.compute_device_type = deviceType

if deviceType != 'NONE':
    bpy.context.user_preferences.addons['cycles'].preferences.devices[0].use = True

# CPU, GPU
device = os.getenv('RENDER_DEVICE', 'CPU')
bpy.context.scene.cycles.device = device

# lower values for CPU, higher values for GPU
tileX = os.getenv('RENDER_TILE_SIZE_X', 16)
tileY = os.getenv('RENDER_TILE_SIZE_Y', 16)
bpy.context.scene.render.tile_x = int(tileX)
bpy.context.scene.render.tile_y = int(tileY)

masterIp = os.getenv('MASTER_PORT_8000_TCP_ADDR', False)
if masterIp == False:
    masterIp = os.getenv('MASTER_IP', '127.0.0.1')

renderMode = os.getenv('RENDER_MODE', False)
if renderMode == False:
    logger.warning('No RENDER_MODE environment variable detected. Set default to SLAVE')
    renderMode = 'SLAVE'

if renderMode == 'MASTER':
    bpy.context.scene.network_render.mode = 'RENDER_MASTER'

if renderMode == 'SLAVE':
    bpy.context.scene.network_render.mode = 'RENDER_SLAVE'
    bpy.context.scene.network_render.server_address = masterIp

# start network render instance
bpy.ops.render.netclientstart()
