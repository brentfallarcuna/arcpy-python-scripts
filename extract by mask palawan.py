import arcpy
from arcpy import env
from arcpy.sa import *
arcpy.CheckOutExtension("Spatial")
env.overwriteOutput = True

#Set the current workspace
env.workspace = (r"C:\thesis\LATEST\Overlay Agreements\5_over_5\Per Province\Palawan")
env.nodata = "MINIMUM"
env.compression = "LZ77"

#see if the shp files are there
#for shp in  arcpy.ListFeatureClasses():
    #print  shp

"""list_10_110 = ['Balabac.shp','Bataraza.shp','Rizal.shp','Brooke.shp','Sofronio Espanola.shp','Quezon.shp','Narra.shp','Aborlan.shp','Puerto Princesa City.shp']
#This is for extracting the forest areas of hansen percent treecover
#loop the list
for i in list_10_110:
    print "Extracting " + i + " in 10_110"
    env.workspace = (r"C:\thesis\LATEST\Overlay Agreements\5_over_5\Per Province\Palawan")
    for raster in arcpy.ListRasters("*10N_110E.tif", "TIF"):
        env.workspace = (r"C:\thesis\LATEST\Overlay Agreements\5_over_5\Per Province\Palawan")
        print "    extracting " + raster #checking the presence of raster
        outputRasterExtractbyMask = ExtractByMask(raster, i)
        prov=i.replace(".shp", "_")
        outputRasterExtractbyMask_Name = prov + raster
        env.workspace = (r"C:\thesis\LATEST\Overlay Agreements\5_over_5\Per Province\Palawan\10N_110E")
        outputRasterExtractbyMask.save(outputRasterExtractbyMask_Name)


list_10_120 = ['Puerto Princesa City.shp','San Vicente.shp','Roxas.shp','Taytay.shp','Dumaran.shp','Araceli.shp',
                    'Linapacan.shp','Culion.shp','Busuanga.shp','El Nido.shp']
#This is for extracting the forest areas of hansen percent treecover
#loop the list
for k in list_10_120:
    print "Extracting " + k + " in 20_110"
    env.workspace = (r"C:\thesis\LATEST\Overlay Agreements\5_over_5\Per Province\Palawan")
    for raster in arcpy.ListRasters("*20N_110E.tif", "TIF"):
        env.workspace = (r"C:\thesis\LATEST\Overlay Agreements\5_over_5\Per Province\Palawan")
        print "    extracting " + raster #checking the presence of raster
        outputRasterExtractbyMask = ExtractByMask(raster, k)
        prov=k.replace(".shp", "_")
        outputRasterExtractbyMask_Name = prov + raster
        env.workspace = (r"C:\thesis\LATEST\Overlay Agreements\5_over_5\Per Province\Palawan\20N_110E")
        outputRasterExtractbyMask.save(outputRasterExtractbyMask_Name)"""

list_20_110 = ['Coron.shp','Cuyo.shp','Magsaysay.shp','Agutaya.shp']
#This is for extracting the forest areas of hansen percent treecover
#loop the list
for d in list_20_110:
    print "Extracting " + d + " in 20_110"
    env.workspace = (r"C:\thesis\LATEST\Overlay Agreements\5_over_5\Per Province\Palawan")
    for raster in arcpy.ListRasters("*20N_120E.tif", "TIF"):
        env.workspace = (r"C:\thesis\LATEST\Overlay Agreements\5_over_5\Per Province\Palawan")
        print "    extracting " + raster #checking the presence of raster
        outputRasterExtractbyMask = ExtractByMask(raster, d)
        prov=d.replace(".shp", "_")
        outputRasterExtractbyMask_Name = prov + raster
        env.workspace = (r"C:\thesis\LATEST\Overlay Agreements\5_over_5\Per Province\Palawan\20N_110E")
        outputRasterExtractbyMask.save(outputRasterExtractbyMask_Name)

"""list_20_120 =['Abra.shp','Apayao.shp','Benguet.shp','Ifugao.shp','Kalinga.shp',\
               'Mountain Province.shp','Ilocos Norte.shp','Ilocos Sur.shp','La Union.shp','Pangasinan.shp',\
               'Cagayan.shp','Isabela.shp','Nueva Vizcaya.shp','Quirino.shp','Aurora.shp',\
               'Bataan.shp','Bulacan.shp','Nueva Ecija.shp','Pampanga.shp','Tarlac.shp','Zambales.shp',\
               'Batangas.shp','Cavite.shp','Laguna.shp','Quezon.shp','Rizal.shp','Marinduque.shp','Occidental Mindoro.shp',\
               'Oriental Mindoro.shp','Palawan.shp','Romblon.shp','NCR.shp','Albay.shp','Camarines Norte.shp',\
               'Camarines Sur.shp','Catanduanes.shp','Masbate.shp','Sorsogon.shp','Aklan.shp','Antique.shp','Capiz.shp',\
               'Guimaras.shp','Iloilo.shp','Negros Occidental.shp','Bohol.shp','Cebu.shp','Negros Oriental.shp','Biliran.shp',\
               'Eastern Samar.shp','Leyte.shp','Northern Samar.shp','Samar.shp','Southern Leyte.shp','Dinagat Islands.shp',\
               'Surigao del Norte.shp']
#This is for extracting the forest areas of hansen percent treecover
#loop the list
for y in list_20_120:
    print "Extracting " + y + " in 20_120"
    env.workspace = (r"C:\thesis\LATEST\Overlay Agreements\5_over_5\Per Province\Palawane")
    for raster in arcpy.ListRasters("*20N_120E.tif", "TIF"):
        env.workspace = (r"C:\thesis\LATEST\Overlay Agreements\5_over_5\Per Province\Palawane")
        print "    extracting " + raster #checking the presence of raster
        outputRasterExtractbyMask = ExtractByMask(raster, y)
        prov=y.replace(".shp", "_")
        outputRasterExtractbyMask_Name = prov + raster
        env.workspace = (r"C:\thesis\LATEST\Overlay Agreements\5_over_5\Per Province\Palawane\Broadleaf Open Canopy")
        outputRasterExtractbyMask.save(outputRasterExtractbyMask_Name)

env.workspace = (r"C:\thesis\LATEST\Overlay Agreements\5_over_5\Per Province\Palawane")
print "Extracting Batanes in 30_120"
for raster in arcpy.ListRasters("*30N_120E.tif", "TIF"):
    print "Extracting Batanes"
    env.workspace = (r"C:\thesis\LATEST\Overlay Agreements\5_over_5\Per Province\Palawane")
    print raster #checking the presence of raster
    g = "Batanes.shp"
    outputRasterExtractbyMask = ExtractByMask(raster, g)
    prov = g.replace(".shp", "_")
    outputRasterExtractbyMask_Name = prov + raster
    env.workspace = (r"C:\thesis\LATEST\Overlay Agreements\5_over_5\Per Province\Palawane\Broadleaf Open Canopy")
    outputRasterExtractbyMask.save(outputRasterExtractbyMask_Name)"""

print "Finish"
