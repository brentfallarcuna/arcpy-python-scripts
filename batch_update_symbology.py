#import the modules
import arcpy
import arcpy.mapping as mapping
from arcpy import env
env.overwriteOutput = True


#set the workspace
arcpy.env.workspace = (r"C:\thesis")

#set the map document
mxd = mapping.MapDocument(r"C:\thesis\Thesis_test_Maps.mxd")

#set the data frame (only one data frame!)
df = mapping.ListDataFrames(mxd)[0]

#set the basis for the layer legend
basis_NDVI = mapping.Layer(r"C:\thesis\hansenwipfiles\2000_85to100_dark.lyr")
#print basis_NDVI

#update the layers!
for layer in mapping.ListLayers(mxd, "new*forests_onlytreecover2000*.tif", df):
    print "Updating this " + layer.name
    mapping.UpdateLayer(df, layer, basis_NDVI)


"""#loop update the symbology!
print "processing NOCHANGE!"
for layer in mapping.ListLayers(mxd, "*nochange*", df):
    print layer.name
    mapping.UpdateLayer(df, layer, basisLayer_nc)

print "processing LOSSYEAR"
#set the basis for the layer legend
basisLayer_lossyear = mapping.Layer(r"C:\thesis\hansenwipfiles\luzon_lossyear_GE.lyr")
#loop update the symbology!
for layer in mapping.ListLayers(mxd, "*loss*", df):
    print layer.name
    mapping.UpdateLayer(df, layer, basisLayer_lossyear)

print "processing GAIN"
#set the basis for the layer legend
basisLayer_gain = mapping.Layer(r"C:\thesis\hansenwipfiles\luzon_gain_GE.lyr")
#loop update the symbology!
for layer in mapping.ListLayers(mxd, "*gain*", df):
    print layer.name
    mapping.UpdateLayer(df, layer, basisLayer_gain)"""

mxd.save()
del mxd
print "Finish!"












