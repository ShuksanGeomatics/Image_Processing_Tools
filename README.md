# Image_Processing_Tools
General Python tools that use GDAL or ImageMagick to perform simple tasks with image files.
Tools Include:
  1. print_gdal_info.py: Prints the coordinate reference system of a GDAL raster file.
  2. RGB_to_grayscale_with_world_file.py:  Uses ImageMagick to create a grayscale version of an RGB image.  Makes a new copy of the existing world file.  This            script bypasses some drawn-out steps to accomplish this in ArcGIS.
  3. transfer_geotiff_metadata.py:  Some tools (like GIMP) will not output image files with coordinate reference system information.  This scipt will transfer those      CRS data from an existing file to a new file.
