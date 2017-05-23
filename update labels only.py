#-------------------------------------------------------------------------------
# Name:        update labels only
# Purpose:   changes the label's font only
#
# Author:      Brent
#
# Created:     06/08/2016
# Copyright:   (c) Brent 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import arcpy
import arcpy.mapping as mapping
from arcpy import env
env.overwriteOutput = True

#set the map document
mxd = mapping.MapDocument(r"C:\thesis\For Journal Publication.mxd")

#set the data frame (only two data frames!)
df = mapping.ListDataFrames(mxd)[1]

#set the layer Cebu
lyr = arcpy.mapping.ListLayers(mxd, "*", df)[4]
print lyr.name

for l in mapping.ListLayers(mxd, "*", df):
    print l.name
    mapping.UpdateLayer(df, l, lyr, "False")

mxd.saveACopy(r"C:\thesis\For Journal Publication2.mxd")
del mxd
print "Finish!"

