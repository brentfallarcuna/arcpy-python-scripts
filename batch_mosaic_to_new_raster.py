#This is for mosaicing rasters
import arcpy
from arcpy import env
env.overwriteOutput = True

#Set the current workspace and other env 't variables
env.workspace = r"C:\thesis\LATEST\Overlay Agreements\5_over_5\Per Province"
env.nodata = "NONE"
env.compression = "LZ77"

list_all_rasters_gain = ["newgain_Luzon_20N_110E.tif;newgain_Luzon_20N_120E.tif",\
"newgain_Mindanao_10N_110E.tif;newgain_Mindanao_10N_120E.tif;newgain_Mindanao_20N_120E.tif",\
"newgain_Negros_Panay_10N_120E.tif;newgain_Negros_Panay_20N_120E.tif",\
"newgain_Palawan_10N_110E.tif;newgain_Palawan_20N_110E.tif;newgain_Palawan_20N_120E.tif"]
output_list = ["Luzon_gain","Mindanao_gain","Negros_Panay_gain","Palawan_gain"]
env.workspace = r"C:\thesis\for_sampling\sampling_outputs\new_gain"

for t in range(0,4):
      print t
      print "Processing gain"# checking the list
      arcpy.MosaicToNewRaster_management(list_all_rasters_gain[t], r"C:\thesis\for_sampling\sampling_outputs\mosaicked_outputs.gdb",\
      output_list[t], "GCS_WGS_1984.prj", "1_BIT", "0.00025", 1)

print "new gain mosaicking Finished!"

list_all_rasters_lossyear = ["lossyear_Luzon_20N_110E.tif;lossyear_Luzon_20N_120E.tif",\
"lossyear_Mindanao_10N_110E.tif;lossyear_Mindanao_10N_120E.tif;lossyear_Mindanao_20N_120E.tif",\
"lossyear_Negros_Panay_10N_120E.tif;lossyear_Negros_Panay_20N_120E.tif",\
"lossyear_Palawan_10N_110E.tif;lossyear_Palawan_20N_110E.tif;lossyear_Palawan_20N_120E.tif"]
output_list = ["Luzon_lossyear","Mindanao_lossyear","Negros_Panay_lossyear","Palawan_lossyear"]
env.workspace = r"C:\thesis\for_sampling\sampling_outputs\new_lossyear"
for f in range(0,4):
      print f
      print " Processing lossyear"# checking the list
      arcpy.MosaicToNewRaster_management(list_all_rasters_lossyear[f], r"C:\thesis\for_sampling\sampling_outputs\mosaicked_outputs.gdb",\
      output_list[f], "GCS_WGS_1984.prj", "4_BIT", "0.00025", 1)

print "lossyear mosaicking Finished!"


list_all_rasters_nochange = ["nochange_Luzon_20N_110E.tif;nochange_Luzon_20N_120E.tif",\
"nochange_Mindanao_10N_110E.tif;nochange_Mindanao_10N_120E.tif;nochange_Mindanao_20N_120E.tif",\
"nochange_Negros_Panay_10N_120E.tif;nochange_Negros_Panay_20N_120E.tif",\
"nochange_Palawan_10N_110E.tif;nochange_Palawan_20N_110E.tif;nochange_Palawan_20N_120E.tif"]
output_list = ["Luzon_nochange","Mindanao_nochange","Negros_Panay_nochange","Palawan_nochange"]
env.workspace = r"C:\thesis\for_sampling\sampling_outputs\nochange"
for f in range(0,4):
      print f
      print " Processing nochange"# checking the list
      arcpy.MosaicToNewRaster_management(list_all_rasters_nochange[f], r"C:\thesis\for_sampling\sampling_outputs\mosaicked_outputs.gdb",\
      output_list[f], "GCS_WGS_1984.prj", "1_BIT", "0.00025", 1)

print "no change mosaicking Finished!"


print "Finish all of them!"
