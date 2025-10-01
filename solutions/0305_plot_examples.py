## Plot images
plt.figure()

plt.subplot(1, 3, 1)
plt.title('Original')
ex_img = example_image[0].numpy() / 255
plt.imshow(ex_img)
# division by 255 to convert [0, 255] to [0, 1]
plt.axis('off')

plt.subplot(1, 3, 2)
plt.title('Adversarial')
adversarial_image = advs_images[1].numpy()[0] / 255
plt.imshow(adversarial_image)
plt.axis('off')

plt.subplot(1, 3, 3)
plt.title('Difference')
difference = adversarial_image - example_image[0]
plt.imshow(difference.numpy() / abs(difference.numpy()).max() * 0.2 + 0.5)
plt.axis('off')

plt.show()
