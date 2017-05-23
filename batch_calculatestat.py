import arcpy
from arcpy import env
from arcpy.sa import *
arcpy.CheckOutExtension("Spatial")
env.overwriteOutput = True

#Set the current workspace
env.workspace = (r"C:\thesis\hansenwipfiles\first and last v1.0")

for raster in arcpy.ListRasters("subset*", "TIF"):
    print "Calculating the statistics of "+ raster
    #calculate all of the statistics
    arcpy.CalculateStatistics_management(raster)


print "Finish"





