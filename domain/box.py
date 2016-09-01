import wx
from infra.color import Color


class Box(object):

    def __init__(self, panel, box_id, color, position, size):
        self._white_box = self._create_bitmap('image/white.jpg')
        self._black_box = self._create_bitmap('image/black.jpg')
        self._green_box = self._create_bitmap('image/green.jpg')
        self._red_box = self._create_bitmap('image/red.jpg')

        self.color_map = {Color.BLACK : self._black_box, 
                          Color.WHITE : self._white_box, 
                          Color.GREEN : self._green_box,
                          Color.RED   : self._red_box}

        self._bitmap = wx.StaticBitmap(panel, box_id, self.color_map[color], 
                                       pos=position, size=size)
        self._position = position

    def __del__(self):
        del self._bitmap
        del self._white_box
        del self._black_box
        del self._green_box
        del self._red_box
        
    def _create_bitmap(self, image_name):
        return wx.Image(image_name, wx.BITMAP_TYPE_JPEG).ConvertToBitmap()
    
    def change_color(self, color):
        self._bitmap.SetBitmap(self.color_map[color])
        
    def is_wall(self):
        return self._bitmap.GetBitmap() == self._black_box
