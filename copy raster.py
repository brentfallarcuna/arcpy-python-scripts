import arcpy, os
from arcpy import env
from arcpy.sa import *
arcpy.CheckOutExtension("Spatial")
env.overwriteOutput = True

#Set the current workspace
env.workspace = r"C:\thesis\LATEST\Overlay Agreements\5_over_5\Per Province\Palawan\20N_120E"
env.nodata = "NONE"
env.compression = "LZ77"

print "datamask to datamask folder"
outFolder = r"C:\thesis\LATEST\Overlay Agreements\5_over_5\Per Province\Palawan\20N_120E\datamask"
#This is for batch copying particular files
print "Copying files to datamask folder"
for raster in arcpy.ListRasters("*datamask*.tif", "TIF"):
    print "   Copying this raster: " + raster #checking the presence of raster
    outRaster = os.path.join(outFolder, raster)
    arcpy.CopyRaster_management(raster,  outRaster)

outFolder = r"C:\thesis\LATEST\Overlay Agreements\5_over_5\Per Province\Palawan\20N_120E\gain"
#This is for batch copying particular files
print "Copying files to gain folder"
for raster in arcpy.ListRasters("*gain*.tif", "TIF"):
    print "   Copying this raster: " + raster #checking the presence of raster
    outRaster = os.path.join(outFolder, raster)
    arcpy.CopyRaster_management(raster,  outRaster)

outFolder = r"C:\thesis\LATEST\Overlay Agreements\5_over_5\Per Province\Palawan\20N_120E\loss"
#This is for batch copying particular files
print "Copying files to loss folder"
for raster in arcpy.ListRasters("*loss_*.tif", "TIF"):
    print "   Copying this raster: " + raster #checking the presence of raster
    outRaster = os.path.join(outFolder, raster)
    arcpy.CopyRaster_management(raster,  outRaster)

outFolder = r"C:\thesis\LATEST\Overlay Agreements\5_over_5\Per Province\Palawan\20N_120E\lossyear"
#This is for batch copying particular files
print "Copying files to lossyear folder"
for raster in arcpy.ListRasters("*lossyear*.tif", "TIF"):
    print "   Copying this raster: " + raster #checking the presence of raster
    outRaster = os.path.join(outFolder, raster)
    arcpy.CopyRaster_management(raster,  outRaster)

outFolder = r"C:\thesis\LATEST\Overlay Agreements\5_over_5\Per Province\Palawan\20N_120E\treecover"
#This is for batch copying particular files
print "Copying files to treecover folder"
for raster in arcpy.ListRasters("*treecover*.tif", "TIF"):
    print "   Copying this raster: " + raster #checking the presence of raster
    outRaster = os.path.join(outFolder, raster)
    arcpy.CopyRaster_management(raster,  outRaster)


print "Finish Copying Palawan!"
