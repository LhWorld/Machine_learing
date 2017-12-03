#coding:utf-8
import numpy as np
import PIL.Image as Image
import pickle as p
import  os

class ImageTools(object):

    image_dir='images/'
    data_file_path='data.bin'
    def imageToArray(self,files):
        images=[]
        for i in range(len(files)):
            image=Image.open(ImageTools.image_dir+files[i])
            r,g,b= image.split()
            r_array = np.array(r).reshape(62500)
            g_array = np.array(g).reshape(62500)
            b_array = np.array(b).reshape(62500)
            image_arry = np.concatenate((r_array,g_array,b_array))
            images=np.concatenate((images,image_arry))
        images =np.array(images).reshape((len(files),(3*62500)))
        f =open(ImageTools.data_file_path,'wb')
        p.dump(images,f)
        f.close()
if __name__=="__main__":
    it = ImageTools()
    files= os.listdir(ImageTools.image_dir)
    print(files)
    it.imageToArray(files)