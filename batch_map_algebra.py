#import all neccessary modules 
import arcpy, arcview, os
from arcpy import env
from arcpy.sa import Raster, Float
env.overwriteOutput = True
arcpy.CheckOutExtension("Spatial")
arcpy.env.workspace = r"C:\thesis\hansenwipfiles\first and last v1.0"

def get_bands(path_to_raster):
    """ Get a list of bands as Raster objects from a multiband raster """
    oldws = arcpy.env.workspace #Save previous workspace
    #Get raster objects from band names
    arcpy.env.workspace = path_to_raster
    bands = [Raster(os.path.join(path_to_raster, b)) for b in arcpy.ListRasters()]
    #Restore previous workspace
    arcpy.env.workspace = oldws
    return bands;

for i in arcpy.ListRasters("subset*", "TIF"): 
      #Use the function above
      band = get_bands(r"C:\thesis\hansenwipfiles\first and last v1.0\\" + i)      
      #Raster List (Assuming the rasters here are already single bands)
      print "     Processing this raster " + i
      ratio = Float(band[1] / band[0]) #ratio
      #ndvi = (Float(band[1] - band[0])) / (Float(band[1] + band[0])) #ndvi
      (oName, oExt) = os.path.splitext(i)
      oName_new = oName.replace("subset","Ratiogb")
      ndviName = r"C:\thesis\hansenwipfiles\first and last v1.0\NDVIandRatio.gdb\\" + oName_new
      ndvi.save(ndviName)
      print "  This " + i + " is Finished!"

  
print "Finish all of them"
