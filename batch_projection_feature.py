import arcpy, os
from arcpy import env
env.overwriteOutput = True

#Set the current workspace
env.workspace = r"C:\Users\Brent\Dropbox\Tenure Instrument_mapcoding"
inpath = env.workspace
outpath = r"C:\Users\Brent\Downloads\Tenure instruments"
for fc in arcpy.ListFeatureClasses("*", "All"):
    print "Projecting " + fc
    #get the coordinate system by describing a feature class
    dsc = arcpy.Describe(r"C:\Users\Brent\Downloads\Region shapefiles WGS 84 used in thesis\ARMM.shp")
    coord_sys = dsc.SpatialReference
    arcpy.Project_management(os.path.join(inpath, fc), outpath+os.sep+"WGS84_"+fc, coord_sys)

print "Finish"






