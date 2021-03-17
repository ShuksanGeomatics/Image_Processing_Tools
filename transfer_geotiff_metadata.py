from osgeo import gdal, gdalconst

# Open the files you want to transfer RPCs from and to
tif_with_RPCs = gdal.Open(tif_file_with_RPCs, gdalconst.GA_ReadOnly)
tif_without_RPCs = gdal.Open(tif_file_without_RPCs,gdalconst.GA_Update)

# get the RPCs from the first file ...
rpcs = tif_with_RPCs.GetMetadata('RPC')

# ... write them to the second file
tif_without_RPCs.SetMetadata(rpcs ,'RPC')

# close the files
del(tif_with_RPCs)
del(tif_without_RPCs)