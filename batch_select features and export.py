import arcpy, os
from arcpy import env
import arcpy.mapping as mapping
env.overwriteOutput = True
#Set the current workspace
arcpy.env.workspace = r"C:\thesis\LATEST\TREES\Per Region\new lossyear\newlossyear.gdb"
ws = arcpy.env.workspace
#define the mxd and data frame
mxd = arcpy.mapping.MapDocument(r"C:\thesis\Thesis_test_Maps.mxd")
df = arcpy.mapping.ListDataFrames(mxd)[0]

#adding the layers
for fc in arcpy.ListFeatureClasses("gdb*"):
        y = os.path.join(ws, fc)
        newlayer = arcpy.mapping.Layer(y)
        arcpy.mapping.AddLayer(df, newlayer,"AUTO_ARRANGE")
        print "This layer is added: " + y
#5111.2692
print "############################################"

output_folder = r"C:\thesis\LATEST\TREES\Per Region\new lossyear\one_pixel.gdb"
#wildcardList = ["gdb*nochange", "gdb*lossyear","gdb*gain"]
#for k in range(0,3):
#This is to remove the extra feature in the shapefile
for layer in arcpy.mapping.ListLayers(mxd, "gdb*", df):
        #print "Processing this Wilcard " + str(k)
        print "Processing this layer "+ layer.name
        arcpy.SelectLayerByAttribute_management(layer, "NEW_SELECTION",  ' "Shape_Area"  < 0.01')#' "Shape_Area"  <= 6.25000000965201E-08 ')
        arcpy.FeatureClassToFeatureClass_conversion(layer, output_folder, layer.name + "one_pixel")
        #o=str(arcpy.GetCount_management(layer))
        #print o+ "   <=== This is the total feature count of " + layer.name

print "###########################################"

"""#remove the layers
for fc in arcpy.mapping.ListLayers(mxd, "gdb*", df):
        print "Removing this layer" + fc
        arcpy.mapping.RemoveLayer(df, fc)

mxd.save()
del mxd"""

print "Finish!"








