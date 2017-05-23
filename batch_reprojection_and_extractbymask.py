import arcpy, os
from arcpy import env
from arcpy.sa import *
arcpy.CheckOutExtension("Spatial")
env.overwriteOutput = True

#Set the current workspace
env.workspace = (r"C:\thesis\for_sampling\sampling_outputs\feature_per_biogeoregion\fcs.gdb")
out_coorsys = arcpy.SpatialReference("Asia Lambert Conformal Conic")

# Get a list of rasters 
for fc in arcpy.ListFeatureClasses():
    #Reproject all the tiff/shp from the rasterList/ListFeatureClasses
    #print fc
    oNamefc = "PCS_" + fc
    print oNamefc
    output = os.path.join(r"C:\thesis\for_sampling\sampling_outputs\feature_per_biogeoregion\fcs.gdb", oNamefc)
    arcpy.Project_management(fc, output , out_coorsys)
    #arcpy.ProjectRaster_management(raster, outputReprojected, "Country_UTM.shp")
    
""" Optional: This is for extracting the Philippines (w/o Sabah etc.)
for raster in arcpy.ListRasters("reprojected*", "TIF"):
    print raster # checking the presence of raster
    outputRasterExtractbyMask = ExtractByMask(raster, "Country_UTM.shp")
    outputRasterExtractbyMask_Name = "phil_only"+raster
    outputRasterExtractbyMask.save(outputRasterExtractbyMask_Name)"""

print "Finish"







    
