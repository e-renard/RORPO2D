#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 1/12/16
# Odyssee Merveille

from PIL import Image
import numpy
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from skimage.filters import threshold_otsu


def plot_vector_field(vx, vy, vecColor = 'red', scaleSize = 20, image = numpy.array(())):

	fig = plt.figure()
	ax = fig.add_subplot(111)

	dimY, dimX = vx.shape
    
	# vector and support
	mx=numpy.array(())
	my=numpy.array(())

	px=numpy.array(())
	py=numpy.array(())

	#plt.ion()
	# create vectors for plotting
	for i in range(dimY):
		for j in range(dimX):

			if vx[i,j] != 0  or vy[i,j] != 0 :
				mx = numpy.append(mx,j)
				my = numpy.append(my,i)
				px = numpy.append(px,vx[i,j])
				py = numpy.append(py,vy[i,j])
    
	if image.size !=0: 
		ax.imshow(image, cmap='gray')
		ax.quiver(mx, my, px, py, scale = 20, color = vecColor, pivot='middle')

	else:
		ax.quiver(mx, -my, px, py, scale = 20, color = vecColor, pivot='middle')
	
	ax.axis('off')
	fig.savefig('plot.png')
	
	
def plot_RORPO_directional_feature_with_gt(imageName, rorpoIntensityName, rorpoDirectionVxName, rorpoDirectionVyName , gtName):
	
	''' Plot directional feature of the provided synthetic image'''
	image = Image.open(imageName)
	image = numpy.asarray(image)
	
	rorpo = Image.open(rorpoIntensityName)
	rorpo = numpy.asarray(rorpo)
	
	mask = Image.open(gtName)
	mask = numpy.asarray(mask).astype(int)
	mask = (mask>10).astype(int)
	print(numpy.unique(mask))

	vx = Image.open(rorpoDirectionVxName)
	vx = numpy.asarray(vx)

	vy = Image.open(rorpoDirectionVyName)
	vy = numpy.asarray(vy)

	vx = vx.astype(numpy.float)
	vy = vy.astype(numpy.float)

	vx /= 100.0
	vy /= 100.0

	vx -= 1
	vy -= 1

	vx = vx * mask
	vy = vy * mask
		
	plot_vector_field(vx, vy, 'red', 15, image)
	
	
def plot_RORPO_directional_feature(imageName, rorpoIntensityName, rorpoDirectionVxName, rorpoDirectionVyName , thresh = -1):
	
	''' Plot directional feature of the provided synthetic image'''
	image = Image.open(imageName)
	image = numpy.asarray(image)
	

	rorpo = Image.open(rorpoIntensityName)
	rorpo = numpy.asarray(rorpo)

	if thresh <= 0:
		thresh = threshold_otsu(rorpo)
		print("Computed threshold for the RORPO intensity feature: %i" %thresh)
		
	mask = (rorpo>thresh).astype(int)


	vx = Image.open(rorpoDirectionVxName)
	vx = numpy.asarray(vx)

	vy = Image.open(rorpoDirectionVyName)
	vy = numpy.asarray(vy)

	vx = vx.astype(numpy.float)
	vy = vy.astype(numpy.float)

	vx /= 100.0
	vy /= 100.0

	vx -= 1
	vy -= 1

	vx = vx * mask
	vy = vy * mask
		
	plot_vector_field(vx, vy, 'red', 15, image)

if __name__ == '__main__':
	
	#~ imageName = "./images/synthetic_image.png"
	#~ rorpoIntensityName = "./results/synthetic_image_RORPO_30_1_1_1.png"
	#~ rorpoDirectionVxName = "./results/synthetic_image_RORPO_30_1_1_1_vx.png"
	#~ rorpoDirectionVyName = "./results/synthetic_image_RORPO_30_1_1_1_vy.png"
	
	#~ imageName = "./images/cracks_image.png"
	#~ gtName = "./images/cracks_image_gt.png"
	#~ rorpoIntensityName = "./results/cracks_image_RORPO_10_1_1_1.png"
	#~ rorpoDirectionVxName = "./results/cracks_image_RORPO_10_1_1_1_vx.png"
	#~ rorpoDirectionVyName = "./results/cracks_image_RORPO_10_1_1_1_vy.png"
	
	imageName = "./images/retinal_image.png"
	rorpoIntensityName = "./results/retinal_image_RORPO_25_1.5_2_1.png"
	rorpoDirectionVxName = "./results/retinal_image_RORPO_25_1.5_2_1_vx.png"
	rorpoDirectionVyName = "./results/retinal_image_RORPO_25_1.5_2_1_vy.png"

	plot_RORPO_directional_feature(imageName, rorpoIntensityName, rorpoDirectionVxName, rorpoDirectionVyName)

