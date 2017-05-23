import arcpy
import collections
from arcpy import env

env.overwriteOutput = True

#Set the current workspace
arcpy.env.workspace = r"C:\thesis"

#define the mxd and for loop the layers
mxd = arcpy.mapping.MapDocument(r"C:\thesis\sampling.mxd")
df = arcpy.mapping.ListDataFrames(mxd)[0]
output_folder = r"C:\thesis\for_sampling\sampling_outputs\feature_per_biogeoregion\PCS.gdb"
"""for layer in arcpy.mapping.ListLayers(mxd): # This format was the older version 
    print layer.name
    if layer.visible:
        arcpy.RefreshTOC()
        arcpy.RefreshActiveView()      
        #arcpy.FeatureClassToFeatureClass_conversion(layer, output_folder, layer.name + "_sample.")
        count = int(arcpy.GetCount_management(layer).getOutput(0)) # counting the total feature on a  visible layer
        print count"""
for layer in arcpy.mapping.ListLayers(mxd, "PCS*", df):
        Sel=arcpy.Describe(layer)
        print  Sel.nameString
        if Sel.FIDset == Sel.FIDset:
            arcpy.FeatureClassToFeatureClass_conversion(layer,output_folder,layer.name + "one_pixel")
            print Sel.nameString + " is Finished!"
        else:
            print "may mali sa code mo!"

#to determine the number of al features per layer in mxd
"""for layer in arcpy.mapping.ListLayers(mxd): #this is the easiest method! 
    print layer.name
    count = int(arcpy.GetCount_management(layer).getOutput(0))
    print count
    with arcpy.da.SearchCursor(layer, "FID") as cur:
        count_of_items = collections.Counter(row[0] for row in cur)
        print "Sorted items"
        print "----"
        for item in sorted(count_of_items.items(), key=lambda x:x[1]):
            print "{0:>12} {1:>4}".format(item[0], item[1])# use this to get a count of unique features (jason scheirer)
    with arcpy.da.SearchCursor(layer, ["FID"]) as cursor: arcgis help, search arcpy.da.cursor
            rows = {row[0] for row in cursor}
            count = 0
            for row in rows:
                count += 1
print "%s features" % count"""

print "Finish"








