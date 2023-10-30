def define_bee():
    import numpy as np

    # make an empty numpy array for storing the image
    image_mat = np.full((16, 16, 3), 1.0)

    # define some colours
    black = [0, 0, 0]
    yellow = [1.0, 0.85, 0]
    grey = [0.65] * 3
    pink = [1, 0, 1]

    # specify which pixels are which colour
    image_mat[7:11, 2] = yellow #black
    image_mat[6:12, 3:5] = yellow #black
    image_mat[6:12, 5:7] = black #yellow
    image_mat[6:12, 7:9] = yellow #black
    image_mat[6:12, 9:11] = black #yellow
    image_mat[6:12, 11:13] = yellow #black
    image_mat[7:11, 13] = yellow #black
    image_mat[4:6, 5:11] = pink #grey
    image_mat[3, 6:10] = pink #grey
    
    return image_mat


def plot_image(image):
    import matplotlib.pyplot as plt

    plt.axis('off')
    plt.imshow(image)
    plt.show()
    
    
bee = define_bee()
plot_image(bee)
