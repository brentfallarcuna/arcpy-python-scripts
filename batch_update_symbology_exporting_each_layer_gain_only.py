 #import the module
import arcpy
import arcpy.mapping as mapping
from arcpy import env
env.overwriteOutput = True

#set the workspace
arcpy.env.workspace = (r"C:\Users\brentiebark\Dropbox\Thesis Results\New Results\Zamboanga tiffs")

#set the map document python_NDVI_2.mxd
mxd = mapping.MapDocument(r"C:\thesis\gain.mxd")

#set the data frame (only one data frame!)
df = mapping.ListDataFrames(mxd)[0]

#set the basis for the layer legend
basisLayer = mapping.Layer(r"C:\thesis\hansenwipfiles\GAIN.lyr")
#print the year 200 text element 
print mapping.ListLayoutElements(mxd, "TEXT_ELEMENT")[10].text

#listing the names of all the text elements
#for ms in mapping.ListLayoutElements(mxd, "TEXT_ELEMENT"):
        #print ms.name

#loop update the symbology!
for layer in mapping.ListLayers(mxd):
        mapping.UpdateLayer(df, layer, basisLayer)
        layer.visible = True
        print "Processing "+layer.name
        #for element in mapping.ListLayoutElements(mxd, "TEXT_ELEMENT"):
        mapping.ListLayoutElements(mxd, "TEXT_ELEMENT")[10].text = layer.name
        mapping.ListLayoutElements(mxd, "TEXT_ELEMENT")[10].elementPositionX = 0.70
        mapping.ListLayoutElements(mxd, "TEXT_ELEMENT")[10].elementPositionY = 9.9505
        arcpy.mapping.ExportToPNG(mxd, r"C:\thesis\Zambo tiffs\Latest\\" + layer.name  + "Agusan del Sur" + ".png","PAGE_LAYOUT", resolution = 400)  
        layer.visible = False

#mapping.ExportToJPEG(mxd, r"C:\Users\Windows\Documents\JO_GIS_Analyst\Brent.jpg", "PAGE_LAYOUT", resolution = 150)
#listing the Layout Elements
#for elm in mapping.ListLayoutElements(mxd): 
#refreshing, saving & deleting mxd
#arcpy.RefreshTOC()
#mxd.save()
del mxd
print "Finish!"


