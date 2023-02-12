from PIL import Image
import matplotlib.pylab as plt


img = Image.open('work_blossom.jpg')
plt.imshow(img)
plt.show()
small_img=img.resize((8,8),Image.BILINEAR)

#resize
o_size=(1000,1000) #output size
res=small_img.resize(o_size,Image.NEAREST)
#save image
res.save('mario_8x8.png')
#display image
plt.imshow(res)
plt.show()












