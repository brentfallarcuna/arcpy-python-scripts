 #import the module
import arcpy
import arcpy.mapping as mapping
from arcpy import env
env.overwriteOutput = True

"""Here, [19] is for Quezon_tiffs.mxd and
[14] for Land_Cover_Type.mxd and  Quezon_gain.mxd also"""


#set the map document
mxd = mapping.MapDocument(r"C:\thesis\Quezon_gain.mxd")
#set the data frame (only one data frame!)
df = mapping.ListDataFrames(mxd)[0]
#set the basis for the layer legend
basisLayer = mapping.Layer(r"C:\thesis\hansenwipfiles\GAIN.lyr")
#print the year 2000 text element
#for u in mapping.ListLayoutElements(mxd, "TEXT_ELEMENT"):
print mapping.ListLayoutElements(mxd, "TEXT_ELEMENT")[14].name

#loop update the symbology!
for layer in mapping.ListLayers(mxd):
        #mapping.UpdateLayer(df, layer, basisLayer)
        layer.visible = True
        print "Processing year " + layer.name
        mapping.ListLayoutElements(mxd, "TEXT_ELEMENT")[14].text = layer.name
        mapping.ListLayoutElements(mxd, "TEXT_ELEMENT")[14].elementPositionX = 3.10
        mapping.ListLayoutElements(mxd, "TEXT_ELEMENT")[14].elementPositionY = 11.18
        mapping.ExportToPNG(mxd, r"C:\thesis\giff_assorted_provinces\\" + layer.name  + "_General_Nakar" + ".png",\
                            "PAGE_LAYOUT", resolution = 700)
        layer.visible = False
mxd.save()
del mxd

print "Finish!"
