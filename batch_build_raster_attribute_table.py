import arcpy
from arcpy import env
arcpy.CheckOutExtension("Spatial")
env.overwriteOutput = True

#Set the current workspace
env.workspace = (r"C:\thesis\for_sampling\sampling_outputs\mosaicked_outputs.gdb")

for raster in arcpy.ListRasters("*"):
    print raster+ "        Building attribute table!"
    arcpy.BuildRasterAttributeTable_management(raster, "OVERWRITE")


print "Finish!"






