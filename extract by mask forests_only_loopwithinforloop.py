import arcpy
from arcpy import env
from arcpy.sa import *
arcpy.CheckOutExtension("Spatial")
env.overwriteOutput = True


#Set the current workspace
env.workspace = (r"C:\thesis\hansenwipfiles\hansenwipfiles v1.1")
env.nodata = "MINIMUM"
env.compression = "LZ77"

# just add the 30N_120E for Batanes Forests
listsRasters = ['*10N_120E.tif']#,'*10N_120E.tif','*20N_110E.tif','*20N_120E.tif'] #*30N_120E.tif

for i in listsRasters:
    print  "Extracting " + i
    env.workspace = (r"C:\thesis\hansenwipfiles\hansenwipfiles v1.1")
    #This is for extracting the forest areas of hansen percent treecover
    for raster in arcpy.ListRasters(i, "TIF"):
        env.workspace = (r"C:\thesis\hansenwipfiles\hansenwipfiles v1.1")
        print "   extracting "+raster #checking the presence of raster
        outputRasterExtractbyMask = ExtractByMask(raster, "5_over_5_overlay_agreement.shp")
        outputRasterExtractbyMask_Name = "forests_"+raster
        env.workspace = (r"C:\thesis\Zamboanga Sib and del Norte")
        outputRasterExtractbyMask.save(outputRasterExtractbyMask_Name)
        
print "Finish"
