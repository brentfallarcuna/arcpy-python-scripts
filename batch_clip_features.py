import arcpy, os
from arcpy import env
env.overwriteOutput = True
env.workspace = r"C:\Users\Brent\Documents\Mangrove_Change_Detection\GCS"
outpath = r"C:\Users\Brent\Documents\Mangrove_Change_Detection\GCS\Zamboanga Only"
#inputs

#output_Folder = r"C:\Users\brentiebark\Documents\Diane Samar and Leyte\Samar\Samar_final.gdb"
for k in arcpy.ListFeatureClasses("0*", "All"):
    print "Clipping " + k + " portion"
    arcpy.Clip_analysis(k, r"C:\Users\Brent\Downloads\Region shapefiles WGS 84 used in thesis\IX.shp",
                           outpath+os.sep+"IX_only"+k)

print "Finish!"


