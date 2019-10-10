import random
from PIL import Image, ImageDraw
import os

my_image = Image.open('img1.png')
my_image = my_image.convert("RGB")
width = my_image.size[0]
height = my_image.size[1]
print("Hello World")
pixel_matrix = my_image.load()
open('log.txt', 'w').close()
f= open("log.txt","w+")
res = [[[0 for k in range(3)] for j in range(width)] for i in range(height)]
f.write("Hello")
for i in range(width):
	for j in range(height):
		a = (2*pixel_matrix[i, j][0]/255)-1
		b = (2*pixel_matrix[i, j][1]/255)-1
		c = (2*pixel_matrix[i, j][2]/255)-1
		res[i][j][0] = a
		res[i][j][1] = b
		res[i][j][2] = c
		#print(a, b, c, end = "|")
		f.write(str(a) + "|")
		f.write(str(b) + "|")
		f.write(str(c) + "|")
	f.write("\n---\n")
print("Hello")
vect = []
vect.append([1, 2, 3])
print(vect[0][2])
#A = [ [1, 2, 3, 4, 5, 111],
#[6, 7, 8, 9, 10, 112],
#[11, 12, 13, 14, 15, 113],
#[16, 17, 18, 19, 20, 114],
#[21, 22, 23, 24, 25, 115],
#[26, 27, 28, 29, 30, 116]
#]
f.write("\n-----||-----\n")
f.close
open('log1.txt', 'w').close()
f= open("log1.txt","w+")
n = 8
m = 16
k1 = n
k0 = 0
l1 = m
l0 = 0
vectors = []
pix = []
while k1 <= height:
	while l1 <= width:
		for i in range(k0, k1):
			for j in range(l0, l1):
				pix.append(res[i][j][0])
				pix.append(res[i][j][1])
				pix.append(res[i][j][2])
				f.write(str(res[i][j][0]) + ", " + str(res[i][j][1]) + ", " + str(res[i][j][0]) + ", ")
		#f.write(vectors[a])
		vectors.append(pix)
		f.write("\n\n-----\n\n")
		pix = []
		l0 += m
		l1 += m
	l0 = 0
	l1 = m
	k0 += n
	k1 +=n
if(height % n != 0):
	print ("Yepn")
	l1 = m
	l0 = 0
	while l1 <= width:
		for i in range(height-n, height):
			for j in range(l0, l1):
				pix.append(res[i][j][0])
				pix.append(res[i][j][1])
				pix.append(res[i][j][2])
				f.write(str(res[i][j][0]) + ", " + str(res[i][j][1]) + ", " + str(res[i][j][0]) + ", ")
		#f.write(vectors[a])
		vectors.append(pix)
		f.write("\n\n-----\n\n")
		pix = []
		l0 += m
		l1 += m
if(width % m != 0):
	print ("Yepm")
	k1 = n
	k0 = 0
	while k1 <=height:
		for i in range(k0, k1):
			for j in range(width-m, width):
				pix.append(res[i][j][0])
				pix.append(res[i][j][1])
				pix.append(res[i][j][2])
				f.write(str(res[i][j][0]) + ", " + str(res[i][j][1]) + ", " + str(res[i][j][0]) + ", ")
		#f.write(vectors[a])
		vectors.append(pix)
		f.write("\n\n-----\n\n")
		pix = []
		k0 += n
		k1 +=n
print(len(vectors))
