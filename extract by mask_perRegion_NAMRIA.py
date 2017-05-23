import arcpy
from arcpy import env
from arcpy.sa import *
arcpy.CheckOutExtension("Spatial")
env.overwriteOutput = True

#Set the current workspace
env.workspace = (r"C:\thesis\LATEST\MOD12\Per Region\new lossyear\regions\regions_outputs")
env.nodata = "NONE"
env.compression = "LZ77"

list_input = ['ARMM.shp','IVB.shp','IX.shp','VI.shp','VII.shp','VIII.shp','X.shp','XI.shp','XII.shp','XIII.shp',
                    'CAR.shp','I.shp','II.shp',
                   'III.shp','IVA.shp','NCR.shp','V.shp']
list_eraser = ['BSWM_ARMM.shp','BSWM_IVB.shp','BSWM_IX.shp','BSWM_VI.shp','BSWM_VII.shp','BSWM_VIII.shp','BSWM_X.shp',
                   'BSWM_XI.shp','BSWM_XII.shp','BSWM_XIII.shp','BSWM_CAR.shp','BSWM_I.shp','BSWM_II.shp',
                   'BSWM_III.shp','BSWM_IVA.shp','BSWM_NCR.shp','BSWM_V.shp']
output = ['MOD12_ARMM.shp','MOD12_IVB.shp','MOD12_IX.shp','MOD12_VI.shp','MOD12_VII.shp','MOD12_VIII.shp','MOD12_X.shp',
                   'MOD12_XI.shp','MOD12_XII.shp','MOD12_XIII.shp','MOD12_CAR.shp','MOD12_I.shp','MOD12_II.shp',
                   'MOD12_III.shp','MOD12_IVA.shp','MOD12_NCR.shp','MOD12_V.shp']
for j in range(0, 17):
    print j
    arcpy.Erase_analysis(r'C:\thesis\LATEST\MOD12\Per Region\new lossyear\regions\regions_outputs\\'+list_input[j],
    r'C:\thesis\LATEST\MOD12\Per Region\new lossyear\regions\regions_outputs\\'+list_eraser[j],
    r'C:\thesis\LATEST\MOD12\Per Region\new lossyear\regions\regions2\\'+ output[j])
print "Finish"





"""list_10_110 = ['ARMM.shp','IVB.shp']
#This is for extracting the forest areas of hansen percent treecover
#loop the list
for i in list_10_110:
    print "Extracting " + i + " in 10_110"
    env.workspace = (r"C:\thesis\LATEST\LATEST Forest Masks\ESSC")
    for raster in arcpy.ListRasters("*10N_110E.tif", "TIF"):
        env.workspace = (r"C:\thesis\LATEST\LATEST Forest Masks\ESSC")
        #print raster #checking the presence of raster
        outputRasterExtractbyMask = ExtractByMask(raster, i)
        prov=i.replace(".shp", "_")
        outputRasterExtractbyMask_Name = prov + raster
        env.workspace = (r"C:\thesis\LATEST\LATEST Forest Masks\ESSC\Per Region")
        outputRasterExtractbyMask.save(outputRasterExtractbyMask_Name)

list_10_120 = ['ARMM.shp','IX.shp','VI.shp','VII.shp','VIII.shp','X.shp','XI.shp','XII.shp','XIII.shp']
#This is for extracting the forest areas of hansen percent treecover
#loop the list;
for k in list_10_120:
    print "Extracting " + k + " in 10_120"
    env.workspace = (r"C:\thesis\LATEST\LATEST Forest Masks\ESSC")
    for raster in arcpy.ListRasters("*10N_120E.tif", "TIF"):
        env.workspace = (r"C:\thesis\LATEST\LATEST Forest Masks\ESSC")
        #print raster #checking the presence of raster
        outputRasterExtractbyMask = ExtractByMask(raster, k)
        prov=k.replace(".shp", "_")
        outputRasterExtractbyMask_Name = prov + raster
        env.workspace = (r"C:\thesis\LATEST\LATEST Forest Masks\ESSC\Per Region")
        outputRasterExtractbyMask.save(outputRasterExtractbyMask_Name)

list_20_110 = ['I.shp', 'IVB.shp']
#This is for extracting the forest areas of hansen percent treecover
#loop the list
for d in list_20_110:
    print "Extracting " + d + " in 20_110"
    env.workspace = (r"C:\thesis\LATEST\LATEST Forest Masks\ESSC")
    for raster in arcpy.ListRasters("*20N_110E.tif", "TIF"):
        env.workspace = (r"C:\thesis\LATEST\LATEST Forest Masks\ESSC")
        #print raster #checking the presence of raster
        outputRasterExtractbyMask = ExtractByMask(raster, d)
        prov=d.replace(".shp", "_")
        outputRasterExtractbyMask_Name = prov + raster
        env.workspace = (r"C:\thesis\LATEST\LATEST Forest Masks\ESSC\Per Region")
        outputRasterExtractbyMask.save(outputRasterExtractbyMask_Name)

list_20_120 = ['VI.shp','VII.shp','VIII.shp','XIII.shp','CAR.shp','I.shp','II.shp',\
                         'III.shp','IVA.shp','IVB.shp','NCR.shp','V.shp']

#This is for extracting the forest areas of hansen percent treecover
#loop the list
for y in list_20_120:
    print "Extracting " + y + " in 20_120"
    env.workspace = (r"C:\thesis\LATEST\LATEST Forest Masks\ESSC")
    for raster in arcpy.ListRasters("*20N_120E.tif", "TIF"):
        env.workspace = (r"C:\thesis\LATEST\LATEST Forest Masks\ESSC")
        #print raster #checking the presence of raster
        outputRasterExtractbyMask = ExtractByMask(raster, y)
        prov=y.replace(".shp", "_")
        outputRasterExtractbyMask_Name = prov + raster
        env.workspace = (r"C:\thesis\LATEST\LATEST Forest Masks\ESSC\Per Region")
        outputRasterExtractbyMask.save(outputRasterExtractbyMask_Name)

env.workspace = (r"C:\thesis\LATEST\LATEST Forest Masks\ESSC")
print "Extracting Batanes in 30_120"
for raster in arcpy.ListRasters("*30N_120E.tif", "TIF"):
    print "Extracting Batanes"
    env.workspace = (r"C:\thesis\LATEST\LATEST Forest Masks\ESSC")
    #print raster #checking the presence of raster
    g = "Batanes.shp"
    outputRasterExtractbyMask = ExtractByMask(raster, g)
    prov = g.replace(".shp", "_")
    outputRasterExtractbyMask_Name = prov + raster
    env.workspace = (r"C:\thesis\LATEST\LATEST Forest Masks\ESSC\Per Region")
    outputRasterExtractbyMask.save(outputRasterExtractbyMask_Name)"""
