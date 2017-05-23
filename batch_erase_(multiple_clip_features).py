import arcpy
from arcpy import env
env.overwriteOutput = True
env.workspace = r"C:\thesis\LATEST\MOD12\Per Region\new lossyear\one_pixel.gdb"

#inputs

list_in_features = ['']


#erase features
list_erase_features =['gdbnewlossyearARMM_forests_onlylossyear_10N_110Eone_pixel','gdbnewlossyearARMM_forests_onlylossyear_10N_120Eone_pixel',
                   'gdbnewlossyearBatanes_forests_onlylossyear_30N_120Eone_pixel','gdbnewlossyearCAR_forests_onlylossyear_20N_120Eone_pixel',
                   'gdbnewlossyearI_forests_onlylossyear_20N_110Eone_pixel','gdbnewlossyearI_forests_onlylossyear_20N_120Eone_pixel',
                   'gdbnewlossyearII_forests_onlylossyear_20N_120Eone_pixel','gdbnewlossyearIII_forests_onlylossyear_20N_120Eone_pixel',
                   'gdbnewlossyearIVA_forests_onlylossyear_20N_120Eone_pixel','gdbnewlossyearIVB_forests_onlylossyear_10N_110Eone_pixel',
                   'gdbnewlossyearIVB_forests_onlylossyear_20N_110Eone_pixel','gdbnewlossyearIVB_forests_onlylossyear_20N_120Eone_pixel',
                   'gdbnewlossyearIX_forests_onlylossyear_10N_120Eone_pixel','gdbnewlossyearNCR_forests_onlylossyear_20N_120Eone_pixel',
                   'gdbnewlossyearV_forests_onlylossyear_20N_120Eone_pixel','gdbnewlossyearVI_forests_onlylossyear_10N_120Eone_pixel',
                   'gdbnewlossyearVI_forests_onlylossyear_20N_120Eone_pixel','gdbnewlossyearVII_forests_onlylossyear_10N_120Eone_pixel',
                   'gdbnewlossyearVII_forests_onlylossyear_20N_120Eone_pixel','gdbnewlossyearVIII_forests_onlylossyear_10N_120Eone_pixel',
                   'gdbnewlossyearVIII_forests_onlylossyear_20N_120Eone_pixel','gdbnewlossyearX_forests_onlylossyear_10N_120Eone_pixel',
                   'gdbnewlossyearXI_forests_onlylossyear_10N_120Eone_pixel','gdbnewlossyearXII_forests_onlylossyear_10N_120Eone_pixel',
                   'gdbnewlossyearXIII_forests_onlylossyear_10N_120Eone_pixel','gdbnewlossyearXIII_forests_onlylossyear_20N_120Eone_pixel']




#output_Folder = r"C:\Users\brentiebark\Documents\Diane Samar and Leyte\Samar\Samar_final.gdb"
for k in range(0,12):
    #print list_erase_features[k]
    p = list_erase_features[k].replace('one_pixel','_final')
    print "Erasing " + p + " portion"
    arcpy.Erase_analysis(Nakar_fc, r"C:\thesis\LATEST\NAMRIA\Per Region\new lossyear\final.gdb\\"+\
                         list_erase_features[k],r"C:\thesis\LATEST\NAMRIA\Per Region\new lossyear\final.gdb\\"+p)

print "Finish!"


