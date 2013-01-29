from pi3d.constants import *
from pi3d.Shape import Shape

class Tube(Shape):
  """ 3d model inherits from Shape"""
  def __init__(self, camera=None, light=None, radius=1.0, thickness=0.5, height=2.0, sides=12, name="",
               x=0.0, y=0.0, z=0.0, rx=0.0, ry=0.0, rz=0.0,
               sx=1.0, sy=1.0, sz=1.0, cx=0.0, cy=0.0, cz=0.0):
    """uses standard constructor for Shape extra Keyword arguments:
    radius -- radius of to mid point of wall
    thickness -- of wall of tube
    height -- length of tube
    sides -- number of sides for Shape.lathe() to use
    """
    super(Tube,self).__init__(camera, light, name, x, y, z, rx, ry, rz, sx, sy, sz, cx, cy, cz)

    if VERBOSE:
      print "Creating Tube ..."

    t = thickness * 0.5
    path = []
    path.append((radius - t, height * .5))
    path.append((radius + t, height * .5))
    path.append((radius + t, height * .4999))
    path.append((radius + t, -height * .4999))
    path.append((radius + t, -height * .5))
    path.append((radius - t, -height * .5))
    path.append((radius - t, -height * .4999))
    path.append((radius - t, height * .4999))
    path.append((radius - t, height * .5))

    self.radius = radius
    self.thickness = thickness
    self.height = height
    self.sides = sides
    self.ttype = GL_TRIANGLES

    self.buf = []
    self.buf.append(self.lathe(path))
