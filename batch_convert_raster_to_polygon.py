#import the module
import arcpy
from arcpy.sa import *
from arcpy import env
arcpy.CheckOutExtension("Spatial")
env.overwriteOutput = True

#set the workspace
arcpy.env.workspace = r"C:\Users\Windows\Documents\JO_GIS_Analyst"

#Get a list of raster and convert it to integer
for raster in arcpy.ListRasters("phil_onlyreprojected*", "TIF"):
    print raster #check the presence of rasters
    OutRaster = Int(Raster(raster)*1000000) #multiplying the raster by 100, preserving only 2 decimal places
    OutRaster_Name = "nofpt" + raster  #specifying the output name
    OutRaster.save(OutRaster_Name) #saving the raster
print "Finish multiplying the raster by 100"

#Get a list of rasters and reclassify it, you opt not to use this if were going to preserved the real values
for raster in arcpy.ListRasters("nofptphil_onlyreprojected*", "TIF"):
    print raster #check the presence of rasters
    #set the remap range
    remap = RemapRange([[995000,1000000,1000000],[985000,994000,990000],[975000,984000,980000],[965000,974000,970000],[955000,964000,960000],[945000,954000,950000],[935000,944000,940000],[925000,934000,930000],[915000,924000,920000],[905000,914000,910000],
                                       [895000,904000,900000],[885000,894000,890000],[875000,884000,880000],[865000,874000,870000],[855000,864000,860000],[845000,854000,850000],[835000,844000,840000],[825000,834000,830000],[815000,824000,820000],[805000,814000,810000],
                                       [795000,804000,800000],[785000,794000,790000],[775000,784000,780000],[765000,774000,770000],[755000,764000,760000],[745000,754000,750000],[735000,744000,740000],[725000,734000,730000],[715000,724000,720000],[705000,714000,710000],
                                       [695000,704000,700000],[685000,694000,690000],[675000,684000,680000],[665000,674000,670000],[655000,644000,660000],[645000,654000,650000],[635000,644000,640000],[625000,634000,630000],[615000,624000,620000],[605000,614000,610000],
                                       [595000,604000,600000],[585000,594000,590000],[575000,584000,580000],[565000,574000,570000],[555000,564000,560000],[545000,554000,550000],[535000,544000,540000],[525000,534000,530000],[515000,524000,520000],[505000,514000,510000],
                                       [495000,504000,500000],[485000,494000,490000],[475000,484000,480000],[465000,474000,470000],[455000,464000,460000],[445000,454000,450000],[450000,444000,440000],[425000,434000,430000],[415000,424000,420000],[405000,414000,410000],
                                       [395000,404000,400000],[385000,394000,390000],[375000,384000,380000],[365000,374000,370000],[355000,364000,360000],[345000,354000,350000],[335000,344000,340000],[325000,334000,330000],[315000,324000,320000],[305000,314000,310000],
                                       [295000,304000,300000],[285000,294000,290000],[275000,284000,280000],[265000,274000,270000],[255000,264000,260000],[245000,254000,250000],[250000,244000,240000],[225000,234000,230000],[215000,224000,220000],[205000,214000,210000],
                                       [195000,204000,200000],[185000,194000,190000],[175000,184000,180000],[165000,174000,170000],[155000,164000,160000],[145000,154000,150000],[115000,144000,140000],[125000,134000,130000],[115000,124000,120000],[105000,114000,110000],
                                       [95000,104000,100000],[85000,94000,90000],[75000,84000,80000],[65000,74000,70000],[55000,64000,60000],[45000,54000,50000],[35000,44000,40000],[25000,34000,30000],[15000,24000,20000],[5000,14000,10000],[4000,-4000,0],
                                       [-14000,-5000,-10000],[-24000,-15000,-20000],[-34000,-25000,-30000],[-44000,-35000,-40000],[-54000,-45000,-50000],[-64000,-55000,-60000],[-74000,-65000,-70000],[-84000,-75000,-80000],[-94000,-85000,-90000],
                                       [-104000,-95000,-100000],[-114000,-105000,-110000],[-124000,-115000,-120000],[-134000,-125000,-130000],[-144000,-135000,-140000],[-154000,-145000,-150000],[-164000,-155000,-160000],[-174000,-165000,-170000],[-184000,-175000,-180000],[-194000,-185000,-190000],[-204000,-195000,-200000],
                                       [-204000,-195000,-200000],[-214000,-205000,-210000],[-224000,-215000,-220000],[-234000,-225000,-230000],[-244000,-235000,-240000],[-254000,-245000,-250000],[-264000,-255000,-260000],[-274000,-265000,-270000],[-284000,-275000,-280000],[-294000,-285000,-290000],[-304000,-295000,-300000],
                                       [-304000,-295000,-300000],[-314000,-305000,-310000],[-324000,-315000,-320000],[-334000,-325000,-330000],[-344000,-335000,-340000],[-354000,-345000,-350000],[-364000,-355000,-360000],[-374000,-365000,-370000],[-384000,-375000,-380000],[-394000,-385000,-390000],[-404000,-395000,-400000],
                                       [-404000,-395000,-400000],[-414000,-405000,-410000],[-424000,-415000,-420000],[-434000,-425000,-430000],[-444000,-435000,-440000],[-454000,-445000,-450000],[-464000,-455000,-460000],[-474000,-465000,-470000],[-484000,-475000,-480000],[-494000,-485000,-490000],[-504000,-495000,-500000],
                                       [-504000,-495000,-500000],[-514000,-505000,-510000],[-524000,-515000,-520000],[-534000,-525000,-530000],[-544000,-535000,-540000],[-554000,-545000,-550000],[-564000,-555000,-560000],[-574000,-565000,-570000],[-584000,-575000,-580000],[-594000,-585000,-590000],[-604000,-595000,-600000],
                                       [-604000,-595000,-600000],[-614000,-605000,-610000],[-624000,-615000,-620000],[-634000,-625000,-630000],[-644000,-635000,-640000],[-654000,-645000,-650000],[-664000,-655000,-660000],[-674000,-665000,-670000],[-684000,-675000,-680000],[-694000,-685000,-690000],[-704000,-695000,-700000],
                                       [-704000,-695000,-700000],[-714000,-705000,-710000],[-724000,-715000,-720000],[-734000,-725000,-730000],[-744000,-735000,-740000],[-754000,-745000,-750000],[-764000,-755000,-760000],[-774000,-765000,-770000],[-784000,-775000,-780000],[-794000,-785000,-790000],[-804000,-795000,-800000],
                                       [-804000,-795000,-800000],[-814000,-805000,-810000],[-824000,-815000,-820000],[-834000,-825000,-800000],[-884000,-835000,-840000],[-854000,-845000,-850000],[-864000,-855000,-860000],[-874000,-865000,-870000],[-884000,-875000,-880000],[-894000,-885000,-890000],[-904000,-895000,-900000],
                                       [-904000,-895000,-900000],[-914000,-905000,-910000],[-924000,-915000,-920000],[-934000,-925000,-930000],[-940000,-935000,-940000],[-954000,-945000,-950000],[-964000,-955000,-960000],[-974000,-965000,-970000],[-984000,-975000,-980000],[-994000,-985000,-990000],[-995000,-1000000,-1000000]])
                            
                                       
                                       
    outReclassify = Reclassify(raster,  "Value",  remap, "NODATA")
    outReclassify_Name = "reclass" + raster #specifying the output name
    outReclassify.save(outReclassify_Name) #saving the reclassified raster
print "Finish reclassifying the raster"

#Get a list of rasters and convert to shapefile
for raster in arcpy.ListRasters("reclassnofptphil_onlyreprojected*", "TIF"):
    print raster #check the presence of rasters
    #convert the raster to polygon
    arcpy.RasterToPolygon_conversion(raster,  raster.replace("tif", "shp"), "SIMPLIFY")
print "Finish converting all the rasters to polygon"

#Get a list of feature classes, add and calculate the new field
for fc in arcpy.ListFeatureClasses("reclassnofptphil_onlyreprojected*"):
    print fc #checking of feature classes
    arcpy.AddField_management(fc, "NDVI", "FLOAT", "9", "6")
    #arcpy.DeleteField_management(fc, "NDVI") 
    expression = "float(!GRIDCODE!) / 1000000.000000"
    arcpy.CalculateField_management(fc, "NDVI", expression, "PYTHON")
print "Finish adding and calculating the field"""

#Adding the municipality to the attribute table
for fc in arcpy.ListFeatureClasses("reclassnofptphil_onlyreprojected*"):
     print fc #checking of feature classes
     outputFeature = "withjoin" + fc # specify output feature
     arcpy.SpatialJoin_analysis(fc, "PHL_adm2_UTM.shp", outputFeature)

print "Finish"
