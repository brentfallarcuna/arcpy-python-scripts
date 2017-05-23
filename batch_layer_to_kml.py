import arcpy, os
from arcpy import env
import arcpy.mapping as mapping

#Set the current workspace etc.
arcpy.env.workspace = r"C:\Users\Brent\OneDrive"
ws = arcpy.env.workspace
env.overwriteOutput = True
mxd = mapping.MapDocument(r"C:\Users\Brent\OneDrive\Mangroves_PTFCF.mxd")
df = mapping.ListDataFrames(mxd)[0]
dfnew = mapping.ListDataFrames(mxd)[1]

"""#add the layer
print "############################################"
for fc in arcpy.ListFeatureClasses():
        y = os.path.join(ws, fc)
        newlayer = arcpy.mapping.Layer(y)
        arcpy.mapping.AddLayer(dfnew, newlayer,"AUTO_ARRANGE")
        print "This layer is added: " + y
print "############################################"

#print "############################################
##Updating the layer
#set the basis for the layer legend
basisLayer_nc= mapping.Layer(r"C:\thesis\hansenwipfiles\luzon_nochange_GE.lyr")

#loop update the symbology!
print "processing NOCHANGE!"
for layer in mapping.ListLayers(mxd, "*nochange_final", df):
        print layer.name
        mapping.UpdateLayer(df, layer, basisLayer_nc)

print "processing LOSSYEAR"
#set the basis for the layer legend
basisLayer_lossyear = mapping.Layer(r"C:\thesis\hansenwipfiles\luzon_lossyear_GE_new.lyr")
#loop update the symbology!
for layer in mapping.ListLayers(mxd, "*Forest*", dfnew):
        print layer.name
        mapping.UpdateLayer(dfnew, layer, basisLayer_lossyear)

print "processing GAIN"
#set the basis for the layer legend
basisLayer_gain = mapping.Layer(r"C:\thesis\hansenwipfiles\luzon_gain_GE.lyr")
#loop update the symbology!
for layer in mapping.ListLayers(mxd, "*gain_final", df):
        print layer.name
        mapping.UpdateLayer(df, layer, basisLayer_gain)
print "############################################

arcpy.env.workspace = r"C:\Users\brentiebark\Dropbox\Thesis Results\Field Work Related\General Nakar\GPX GPS"
ws = arcpy.env.workspace
for lyr in mapping.ListLayers(mxd, "waypoint*"):
    print lyr.name + " will be converted to .kmz"
    outputName = lyr.name
    arcpy.LayerToKML_conversion(lyr, os.path.join(ws, outputName +".kmz"), "", "", "", "1096", "96")

arcpy.env.workspace = r"C:\Users\brentiebark\Dropbox\Thesis Results\Field Work Related\General Nakar\GPX GPS"
ws = arcpy.env.workspace
for lyr in mapping.ListLayers(mxd, "track*"):
    print lyr.name + " will be converted to .kmz"
    outputName = lyr.name
    arcpy.LayerToKML_conversion(lyr, os.path.join(ws, outputName +".kmz"), "", "", "", "1096", "96")"""

#convert all the layers to kml (lahatan ito, hindi ito sample!)
arcpy.env.workspace = r"C:\Users\Brent\OneDrive"
ws = arcpy.env.workspace
for i in mapping.ListLayers(mxd, "IX*", df):
    print "This will be converted to kmz:", i.name
    outputName = i.name
    arcpy.LayerToKML_conversion(i, os.path.join(ws, outputName +".kmz"), "", "", "", "1096", "96")


print "Finish!"