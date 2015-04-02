#www.stuffaboutcode.com
#Martin O'Hanlon
#Boot a Bully for Autcraft

from mcpi.minecraft import Minecraft
from mcpi.minecraft import Vec3
from mcpi import block
from time import sleep
from minecrafttext import MinecraftText 
import mcpi.minecraftstuff as mcstuff

from random import randint

def showAndClearWord(mcText, word, seconds):
    mcText.writeLineToMC(word, 0)
    sleep(seconds)
    mcText.clearLine(0)

BOOTBLOCKS = [mcstuff.ShapeBlock(0,0,0,block.WOOL.id,15),
              mcstuff.ShapeBlock(1,0,0,block.WOOL.id,15),
              mcstuff.ShapeBlock(2,0,0,block.WOOL.id,15),
              mcstuff.ShapeBlock(3,0,0,block.WOOL.id,15),
              mcstuff.ShapeBlock(4,0,0,block.WOOL.id,15),
              mcstuff.ShapeBlock(5,0,0,block.WOOL.id,15),
              mcstuff.ShapeBlock(6,0,0,block.WOOL.id,15),
              mcstuff.ShapeBlock(7,0,0,block.WOOL.id,15),
              mcstuff.ShapeBlock(0,1,0,block.WOOL.id,12),
              mcstuff.ShapeBlock(1,1,0,block.WOOL.id,12),
              mcstuff.ShapeBlock(2,1,0,block.WOOL.id,12),
              mcstuff.ShapeBlock(3,1,0,block.WOOL.id,12),
              mcstuff.ShapeBlock(4,1,0,block.WOOL.id,12),
              mcstuff.ShapeBlock(5,1,0,block.WOOL.id,12),
              mcstuff.ShapeBlock(6,1,0,block.WOOL.id,12),
              mcstuff.ShapeBlock(7,1,0,block.WOOL.id,12),
              mcstuff.ShapeBlock(8,1,0,block.WOOL.id,12),
              mcstuff.ShapeBlock(0,2,0,block.WOOL.id,12),
              mcstuff.ShapeBlock(1,2,0,block.WOOL.id,12),
              mcstuff.ShapeBlock(2,2,0,block.WOOL.id,12),
              mcstuff.ShapeBlock(3,2,0,block.WOOL.id,12),
              mcstuff.ShapeBlock(4,2,0,block.WOOL.id,12),
              mcstuff.ShapeBlock(5,2,0,block.WOOL.id,12),
              mcstuff.ShapeBlock(6,2,0,block.WOOL.id,12),
              mcstuff.ShapeBlock(7,2,0,block.WOOL.id,12),
              mcstuff.ShapeBlock(8,2,0,block.WOOL.id,12),
              mcstuff.ShapeBlock(0,3,0,block.WOOL.id,12),
              mcstuff.ShapeBlock(1,3,0,block.WOOL.id,12),
              mcstuff.ShapeBlock(2,3,0,block.WOOL.id,12),
              mcstuff.ShapeBlock(3,3,0,block.WOOL.id,12),
              mcstuff.ShapeBlock(4,3,0,block.WOOL.id,12),
              mcstuff.ShapeBlock(5,3,0,block.WOOL.id,12),
              mcstuff.ShapeBlock(6,3,0,block.WOOL.id,12),
              mcstuff.ShapeBlock(7,3,0,block.WOOL.id,12),
              mcstuff.ShapeBlock(8,3,0,block.WOOL.id,12),
              mcstuff.ShapeBlock(0,4,0,block.WOOL.id,12),
              mcstuff.ShapeBlock(1,4,0,block.WOOL.id,12),
              mcstuff.ShapeBlock(2,4,0,block.WOOL.id,12),
              mcstuff.ShapeBlock(3,4,0,block.WOOL.id,12),
              mcstuff.ShapeBlock(4,4,0,block.WOOL.id,12),
              mcstuff.ShapeBlock(5,4,0,block.WOOL.id,12),
              mcstuff.ShapeBlock(1,5,0,block.WOOL.id,12),
              mcstuff.ShapeBlock(2,5,0,block.WOOL.id,12),
              mcstuff.ShapeBlock(3,5,0,block.WOOL.id,12),
              mcstuff.ShapeBlock(1,6,0,block.WOOL.id,6),
              mcstuff.ShapeBlock(2,6,0,block.WOOL.id,6),
              mcstuff.ShapeBlock(3,6,0,block.WOOL.id,6)]

DELAY = 1

#connect to minecraft
mc = Minecraft.create()
#mc.player.setTilePos(-84, 35, -100)
#mc.setBlocks(-95, 35, -125,
#             -65, 60, -80,
#             block.AIR.id)
#create my minecraft text screen object
mcText = MinecraftText(mc)

sleep(15)

showAndClearWord(mcText, "  if", DELAY)
showAndClearWord(mcText, "  you", DELAY)
showAndClearWord(mcText, "  see", DELAY)
showAndClearWord(mcText, "   a", DELAY)
showAndClearWord(mcText, " bully", DELAY)
showAndClearWord(mcText, "   in", DELAY)
showAndClearWord(mcText, "minecraft", DELAY + 1)
showAndClearWord(mcText, "  they", DELAY)
showAndClearWord(mcText, "  dont", DELAY)
showAndClearWord(mcText, " deserve", DELAY)
showAndClearWord(mcText, " respect", DELAY + 1)
showAndClearWord(mcText, "  take", DELAY)
showAndClearWord(mcText, "   a", DELAY)
mcText.writeLineToMC(" stand", 0)

#create the boot
bootPos = Vec3(-88, 70, -125)
boot = mcstuff.MinecraftShape(mc, bootPos, BOOTBLOCKS)

#move the boot down
for down in range(1,40):
    #add another row of leg
    boot.shapeBlocks.append(mcstuff.ShapeBlock(1,6 + down,0,block.WOOL.id,6))
    boot.shapeBlocks.append(mcstuff.ShapeBlock(2,6 + down,0,block.WOOL.id,6))
    boot.shapeBlocks.append(mcstuff.ShapeBlock(3,6 + down,0,block.WOOL.id,6))
    #move the shape down
    boot.moveBy(0, -1, 0)
    #delay
    sleep(0.25)

sleep(2)
for count in range(0,4):
    for flash in range(1,50):
        #make the boot flash
        x = randint(1,3)
        y = randint(6,45)
        flashPos = Vec3(boot.position.x + x,
                        boot.position.y + y,
                        boot.position.z)
        mc.setBlock(flashPos, block.WOOL.id, randint(0,15))
        sleep(0.1)

    #line up and down
    start = 6
    end = 45
    step = 1
    for updown in range(1,6):
        for line in range(start,end,step):
            mc.setBlocks(boot.position.x + 1,
                         boot.position.y + line,
                         boot.position.z,
                         boot.position.x + 3,
                         boot.position.y + line,
                         boot.position.z,
                         block.WOOL.id,
                         randint(0,15))
            sleep(0.05)
            mc.setBlocks(boot.position.x + 1,
                         boot.position.y + line,
                         boot.position.z,
                         boot.position.x + 3,
                         boot.position.y + line,
                         boot.position.z,
                         block.WOOL.id,
                         6)
        #swap the direciton of the line
        start,end = end, start
        step = step * -1

    #line side to side
    start = 1
    end = 3
    step = 1
    for leftright in range(1,15):
        for line in range(start,end,step):
            mc.setBlocks(boot.position.x + line,
                         boot.position.y + 6,
                         boot.position.z,
                         boot.position.x + line,
                         boot.position.y + 45,
                         boot.position.z,
                         block.WOOL.id,
                         randint(0,15))
            sleep(0.50)
            mc.setBlocks(boot.position.x + line,
                         boot.position.y + 6,
                         boot.position.z,
                         boot.position.x + line,
                         boot.position.y + 45,
                         boot.position.z,
                         block.WOOL.id,
                         6)
        #swap the direciton of the line
        start,end = end, start
        step = step * -1

    

sleep(5)
#clear the boot and text
boot.clear()
mcText.clearLine(0)

mcText.writeNextLine("April 2nd")
mcText.writeNextLine("Autism Awareness Day")
mcText.writeNextLine("            Autcraft")

sleep(25)

mcText.clearLine(0)
mcText.clearLine(1)
mcText.clearLine(2)
