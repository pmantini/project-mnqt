"""
Project MNQT
Scale class
"""

import math
import numpy as np

class Scale:
    """ Scale class to adjust the width of an image """
    
    def resize(self, image, new_width, new_height, interpolation):
        """ Calls the appropriate function to scale the image based on the interpolation method """
        
        new_width = int(new_width)
        new_height = int(new_height)
            
        if interpolation == 'Bilinear':
            return self.scale_bilinear(image, new_width, new_height)
            
        elif interpolation == 'Bicubic':
            return self.scale_bicubic(image, new_width, new_height)
            
        else: # default to nearest neighbor
            return self.scale_nearest_neighbor(image, new_width, new_height)
        
        
    def scale_nearest_neighbor(self, image, new_width, new_height):
        """ Scales using nearest neighbor interpolation """
        
        width, height = image.shape
        fx = float(new_width)/width
        fy = float(new_height)/height
        
        new_image = np.zeros((new_width, new_height))
        for i in range(new_width):
            for j in range(new_height):
                new_image[i,j] = image[int(i/fx), int(j/fy)]

        return new_image
        
    def scale_bilinear(self, image, new_width, new_height):
        """ Scales using bilinear interpolation """
        
        width, height = image.shape
        fx = float(new_width)/width
        fy = float(new_height)/height
        
        new_image = np.zeros((new_width, new_height))
        
        for i in range(new_width):
            for j in range(new_height):
                x = i/fx
                y = j/fy
                
                # find 4 nearest neighbors
                # ex: x = 20.5, y = 33.3 -> x1 = 20, x2 = 21, y1 = 33, y2 = 34
                x1 = math.floor(x)
                x2 = math.ceil(x)
                if x2 >= width:
                    x2 = width - 1
                    
                y1 = math.floor(y)
                y2 = math.ceil(y)
                if y2 >= height:
                    y2 = height - 1
            
                # interpolate
                new_image[i,j] = 0
        
        return new_image
        
    def scale_bicubic(self, image, new_width, new_height):
        """ Scales using bicubic interpolation """
        
        width, height = image.shape
        fx = float(new_width)/width
        fy = float(new_height)/height
        
        new_image = np.zeros
        
        for i in range(new_width):
            for j in range(new_height):
                x = i/fx
                y = j/fy
                
                # find 16 nearest neighbors
                x1 = math.floor(x)
                x2 = math.ceil(x)
                if x2 >= width:
                    x2 = width - 1
                if x1 == x2:
                    x0 = x1
                    x3 = x2
                else:
                    x0 = 0 if x1 <= 0 else x1 - 1
                    x3 = width - 1 if x2 >= width - 1 else x2 + 1
                    
                y1 = math.floor(y)
                y2 = math.ceil(y)
                if y2 >= height:
                    y2 = height - 1
                if y1 == y2:
                    y0 = y1
                    y3 = y2
                else:
                    y0 = 0 if y1 <= 0 else y1 - 1
                    y3 = height - 1 if y2 >= height - 1 else y2 + 1
                
                # interpolate
                new_image[i,j] = 0
        
        return new_image