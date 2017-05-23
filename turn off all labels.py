#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Brent
#
# Created:     04/04/2016
# Copyright:   (c) Brent 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#import the module
import arcpy, os
import arcpy.mapping as mapping
from arcpy import env
env.overwriteOutput = True

#set the map document
mxd = mapping.MapDocument(r"C:\thesis\For Journal Publication.mxd")
#set the data frame (only one data frame!)
df = mapping.ListDataFrames(mxd)[0]

"""###################################
#Adding the the layers from a file .gdb
env.workspace = r"C:\thesis\giff_assorted_provinces\new_lossyears_raster\Nakar_final.gdb"
ws = env.workspace
for fc in arcpy.ListFeatureClasses("gdb*"):
        y = os.path.join(ws, fc)
        newlayer = arcpy.mapping.Layer(y)
        arcpy.mapping.AddLayer(df, newlayer,"AUTO_ARRANGE")
        print "This layer is added: " + y
###################################"""

#set the basis for the layer legend
basisLayer = mapping.Layer(r"C:\thesis\hansenwipfiles\Land Cover.lyr")
for k in mapping.ListLayers(mxd, "*", df):
    print k.name
    k.visible = True
    k.showLabels = True

mxd.save()
#del mxd
print "Finish! ok na!"

