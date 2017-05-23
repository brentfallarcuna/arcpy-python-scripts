import arcpy
from arcpy import env
from arcpy.sa import *
arcpy.CheckOutExtension("Spatial")
env.overwriteOutput = True

#Set the current workspace
env.workspace = r"C:\thesis\for_sampling\sampling_outputs\new_loss"

for raster in arcpy.ListRasters("*", "TIF"):
    print raster
    #get the coordinate system by describing a feature class
    dsc = arcpy.Describe(r"C:\Users\brentiebark\Downloads\PHL_adm0.shp")
    coord_sys = dsc.spatialReference
    arcpy.DefineProjection_management(raster, coord_sys)
    
print "Finish"







    
