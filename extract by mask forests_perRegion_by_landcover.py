import arcpy, os
from arcpy import env
from arcpy.sa import *
arcpy.CheckOutExtension("Spatial")
env.overwriteOutput = True


#Set the current workspace
env.workspace = r"C:\thesis\LATEST\LATEST Forest Masks (with 2013 loss)\NAMRIA\Per Region"
env.nodata = "MINIMUM"
env.compression = "LZ77"

# All tiles are included here!
listsRasters = ['*10N_110E.tif','*10N_120E.tif','*20N_110E.tif','*20N_120E.tif','*30N_120E.tif']

for i in listsRasters:
    print  "Extracting this tile: " + i
    env.workspace = r"C:\thesis\LATEST\LATEST Forest Masks (with 2013 loss)\NAMRIA\Per Region"
    #This is for extracting the particular forest landcover of hansen percent treecover
    for raster in arcpy.ListRasters(i, "TIF"):
        env.workspace = (r"C:\thesis\LATEST\LATEST Forest Masks (with 2013 loss)\NAMRIA\Per Region")
        print "    extracting this raster: "+ raster #checking the presence of raster
        outputRasterExtractbyMask = ExtractByMask(raster, "Closed_Forest.shp")
        outFolder = r"C:\thesis\LATEST\NAMRIA\Per Region\Per Landcover\Closed Forest"
        oName, oExt = os.path.splitext(raster)
        outRaster = os.path.join(outFolder, oName+ "_Closed Forest.tif")
        outputRasterExtractbyMask_Name = outRaster
        env.workspace = r"C:\thesis\LATEST\NAMRIA\Per Region\Per Landcover\Closed Forest"
        outputRasterExtractbyMask.save(outputRasterExtractbyMask_Name)

print "Finish"
