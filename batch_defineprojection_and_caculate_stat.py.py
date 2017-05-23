import arcpy
from arcpy import env
env.overwriteOutput = True

#Set the current workspace
env.workspace = r"C:\thesis\LATEST\TREES\Per Region\new lossyear"
for raster in arcpy.ListRasters("*", "TIF"):
    print "Defining projection of " + raster
    #get the coordinate system by describing a feature class or raster
    dsc = arcpy.Describe(r"C:\thesis\LATEST\TREES\Per Region\treecover\ARMM_forests_onlytreecover2000_10N_110E.tif")
    coord_sys = dsc.spatialReference
    arcpy.DefineProjection_management(raster, coord_sys)

env.workspace = r"C:\thesis\LATEST\TREES\Per Region\new lossyear"
for raster in arcpy.ListRasters("*", "TIF"):
    print "Calculating statistics of " + raster
    #calculate all of the statistics
    arcpy.CalculateStatistics_management(raster)
"""
#_____________________________________________

env.workspace = (r"C:\thesis\for_sampling\sampling_outputs\new_loss")
for raster in arcpy.ListRasters("*Luzon*"):
    print "Defining projection of " + raster
    #get the coordinate system by describing a feature class
    dsc = arcpy.Describe(r"C:\Users\brentiebark\Downloads\PHL_adm0.shp")
    coord_sys = dsc.spatialReference
    arcpy.DefineProjection_management(raster, coord_sys)

env.workspace = (r"C:\thesis\for_sampling\sampling_outputs\new_loss")
for raster in arcpy.ListRasters("*Luzon*"):
    print "Calculating statistics of " + raster
    #calculate all of the statistics
    arcpy.CalculateStatistics_management(raster)
#___________________________________________________

env.workspace = (r"C:\thesis\for_sampling\sampling_outputs\new_lossyear")
for raster in arcpy.ListRasters("*Luzon*"):
    print "Defining projection of " + raster
    #get the coordinate system by describing a feature class
    dsc = arcpy.Describe(r"C:\Users\brentiebark\Downloads\PHL_adm0.shp")
    coord_sys = dsc.spatialReference
    arcpy.DefineProjection_management(raster, coord_sys)

env.workspace = (r"C:\thesis\for_sampling\sampling_outputs\new_lossyear")
for raster in arcpy.ListRasters("*Luzon*"):
    print "Calculating statistics of " + raster
    #calculate all of the statistics
    arcpy.CalculateStatistics_management(raster)

#_______________________________________________________________
env.workspace = (r"C:\thesis\for_sampling\sampling_outputs\nochange")
for raster in arcpy.ListRasters("*Luzon*"):
    print "Defining projection of " + raster
    #get the coordinate system by describing a feature class
    dsc = arcpy.Describe(r"C:\Users\brentiebark\Downloads\PHL_adm0.shp")
    coord_sys = dsc.spatialReference
    arcpy.DefineProjection_management(raster, coord_sys)

env.workspace = (r"C:\thesis\for_sampling\sampling_outputs\nochange")
for raster in arcpy.ListRasters("*Luzon*"):
    print "Calculating statistics of " + raster
    #calculate all of the statistics
    arcpy.CalculateStatistics_management(raster)
"""
print "Finish"






