import cv2
import numpy as np
from sklearn.cluster import KMeans

################ code from https://www.timpoulsen.com/2018/finding-the-dominant-colors-of-an-image.html

def make_histogram(cluster):
    """
    Count the number of pixels in each cluster
    :param: KMeans cluster
    :return: numpy histogram
    """
    numLabels = np.arange(0, len(np.unique(cluster.labels_)) + 1)
    hist, _ = np.histogram(cluster.labels_, bins=numLabels)
    hist = hist.astype('float32')
    hist /= hist.sum()
    return hist


def make_bar(height, width, color):
    """
    Create an image of a given color
    :param: height of the image
    :param: width of the image
    :param: BGR pixel values of the color
    :return: tuple of bar, rgb values, and hsv values
    """
    bar = np.zeros((height, width, 3), np.uint8)
    bar[:] = color
    red, green, blue = int(color[2]), int(color[1]), int(color[0])
    hsv_bar = cv2.cvtColor(bar, cv2.COLOR_BGR2HSV)
    hue, sat, val = hsv_bar[0][0]
    return bar, (red, green, blue), (hue, sat, val)


def sort_hsvs(hsv_list):
    """
    Sort the list of HSV values
    :param hsv_list: List of HSV tuples
    :return: List of indexes, sorted by hue, then saturation, then value
    """
    bars_with_indexes = []
    for index, hsv_val in enumerate(hsv_list):
        bars_with_indexes.append((index, hsv_val[0], hsv_val[1], hsv_val[2]))
    bars_with_indexes.sort(key=lambda elem: (elem[1], elem[2], elem[3]))
    return [item[0] for item in bars_with_indexes]

################

def getImagePartition(image, height, width, size):
    y = size*height
    x = size*width
    return image[y:y+size, x:x+size].copy()

def getMostDominantColor(image):
    height, width, _ = np.shape(image)
    image = image.reshape((height * width, 3))
    num_clusters = 5
    clusters = KMeans(n_clusters=num_clusters)
    clusters.fit(image)
    histogram = make_histogram(clusters)
    combined = zip(histogram, clusters.cluster_centers_)
    combined = sorted(combined, key=lambda x: x[0], reverse=True)
    return [int(combined[0][1][0]), int(combined[0][1][1]), int(combined[0][1][2])]

def appendPixelToImage(newImage, mdc, row, col, sizePerPixel):
    x = col*sizePerPixel
    y = row*sizePerPixel
    for r in range(sizePerPixel):
        for c in range(sizePerPixel):
            if((y+r)<len(newImage) and (x+c)<len(newImage[0])):
                newImage[y+r][x+c] = mdc

################

if __name__ == "__main__":
    imageLocation = input("Enter location of image with its name as a relative path (for example ./image.png): ")
    sizePerPixel = int(input("Enter size of each pixel (for example if 32 is entered each 32x32 pixels will be converted into 1 pixel): "))

    image = cv2.imread(imageLocation)

    widthPartitions = int(image.shape[1]/sizePerPixel)
    heightPartitions = int(image.shape[0]/sizePerPixel)
    newImage = [[[0,0,0] for j in range(image.shape[0])] for x in range(image.shape[1])]

    for r in range(heightPartitions):
        for c in range(widthPartitions):
            partition = getImagePartition(image, r, c, sizePerPixel)
            # cv2.imshow('partition '+str(r)+"x"+str(c), partition)
            mdc = getMostDominantColor(partition)
            appendPixelToImage(newImage, mdc, r, c, sizePerPixel)

    newImage = np.array(newImage, dtype=np.uint8)
    print(newImage)
    cv2.imshow('originalImage', image)
    cv2.imshow('sprite', newImage)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
