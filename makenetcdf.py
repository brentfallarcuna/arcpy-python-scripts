import arcpy, os
from arcpy import env
from arcpy.sa import *
arcpy.CheckOutExtension("Spatial")

#set the workspace#set the workspace and output as true
env.workspace = r"C:\Users\brentiebark\Desktop\netcdfs"
env.overwriteOutput = True
env.compression = "LZW"
"""
out_Folder = env.workspace
for nc in arcpy.ListFiles("*.nc"):
    print "Processing this " + nc
    in_nc = os.path.join(out_Folder, nc)
    (shortname, extension) = os.path.splitext(nc)
    out_layer = shortname+"_sst"
    out =  os.path.join(out_Folder, out_layer)
    arcpy.MakeNetCDFRasterLayer_md(in_nc, "sst", "lon", "lat", out)
    arcpy.CopyRaster_management(out, out+".tif")
    """
"""for raster in arcpy.ListRasters("*.tif"):
    print raster
    outputRasterExtractbyMask = ExtractByMask(raster, "PHL_adm0.shp")
    outputRasterExtractbyMask_Name = raster.replace("_sst","Phil")
    outputRasterExtractbyMask.save(outputRasterExtractbyMask_Name)
    print "This " + raster + " is Finish"""
print "Finish"  
    

