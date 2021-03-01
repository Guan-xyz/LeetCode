# 832. Flipping an Image


def flip_and_invert_image(image):
    reversed = [i[::-1] for i in image]
    for j in reversed:
        for k in range(len(j)):
            j[k] = j[k] ^ 1
    return reversed
