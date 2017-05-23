 #import the module
import arcpy
import arcpy.mapping as mapping
from arcpy import env
env.overwriteOutput = True


#set the workspace
arcpy.env.workspace = "C:\Users\Windows\Documents\JO_GIS_Analyst"

#set the map document python_NDVI_2.mxd
mxd = mapping.MapDocument(r"C:\Users\Windows\Documents\JO_GIS_Analyst\python_NDVI_2.mxd")

#set the data frame (only one data frame!)
df = mapping.ListDataFrames(mxd)[0]

#set the basis for the layer legend
basisLayer = mapping.Layer(r"C:\Users\Windows\Documents\JO_GIS_Analyst\NDVI_ColorTable.lyr")
#print mapping.ListLayoutElements(mxd, "TEXT_ELEMENT")[27].text

#loop update the symbology!
for layer in mapping.ListLayers(mxd):
        #mapping.UpdateLayer(df, layer, basisLayer)
        layer.visible = True
        #print layer.name[0:25]
        #for element in mapping.ListLayoutElements(mxd, "TEXT_ELEMENT"):
        mapping.ListLayoutElements(mxd, "TEXT_ELEMENT")[27].text = layer.name
        mapping.ListLayoutElements(mxd, "TEXT_ELEMENT")[27].elementPositionX = 0.90
        mapping.ListLayoutElements(mxd, "TEXT_ELEMENT")[27].elementPositionY = 21.3
        mapping.ExportToJPEG(mxd, r"C:\Users\Windows\Documents\JO_GIS_Analyst\\" + layer.name + ".jpg", "PAGE_LAYOUT", resolution = 150)  
        layer.visible = False

#mapping.ExportToJPEG(mxd, r"C:\Users\Windows\Documents\JO_GIS_Analyst\Brent.jpg", "PAGE_LAYOUT", resolution = 150)
#listing the Layout Elements
#for elm in mapping.ListLayoutElements(mxd): 
#refreshing, saving & deleting mxd
#arcpy.RefreshTOC()
#mxd.save()
del mxd
print "Finish!"


        
        
        
        
        
        




