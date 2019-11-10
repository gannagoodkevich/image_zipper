import numpy as np
import cv2
import time

N = 2
M = 2
P = 6
ERROR = 0.00145

img_path = "img.jpg"
train_example = cv2.imread(img_path)
IMAGE_SIZE = (256, 256)
train_example = cv2.resize(train_example, IMAGE_SIZE)

cv2.imwrite("img2.jpg", train_example)
print(train_example.size)
print(train_example.shape)

matrix = np.array(train_example)
matrix = ((matrix / 0.5) / 255) - 1

W1 = np.random.uniform(-0.5, 0.5, (N * M * 3, P))
W2 = W1.transpose()

current_error = 10000
step = 0
A = 0.01
start_time = time.time()
while current_error > ERROR:
    current_error = 0
    for i in range(int(IMAGE_SIZE[0] / N)):
        for j in range(int(IMAGE_SIZE[1] / M)):
            X1 = matrix[(i * N):(i * N + N), (j * M):(j * M + M)]
            X1 = np.reshape(X1, (1, M * N * 3))
            Y1 = X1.dot(W1)

            X2 = Y1.dot(W2)

            dX = X2 - X1
            oldW2 = W2.copy()
            W2 = W2 - (A * Y1.transpose()).dot(dX)
            W1 = W1 - (A * X1.transpose()).dot(dX).dot(oldW2.transpose())
            err = np.sum(dX * dX) / (M * N * 3)
            current_error = current_error + err
    current_error = current_error / ((IMAGE_SIZE[0] / N) * (IMAGE_SIZE[1] / M))
    print("step #" + str(step))
    print("current error = " + str(current_error))
    step = step + 1

output_matrix = None
np.save("W1.npy", W1)
np.save("W2.npy", W2)

for i in range(int(IMAGE_SIZE[0] / N)):
    row = None
    zip_row = None
    for j in range(int(IMAGE_SIZE[1] / M)):
        X1 = matrix[(i * N):(i * N + N), (j * M):(j * M + M)]
        X1 = np.reshape(X1, (1, M * N * 3))

        Y1 = X1.dot(W1)

        X2 = Y1.dot(W2)

        X2 = np.reshape(X2, (N, M, 3))
        X2 = X2.swapaxes(0, 1)
        X2 = ((X2 + 1) / (1 / 255)) / 2

        if row is None:
            row = X2
        else:
            row = np.vstack((row, X2))
    if output_matrix is None:
        output_matrix = row
    else:
        output_matrix = np.hstack((output_matrix, row))
end_time = time.time()
print("time:", end_time - start_time)
output_matrix = output_matrix.transpose(1, 0, 2)
cv2.imwrite("mrz1/result.jpg", output_matrix)
