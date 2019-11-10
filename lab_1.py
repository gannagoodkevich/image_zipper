import numpy as np
import random
from PIL import Image, ImageDraw
import os


my_image = Image.open('img.png')
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
n = 64
m = 64
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
num_of_neir = 20
max_err = 0.1*num_of_neir
err = 200
teach = 0.005
w1 = np.random.rand(3*n*m, num_of_neir)*2-1
print(w1)
w2 = w1.transpose()
vect = np.array(vectors[0])
print(len(vect))
aaa = []
y_arr = np.zeros(aaa)
#print(y)
print(len(vectors))
a = 0
#vect = vect.transpose()
while err > max_err:
	for i in range(len(vectors)):
		print("ITERATION " + str(a))
		a+=1
		vect = np.array(vectors[i])
		#print(vect)
		#print(w1)
		y = np.dot(vect, w1)
		x = np.dot(y, w2)
		#print(len(x))
		delta_x = x - vect
		#print(len(delta_x.transpose()))
		w1 = w1 - teach  * np.dot(np.dot( vect.transpose(), delta_x), w2.transpose())
		w2 = w2 - teach * np.dot( y.transpose(), delta_x)
		#print("-- Y --")
		#print(y)
		#print("-- X --")
		#print(x)
		sum_err = 0
		err = 0
		teach = 0.01
		for j in range(len(vectors)):
			for i in range(3*n*m):
				sum_err += delta_x[i] * delta_x[i]
			err += sum_err
		print(err)
		#print("--DELTA--")
		#print(delta_x)
		print (np.dot(delta_x, delta_x))
