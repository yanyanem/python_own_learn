'''

book 机器学习系统设计 

page P155 第十章 计算机视觉：模式识别

code 代码部分

date 2017/03/09

copy sj 

'''


import mahotas as mh
from matplotlib import pyplot as plt
import numpy as np

sj_face="mu_tou.jpg"
#sj_face="head-s2-0.jpg"
#sj_face="img_2955.jpg"
#image=mh.imread("syx_face.png")

image=mh.imread(sj_face)


plt.subplot(241)
plt.imshow(image)

image1=image-image.mean()
plt.subplot(242)
plt.imshow(image1)


image_gray=mh.colors.rgb2gray(image,dtype=np.uint8)
plt.subplot(243)
plt.gray()
plt.imshow(image_gray)


thresh=mh.thresholding.otsu(image_gray)
print(thresh)
plt.subplot(244)
image1=image_gray>thresh
plt.imshow(image1)


otsubin = (image_gray>thresh)
outsubin = mh.open(otsubin, np.ones((2,2)))
plt.subplot(245)
plt.imshow (outsubin)

otsubin = (image_gray<=thresh)
outsubin = mh.close(otsubin, np.ones((2,2)))
plt.subplot(246)
plt.imshow (outsubin)

'''
thresh=mh.thresholding.rc(image_gray)
print(thresh)
plt.subplot(247)
image1=image_gray>thresh
plt.imshow(image1)
'''

image_gray=mh.colors.rgb2gray(image)
im8=mh.gaussian_filter(image_gray,8)
plt.subplot(247)
plt.imshow(im8)



#im8=im8.astype(int)
#thresh=mh.thresholding.otsu(im8)
print(thresh)
plt.subplot(248)
image1=im8>thresh
plt.imshow(image1)

plt.show()

print("----------------------------------------------------------------")

image=mh.imread(sj_face,as_grey=True)

plt.subplot(141)
plt.imshow(image)


salt=np.random.random(image.shape) > .975
pepper=np.random.random(image.shape) > .975
image1=mh.stretch(image)
image1=np.maximum(salt*170,image1)
image1=np.minimum(pepper*30+image*(~pepper),image1)
plt.subplot(142)
plt.imshow(image1)

image=mh.imread(sj_face)
r,g,b=image.transpose(2,0,1)
r12=mh.gaussian_filter(r,12.)
g12=mh.gaussian_filter(g,12.)
b12=mh.gaussian_filter(b,12.)
im12=mh.as_rgb(r12,g12,b12)
h,w=r.shape
Y,X=np.mgrid[:h,:w]
Y=Y-h/2.
Y=Y/Y.max()
X=X-w/2.
X=X/X.max()
W=np.exp(-2.*(X**2+Y**2))
W=W-W.min()
W=W/W.ptp()
W=W[:,:,None]
ringed=mh.stretch(image*W+(1-W)*im12)
plt.subplot(143)
plt.imshow(ringed)


image=mh.imread(sj_face,as_grey=True)
filtered=mh.sobel(image,just_filter=True)
plt.subplot(144)
plt.imshow(filtered)

plt.show()

# P168 不是很理解这个怎么用 
from mahotas.features import surf
image=mh.imread(sj_face,as_grey=True)
descriptors=surf.surf(image,descriptor_only=True)
descriptors=surf.dense(image,spacing=16)



