#import the module
import arcpy
from arcpy import env

#set the workspace, output as true, compression
env.workspace = r"C:\thesis\for_sampling\sampling_outputs"
env.overwriteOutput = True
env.compression = "LZW"

#outFolder = r"C:\thesis\for_sampling\sampling_outputs"
#Get a list of features and dissolve them
for fc in arcpy.ListFeatureClasses("*_*"):
    print "Dissolving " + fc
    #oName, oExt = os.path.splitext(fc)
    #outFeature = os.path.join(outFolder, oName+ ".shp")
    arcpy.Dissolve_management(fc, r"C:\thesis\for_sampling\sampling_outputs\\" + "dissolved"+fc, "GRIDCODE")



print "Finish!"




