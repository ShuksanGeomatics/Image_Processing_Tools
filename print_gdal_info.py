#!/usr/bin/env python3
'''Prints the metadata for GDAL accepted raster datasets'''
__author__ = 'Gerry Gabrisch/Lummi GIS'
__date__ = 'Feburary 2021'
__copyright__ = 'MIT'

import traceback
import sys
import gdal

try:
   
    def main():
        
        x = get_image_metadata(in_image)
        print_image_metadata(x)
        
        
        
    def get_image_metadata(in_image):
        x = gdal.Info(in_image)
        return x
    
    def print_image_metadata(x):
        print(x)
        
        
    def main(in_image):
        x = get_image_metadata(in_image)
        print_image_metadata(x)

except:
    tb = sys.exc_info()[2]
    tbinfo = traceback.format_tb(tb)[0]
    print ("PYTHON ERRORS:\nTraceback info:\n" + tbinfo + "\nError Info:\n" + str(sys.exc_info()[1]))

if __name__ == "__main__":
    main("/media/2TBHD/GIS/Projects/MtBakerMap/MtBakerClimbingRoutes.pdf")  

