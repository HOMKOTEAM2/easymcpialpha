from easymcpi import McpiUtilits
from mcpi.minecraft import Minecraft
import mcpi.block as block

mc = Minecraft.create()
mcpiutil = McpiUtilits(mc)

pos = mc.player.getTilePos()
x, y, z = pos.x, pos.y, pos.z

mcpiutil.build_tower(x, y, z, height=5, radius=5, block_id=block.BEDROCK.id)