import arcpy
from arcpy import env
from arcpy.sa import *
arcpy.CheckOutExtension("Spatial")
env.overwriteOutput = True

#Set the current workspace
env.nodata = "NONE"
env.compression = "LZ77"
env.workspace = r"C:\thesis\LATEST\MOD12\Per Region\new lossyear\one_pixel.gdb"

#This is for extracting the forest areas of hansen percent treecover



"""for raster in arcpy.ListRasters("*20N_120E.tif", "TIF"):
    env.workspace = r"C:\thesis\for_sampling\sampling_outputs"
    #print raster #checking the presence of raster
    outputRasterExtractbyMask = ExtractByMask(raster, "Greater_Luzon_Final.shp")
    outputRasterExtractbyMask_Name = "Luzon"+raster
    env.workspace = r"C:\thesis\for_sampling\sampling_outputs\Greater Luzon"
    outputRasterExtractbyMask.save(outputRasterExtractbyMask_Name)
    print raster + "  is finished!"
print  "Luzon 20N_120E is Finished!"

env.workspace = r"C:\thesis\for_sampling\sampling_outputs"
for raster in arcpy.ListRasters("*20N_110E.tif", "TIF"):
    env.workspace = r"C:\thesis\for_sampling\sampling_outputs"
    #print raster #checking the presence of raster
    outputRasterExtractbyMask = ExtractByMask(raster, "Greater_Luzon_Final.shp")
    outputRasterExtractbyMask_Name = "Luzon"+raster
    env.workspace = r"C:\thesis\for_sampling\sampling_outputs\Greater Luzon"
    outputRasterExtractbyMask.save(outputRasterExtractbyMask_Name)
    print raster + "  is finished!"
print  "Luzon 20N_110E is Finished!"

env.workspace = r"C:\thesis\for_sampling\sampling_outputs"
for raster in arcpy.ListRasters("*20N_120E.tif", "TIF"):
    env.workspace = r"C:\thesis\for_sampling\sampling_outputs"
    #print raster #checking the presence of raster
    outputRasterExtractbyMask = ExtractByMask(raster, "Greater_Negros_Panay_Final.shp")
    outputRasterExtractbyMask_Name = "Negros_Panay"+raster
    env.workspace = r"C:\thesis\for_sampling\sampling_outputs\Greater Negros Panay"
    outputRasterExtractbyMask.save(outputRasterExtractbyMask_Name)
    print raster + "  is finished!"
print  "Negros Panay 20N_120E is Finished!"

env.workspace = r"C:\thesis\for_sampling\sampling_outputs"
for raster in arcpy.ListRasters("*10N_120E.tif", "TIF"):
    env.workspace = r"C:\thesis\for_sampling\sampling_outputs"
    #print raster #checking the presence of raster
    outputRasterExtractbyMask = ExtractByMask(raster, "Greater_Negros_Panay_Final.shp")
    outputRasterExtractbyMask_Name =  "Negros_Panay"+raster
    env.workspace = r"C:\thesis\for_sampling\sampling_outputs\Greater Negros Panay"
    outputRasterExtractbyMask.save(outputRasterExtractbyMask_Name)
    print raster + "  is finished!"
print  "Negros Panay 10N_120E is Finished!"

env.workspace = r"C:\thesis\for_sampling\sampling_outputs"
for raster in arcpy.ListRasters("*10N_120E.tif", "TIF"):
    env.workspace = r"C:\thesis\for_sampling\sampling_outputs"
    #print raster #checking the presence of raster
    outputRasterExtractbyMask = ExtractByMask(raster, "Greater_Mindanao_Final.shp")
    outputRasterExtractbyMask_Name = "Mindanao"+raster
    env.workspace = r"C:\thesis\for_sampling\sampling_outputs\Greater Mindanao"
    outputRasterExtractbyMask.save(outputRasterExtractbyMask_Name)
    print raster + "  is finished!"
print  "Mindanao 10N_120E is Finished!"

env.workspace = r"C:\thesis\for_sampling\sampling_outputs"
for raster in arcpy.ListRasters("*10N_110E.tif", "TIF"):
    env.workspace = r"C:\thesis\for_sampling\sampling_outputs"
    #print raster #checking the presence of raster
    outputRasterExtractbyMask = ExtractByMask(raster, "Greater_Mindanao_Final.shp")
    outputRasterExtractbyMask_Name = "Mindanao"+raster
    env.workspace = r"C:\thesis\for_sampling\sampling_outputs\Greater Mindanao"
    outputRasterExtractbyMask.save(outputRasterExtractbyMask_Name)
    print raster + "  is finished!"
print  "Mindanao 10N_110E is Finished!"

env.workspace = r"C:\thesis\for_sampling\sampling_outputs"
for raster in arcpy.ListRasters("*20N_120E.tif", "TIF"):
    env.workspace = r"C:\thesis\for_sampling\sampling_outputs"
    #print raster #checking the presence of raster
    outputRasterExtractbyMask = ExtractByMask(raster, "Greater_Mindanao_Final.shp")
    outputRasterExtractbyMask_Name = "Mindanao"+raster
    env.workspace = r"C:\thesis\for_sampling\sampling_outputs\Greater Mindanao"
    outputRasterExtractbyMask.save(outputRasterExtractbyMask_Name)
    print raster + "  is finished!"
print  "Mindanao 20N_120E is Finished!"

env.workspace = r"C:\thesis\for_sampling\sampling_outputs"
for raster in arcpy.ListRasters("*10N_110E.tif", "TIF"):
    env.workspace = r"C:\thesis\for_sampling\sampling_outputs"
    #print raster #checking the presence of raster
    outputRasterExtractbyMask = ExtractByMask(raster, "Greater_Palawan_Final.shp")
    outputRasterExtractbyMask_Name = "Palawan"+raster
    env.workspace = r"C:\thesis\for_sampling\sampling_outputs\Greater Palawan"
    outputRasterExtractbyMask.save(outputRasterExtractbyMask_Name)
    print raster + "  is finished!"
print  "Palawan 10N_110E is Finished!"

env.workspace = r"C:\thesis\for_sampling\sampling_outputs"
for raster in arcpy.ListRasters("*20N_110E.tif", "TIF"):
    env.workspace = r"C:\thesis\for_sampling\sampling_outputs"
    #print raster #checking the presence of raster
    outputRasterExtractbyMask = ExtractByMask(raster, "Greater_Palawan_Final.shp")
    outputRasterExtractbyMask_Name = "Palawan"+raster
    env.workspace = r"C:\thesis\for_sampling\sampling_outputs\Greater Palawan"
    outputRasterExtractbyMask.save(outputRasterExtractbyMask_Name)
    print raster + "  is finished!"
print  "Palawan 20N_110E is Finished!"

env.workspace = r"C:\thesis\for_sampling\sampling_outputs"
for raster in arcpy.ListRasters("*20N_120E.tif", "TIF"):
    env.workspace = r"C:\thesis\for_sampling\sampling_outputs"
    #print raster #checking the presence of raster
    outputRasterExtractbyMask = ExtractByMask(raster, "Greater_Palawan_Final.shp")
    outputRasterExtractbyMask_Name = "Palawan"+raster
    env.workspace = r"C:\thesis\for_sampling\sampling_outputs\Greater Palawan"
    outputRasterExtractbyMask.save(outputRasterExtractbyMask_Name)
    print raster + "  is finished!"
print  "Palawan 20N_120E is Finished!"""

print "Finish all of them!"
