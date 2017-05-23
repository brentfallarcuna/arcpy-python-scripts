import arcpy
from arcpy import env
from arcpy.sa import *
arcpy.CheckOutExtension("Spatial")
env.overwriteOutput = True

#Set the current workspace
env.workspace = (r"C:\thesis\LATEST\Overlay Agreements\5_over_5")
env.nodata = "NONE"
env.compression = "LZ77"

#see if the shp files are there
#for shp in  arcpy.ListFeatureClasses():
    #print  shp

list_10_110 = ['ARMM.shp','IVB.shp']
#This is for extracting the forest areas of hansen percent treecover
#loop the list
for i in list_10_110:
    print "Extracting " + i + " in 10_110"
    env.workspace = (r"C:\thesis\LATEST\Overlay Agreements\5_over_5")
    for raster in arcpy.ListRasters("*10N_110E.tif", "TIF"):
        env.workspace = (r"C:\thesis\LATEST\Overlay Agreements\5_over_5")
        print "    Extracting "+raster #checking the presence of raster
        outputRasterExtractbyMask = ExtractByMask(raster, i)
        prov=i.replace(".shp", "_")
        outputRasterExtractbyMask_Name = prov + raster
        env.workspace = (r"C:\thesis\LATEST\Overlay Agreements\5_over_5\Per Region")
        outputRasterExtractbyMask.save(outputRasterExtractbyMask_Name)

list_10_120 = ['ARMM.shp','IX.shp','VI.shp','VII.shp','VIII.shp','X.shp','XI.shp','XII.shp','XIII.shp']	
#This is for extracting the forest areas of hansen percent treecover
#loop the list
for k in list_10_120:
    print "Extracting " + k + " in 10_120"
    env.workspace = (r"C:\thesis\LATEST\Overlay Agreements\5_over_5")
    for raster in arcpy.ListRasters("*10N_120E.tif", "TIF"):
        env.workspace = (r"C:\thesis\LATEST\Overlay Agreements\5_over_5")
        print "    Extracting "+raster #checking the presence of raster
        outputRasterExtractbyMask = ExtractByMask(raster, k)
        prov=k.replace(".shp", "_")
        outputRasterExtractbyMask_Name = prov + raster
        env.workspace = (r"C:\thesis\LATEST\Overlay Agreements\5_over_5\Per Region")
        outputRasterExtractbyMask.save(outputRasterExtractbyMask_Name)

list_20_110 = ['I.shp', 'IVB.shp']
#This is for extracting the forest areas of hansen percent treecover
#loop the list
for d in list_20_110:
    print "Extracting " + d + " in 20_110"
    env.workspace = (r"C:\thesis\LATEST\Overlay Agreements\5_over_5")
    for raster in arcpy.ListRasters("*20N_110E.tif", "TIF"):
        env.workspace = (r"C:\thesis\LATEST\Overlay Agreements\5_over_5")
        print "    Extracting "+raster #checking the presence of raster
        outputRasterExtractbyMask = ExtractByMask(raster, d)
        prov=d.replace(".shp", "_")
        outputRasterExtractbyMask_Name = prov + raster
        env.workspace = (r"C:\thesis\LATEST\Overlay Agreements\5_over_5\Per Region")
        outputRasterExtractbyMask.save(outputRasterExtractbyMask_Name)
	
list_20_120 = ['VI.shp','VII.shp','VIII.shp','XIII.shp','CAR.shp','I.shp','II.shp','III.shp','IVA.shp','IVB.shp','NCR.shp','V.shp']
#This is for extracting the forest areas of hansen percent treecover
#loop the list
for y in list_20_120:
    print "Extracting " + y + " in 20_120"
    env.workspace = (r"C:\thesis\LATEST\Overlay Agreements\5_over_5")
    for raster in arcpy.ListRasters("*20N_120E.tif", "TIF"):
        env.workspace = (r"C:\thesis\LATEST\Overlay Agreements\5_over_5")
        print "    Extracting "+raster #checking the presence of raster
        outputRasterExtractbyMask = ExtractByMask(raster, y)
        prov=y.replace(".shp", "_")
        outputRasterExtractbyMask_Name = prov + raster
        env.workspace = (r"C:\thesis\LATEST\Overlay Agreements\5_over_5\Per Region")
        outputRasterExtractbyMask.save(outputRasterExtractbyMask_Name)

"""env.workspace = (r"C:\thesis\LATEST\Overlay Agreements\5_over_5")
print "Extracting Batanes in 30_120"
for raster in arcpy.ListRasters("*30N_120E.tif", "TIF"):
    print "Extracting Batanes"
    env.workspace = (r"C:\thesis\LATEST\Overlay Agreements\5_over_5")
    #print raster #checking the presence of raster
    g = "Batanes.shp"
    outputRasterExtractbyMask = ExtractByMask(raster, g)
    prov = g.replace(".shp", "_")
    outputRasterExtractbyMask_Name = prov + raster
    env.workspace = (r"C:\thesis\LATEST\Overlay Agreements\5_over_5\Per Region")
    outputRasterExtractbyMask.save(outputRasterExtractbyMask_Name)"""


print "Finish"
