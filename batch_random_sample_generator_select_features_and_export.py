import random, os
import arcpy
from arcpy import env, mapping
arcpy.env.overwriteOutput = True
#Set the current workspace
arcpy.env.workspace = r"C:\thesis\for_sampling\sampling_outputs\feature_per_biogeoregion\one_pixel.gdb"
ws = arcpy.env.workspace
#define the mxd and data frame
mxd = mapping.MapDocument(r"C:\thesis\sampling.mxd")
df = mapping.ListDataFrames(mxd)[0]
output_folder = r"C:\thesis\for_sampling\sampling_outputs\bigger_samples_160"

#for u in mapping.ListLayers(mxd, "*", df):
print mapping.ListLayers(mxd, "*", df)[51].name
"""
print "############################################"
for fc in arcpy.ListFeatureClasses():
        y = os.path.join(ws, fc)
        newlayer = arcpy.mapping.Layer(y)
        arcpy.mapping.AddLayer(df, newlayer,"AUTO_ARRANGE")
        print "This layer is added: " + y
print "############################################"
"""
print "###############################################################################"
print "           Processing Luzon GAIN"
u= "FID in "
n = str(random.sample(range(11176), 32))
k = n.replace("[","(")
o = k.replace("]",")")
b = str(u + o)
gainLuzonlyr = mapping.ListLayers(mxd, "*", df)[40]
print b
print gainLuzonlyr
arcpy.SelectLayerByAttribute_management(gainLuzonlyr, "NEW_SELECTION", b)
arcpy.FeatureClassToFeatureClass_conversion(gainLuzonlyr, output_folder, gainLuzonlyr.name.replace("gain","gain_final"))

print "           Processing MIN GAIN"
n = str(random.sample(range(10286), 32))
k = n.replace("[","(")
o = k.replace("]",")")
b = str(u + o)
gainLuzonlyr = mapping.ListLayers(mxd, "*", df)[41]
print gainLuzonlyr
arcpy.SelectLayerByAttribute_management(gainLuzonlyr, "NEW_SELECTION", b)
arcpy.FeatureClassToFeatureClass_conversion(gainLuzonlyr, output_folder, gainLuzonlyr.name.replace("gain","gain_final"))

print "           Processing NP GAIN"
n = str(random.sample(range(401), 32))
k = n.replace("[","(")
o = k.replace("]",")")
b = str(u + o)
gainLuzonlyr = mapping.ListLayers(mxd, "*", df)[42]
print gainLuzonlyr
arcpy.SelectLayerByAttribute_management(gainLuzonlyr, "NEW_SELECTION", b)
arcpy.FeatureClassToFeatureClass_conversion(gainLuzonlyr, output_folder, gainLuzonlyr.name.replace("gain","gain_final"))


print "           Processing PAL GAIN"
u= "FID in "
n = str(random.sample(range(4202), 32))
k = n.replace("[","(")
o = k.replace("]",")")
b = str(u + o)
gainLuzonlyr = mapping.ListLayers(mxd, "*", df)[43]
print gainLuzonlyr
arcpy.SelectLayerByAttribute_management(gainLuzonlyr, "NEW_SELECTION", b)
arcpy.FeatureClassToFeatureClass_conversion(gainLuzonlyr, output_folder, gainLuzonlyr.name.replace("gain","gain_final"))
print "###############################################################################"

print "           Processing Luzon LOSS"
n = str(random.sample(range(78527), 48))
k = n.replace("[","(")
o = k.replace("]",")")
b = str(u + o)
gainLuzonlyr = mapping.ListLayers(mxd, "*", df)[44]
print gainLuzonlyr
arcpy.SelectLayerByAttribute_management(gainLuzonlyr, "NEW_SELECTION", b)
arcpy.FeatureClassToFeatureClass_conversion(gainLuzonlyr, output_folder, gainLuzonlyr.name.replace("lossyear","lossyear_final"))

print "           Processing MIN LOSS"
n = str(random.sample(range(47855), 48))
k = n.replace("[","(")
o = k.replace("]",")")
b = str(u + o)
gainLuzonlyr = mapping.ListLayers(mxd, "*", df)[45]
print gainLuzonlyr
arcpy.SelectLayerByAttribute_management(gainLuzonlyr, "NEW_SELECTION", b)
arcpy.FeatureClassToFeatureClass_conversion(gainLuzonlyr, output_folder, gainLuzonlyr.name.replace("lossyear","lossyear_final"))

print "           Processing NP LOSS"
u= "FID in "
n = str(random.sample(range(2772), 48))
k = n.replace("[","(")
o = k.replace("]",")")
b = str(u + o)
gainLuzonlyr = mapping.ListLayers(mxd, "*", df)[46]
print gainLuzonlyr
arcpy.SelectLayerByAttribute_management(gainLuzonlyr, "NEW_SELECTION", b)
arcpy.FeatureClassToFeatureClass_conversion(gainLuzonlyr, output_folder, gainLuzonlyr.name.replace("lossyear","lossyear_final"))

print "           Processing PAL LOSS"
n = str(random.sample(range(16021), 48))
k = n.replace("[","(")
o = k.replace("]",")")
b = str(u + o)
gainLuzonlyr = mapping.ListLayers(mxd, "*", df)[47]
print gainLuzonlyr
arcpy.SelectLayerByAttribute_management(gainLuzonlyr, "NEW_SELECTION", b)
arcpy.FeatureClassToFeatureClass_conversion(gainLuzonlyr, output_folder, gainLuzonlyr.name.replace("lossyear","lossyear_final"))
print "###############################################################################"
print "           Processing LUZON NOCHANGE"
n = str(random.sample(range(44811), 80))
k = n.replace("[","(")
o = k.replace("]",")")
b = str(u + o)
gainLuzonlyr = mapping.ListLayers(mxd, "*", df)[48]
print gainLuzonlyr
arcpy.SelectLayerByAttribute_management(gainLuzonlyr, "NEW_SELECTION", b)
arcpy.FeatureClassToFeatureClass_conversion(gainLuzonlyr, output_folder, gainLuzonlyr.name.replace("nochange","nochange_final"))


print "           Processing MIN NOCHANGE"
u= "FID in "
n = str(random.sample(range(29646), 80))
k = n.replace("[","(")
o = k.replace("]",")")
b = str(u + o)
gainLuzonlyr = mapping.ListLayers(mxd, "*", df)[49]
print gainLuzonlyr
arcpy.SelectLayerByAttribute_management(gainLuzonlyr, "NEW_SELECTION", b)
arcpy.FeatureClassToFeatureClass_conversion(gainLuzonlyr, output_folder, gainLuzonlyr.name.replace("nochange","nochange_final"))

print "           Processing NP NOCHANGE"
n = str(random.sample(range(6458), 80))
k = n.replace("[","(")
o = k.replace("]",")")
b = str(u + o)
gainLuzonlyr = mapping.ListLayers(mxd, "*", df)[50]
print gainLuzonlyr
arcpy.SelectLayerByAttribute_management(gainLuzonlyr, "NEW_SELECTION", b)
arcpy.FeatureClassToFeatureClass_conversion(gainLuzonlyr, output_folder, gainLuzonlyr.name.replace("nochange","nochange_final"))

print "           Processing PAL NOCHANGE"
n = str(random.sample(range(12191), 80))
k = n.replace("[","(")
o = k.replace("]",")")
b = str(u + o)
gainLuzonlyr = mapping.ListLayers(mxd, "*", df)[51]
print gainLuzonlyr
arcpy.SelectLayerByAttribute_management(gainLuzonlyr, "NEW_SELECTION", b)
arcpy.FeatureClassToFeatureClass_conversion(gainLuzonlyr, output_folder, gainLuzonlyr.name.replace("nochange","nochange_final"))
print "###############################################################################"

"""
print "removing the layers"
for fc in arcpy.mapping.ListLayers(mxd, "gdb*", df):
        print "removing this layer"
        print fc
        arcpy.mapping.RemoveLayer(df, fc)"""

#mxd.save()"""
del mxd

print "Finish!"





