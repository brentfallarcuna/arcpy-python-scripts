#import the module
import arcpy, os
import arcpy.mapping as mapping
from arcpy import env
env.overwriteOutput = True

#set the map document
mxd = mapping.MapDocument(r"C:\thesis\Land_Cover_Type_Zamboanga_del_Norte.mxd")
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
"""for k in mapping.ListLayers(mxd, "*", df):
    print k.name
    k.visible = True
    k.showLabels = False"""

#print the year 2000 text element
#for u in mapping.ListLayoutElements(mxd, "TEXT_ELEMENT"):
    #print u.name
#print mapping.ListLayoutElements(mxd, "TEXT_ELEMENT")[14].name
#loop update the symbology!
for layer in mapping.ListLayers(mxd, "2*", df):
    mapping.UpdateLayer(df, layer, basisLayer)
    layer.visible = True
    print "Processing year " + layer.name
    mapping.ListLayoutElements(mxd, "TEXT_ELEMENT")[14].text = layer.name
    mapping.ListLayoutElements(mxd, "TEXT_ELEMENT")[14].elementPositionX = 1.825
    mapping.ListLayoutElements(mxd, "TEXT_ELEMENT")[14].elementPositionY = 10.8892
    mapping.ExportToTIFF(mxd, r"C:\thesis\giff_assorted_provinces\Zamboanga giffs\ZDN\\" + "Tenure"+ layer.name + ".tif",
    "PAGE_LAYOUT", resolution = 250)
    layer.visible = False
#mxd.save()
#del mxd
print "Finish!"
