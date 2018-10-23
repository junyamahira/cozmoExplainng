import asyncio
import cozmo
from PIL import Image, ImageDraw
from datetime import datetime

def on_img(event, *, image:cozmo.world.CameraImage, **kw):
  print(image.raw_image)

  fpass = '/Users/c0116278ba/cozmo_sdk_examples_1.4.5/data/'
  fname = datetime.now().strftime("%H_%M_%S_%f")
  image.raw_image.save(fpass + fname + ".png")


async def cozmo_program(robot: cozmo.robot.Robot):
  robot.camera.image_stream_enabled = True
  robot.camera.color_image_enabled = True
  robot.add_event_handler(cozmo.world.EvtNewCameraImage, on_img)
  robot.set_head_angle(cozmo.util.Angle(degrees=0))

  while True:
    await asyncio.sleep(1)

cozmo.robot.Robot.drive_off_charger_on_connect = False
cozmo.run_program(cozmo_program)
