import arcpy
from arcpy import env
from arcpy.sa import *
arcpy.CheckOutExtension("Spatial")
env.overwriteOutput = True


#Set the current workspace
env.workspace = r"C:\thesis\NDVI_reprojected"
env.nodata = "MINIMUM"
env.compression = "LZ77"


#for shp in arcpy.ListFeatureClasses():
    #print shp
    
#This is for extracting the forest areas of hansen percent treecover
for raster in arcpy.ListRasters("*.tif", "TIF"):
    env.workspace = r"C:\thesis\NDVI_reprojected"
    #print raster #checking the presence of raster
    outputRasterExtractbyMask = ExtractByMask(raster, "sample_nakar.shp")
    outputRasterExtractbyMask_Name = "nakar_upper"+raster
    env.workspace = r"C:\thesis\NDVI_reprojected\Quezon"
    outputRasterExtractbyMask.save(outputRasterExtractbyMask_Name)
    print raster + "  is finished!"


print "Finish (all of them)!"
