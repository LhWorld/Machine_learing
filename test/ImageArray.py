#coding:utf-8
import numpy as np
import PIL.Image as Image
import pickle as p
import  os

class ImageTools(object):

    image_dir='images/'
    result_dir='results/'
    data_file_path='data.bin'
    def imageToArray(self,files):
        images=[]
        for i in range(len(files)):
            image=Image.open(ImageTools.image_dir+files[i])
            r,g,b= image.split()
            r_array = np.array(r).reshape(62500)
            g_array = np.array(g).reshape(62500)
            b_array = np.array(b).reshape(62500)
            image_arry = np.concatenate((r_array,g_array,b_array)) #按照行打开文件
            images=np.concatenate((images,image_arry)) #组合在一起 行拼接
        print(images.shape)
        images =np.array(images).reshape((len(files),(3*62500))) # 列拼接
        print(images.shape)
        f =open(ImageTools.data_file_path,'wb')
        p.dump(images,f)
        f.close()

    def readToImage(self,file):
        f = open(file,'rb')
        arr = p.load(f) # 30行，187500列
        rows = arr.shape[0]

        new_arr =arr.reshape((rows,3,250,250)) # 把矩阵变成一个高维矩阵

        for i in range(rows):
            r =Image.fromarray(new_arr[i][0]).convert("L") #把每个图片中RGB通道分离
            g =Image.fromarray(new_arr[i][1]).convert("L") #把每个图片中RGB通道分离
            b =Image.fromarray(new_arr[i][2]).convert("L") #把每个图片中RGB通道分离

            image = Image.merge("RGB",(r,g,b)); # 合并RGB通道获得一张图片
            # f =open(ImageTools.result_dir+str(i)+'.png','wb')
            image.save(ImageTools.result_dir+str(i)+'.png',"png")
if __name__=="__main__":
    it = ImageTools()
    files= os.listdir(ImageTools.image_dir)
    # it.imageToArray(files)
    it.readToImage('data.bin')