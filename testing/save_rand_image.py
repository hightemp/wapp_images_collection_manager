from randimage import get_random_image, show_array
import matplotlib

img_size = (128,128)

for i in range(1, 50):
    img = get_random_image(img_size)
    matplotlib.image.imsave(f"../static/uploads/image_{i}.png", img)

