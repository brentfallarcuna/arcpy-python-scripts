import arcpy, os
from arcpy import env
from arcpy.sa import *
arcpy.CheckOutExtension("Spatial")
env.overwriteOutput = True


#Set the current workspace
env.workspace = r"C:\thesis\LATEST\LATEST Forest Masks (with 2013 loss)\NAMRIA\Per Province"
env.nodata = "MINIMUM"
env.compression = "LZ77"

# All tiles are included here!
listsRasters = ['Zamboanga Sib*10N_120E.tif']#'Quezon*20N_120E.tif','Palawan*10N_110E.tif','Southern Leyte*20N_120E.tif',]#,'*30N_120E.tif']

for i in listsRasters:
        print  "Extracting this tile: " + i
        env.workspace = r"C:\thesis\LATEST\LATEST Forest Masks (with 2013 loss)\NAMRIA\Per Province"
        #This is for extracting the particular forest landform by from the Provinces_forest_only
        for raster in arcpy.ListRasters(i, "TIF"):
            env.workspace = r"C:\thesis\LATEST\LATEST Forest Masks (with 2013 loss)\NAMRIA\Per Province"
            print "    Extracting Siay study from this raster: "+ raster #checking the presence of raster
            outputRasterExtractbyMask = ExtractByMask(raster, "Siay.shp")
            outFolder = r"C:\thesis\Zamboanga Sib and del Norte"
            oName, oExt = os.path.splitext(raster)
            outRaster = os.path.join(outFolder, oName+ "Siay.tif")
            outputRasterExtractbyMask_Name = outRaster
            env.workspace = r"C:\thesis\Zamboanga Sib and del Norte"
            outputRasterExtractbyMask.save(outputRasterExtractbyMask_Name)

print "Finish Extracting (Sibugay)"
