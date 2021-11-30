import os
import numpy as np
import matplotlib.pyplot as plt
import gzip

with gzip.open('C:\\Users\\esteb\\Downloads\\generated_images.gz', 'rb') as f:
    imgs = f.read()

with open('C:\\Users\\esteb\\Downloads\\generated_images.npy', 'wb') as f:
    f.write(imgs)

imgs = np.load('C:\\Users\\esteb\\Downloads\\generated_images.npy')

imgs_per_epoch = 10
epochs = 50

fig = plt.figure()

rows = 2
cols = 5

fig.add_subplot(rows, cols, 1)

img = []

for i in range(0, imgs.shape[0], imgs_per_epoch):
    for x in range(imgs_per_epoch):
        im = imgs[i+x]
        if len(img) < imgs_per_epoch:
            fig.add_subplot(rows, cols, x+1)
            plt.axis('off')
            img.append(plt.imshow(im, cmap='gray'))
        else:
            img[x].set_data(im)
    plt.pause(0.1)
    plt.draw()