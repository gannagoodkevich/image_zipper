import random
from PIL import Image, ImageDraw
import os

my_image = Image.open('img1.png')
my_image = my_image.convert("RGB")
width = my_image.size[0]
height = my_image.size[1]
pixel_matrix = my_image.load()

for i in range(width):
	for j in range(height):
		a = str((2*pixel_matrix[i, j][0]/255)-1)
		b = str((2*pixel_matrix[i, j][1]/255)-1)
		c = str((2*pixel_matrix[i, j][2]/255)-1)
		#print(a, b, c, end = "|")
	#print("---")
print(str(width))
print(str(height))

A = [ [1, 2, 3, 4, 5, 111],
[6, 7, 8, 9, 10, 112],
[11, 12, 13, 14, 15, 113],
[16, 17, 18, 19, 20, 114],
[21, 22, 23, 24, 25, 115]
]
n = 2
m = 3
k1 = n
k0 = 0
l1 = m
l0 = 0
while k1 <= 5:
	while l1 <= 6:
		for i in range(k0, k1):
			for j in range(l0, l1):
				print(A[i][j], end = "|")
		l0 += m
		l1 += m
	l0 = 0
	l1 = m
	k0 += n
	k1 +=n
