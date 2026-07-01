from mcpi.minecraft import Minecraft
from minecraftstuff import MinecraftDrawing
import mcpi.block as block

class McpiUtilits:
    def __init__(self, mc):
            self.mc = mc
            self.mcdraw = MinecraftDrawing(mc)

    def draw_box(self,x,y,z,length,width,height,block_id,hollow=False):
        try:
            if hollow == False:
                self.mc.setBlocks(x,y,z,x+length,y+height,z+width,block_id)
            elif hollow:
                self.mc.setBlocks(x,y,z,x+length,y+height,z+width,block_id)
                self.mc.setBlocks(x+1,y+1,z+1,x+length-1,y+height-1,z+width-1,block.AIR.id)
            else:
                print("Ошибка. Проверьте формат ввода")
                self.mc.postToChat("Ошибка. Проверьте формат ввода")
        except Exception as e:
            print(f"Ошибка: {e}")
            self.mc.postToChat(f"Ошибка: {e}")
    
    def build_tower(self,x,y,z,height,radius,block_id):
        for i in range(0,height+1,1):
            self.mcdraw.drawHorizontalCircle(x,y+i,z,radius,block_id)