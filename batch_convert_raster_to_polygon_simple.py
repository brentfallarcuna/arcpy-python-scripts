#This is for a simple batch raster to polygon processing
#Matagal ang prosesong ito!
#import the module
import arcpy, os
from arcpy import env

#set the workspace and output as true
env.overwriteOutput = True
env.compression = "LZW"
env.workspace = r"C:\thesis\LATEST\TREES\Per Region\new lossyear"

#Get a list of rasters and convert to shapefile
"""
r = ['*gain','*lossyear','*nochange']

for k in r:
    print "________________________________________________________________"
    print "Converting: "
    print k
    env.workspace = r"C:\thesis\for_sampling\sampling_outputs\mosaicked_outputs.gdb"
    for raster in arcpy.ListRasters(k):
        outFolder = r"C:\thesis\for_sampling\sampling_outputs\feature_per_biogeoregion\fcs.gdb"
        print "Converting this " +raster #check the presence of rasters
        out_ras = "gdb" + raster
        u = os.path.join(outFolder, out_ras)
        #print outras
        arcpy.RasterToPolygon_conversion(raster, u, "NO_SIMPLIFY")
        print "                         Finish converting " + raster

#This code below has much simpler flow """
for raster in arcpy.ListRasters("new*.tif"):
    #env.workspace = r"C:\thesis\giff_assorted_provinces\new_lossyears_raster"
    print "Converting this " +raster #check the presence of rasters
    outFolder = r"C:\thesis\LATEST\TREES\Per Region\new lossyear\newlossyear.gdb"
    out_poly = "gdb" + raster.replace(".tif", "")
    u = os.path.join(outFolder, out_poly)
    print  "                         to this new " + out_poly
    arcpy.RasterToPolygon_conversion(raster, u, "NO_SIMPLIFY")
    print "                                                   Finish converting " + raster

print "Finish converting all the rasters to polygon"

