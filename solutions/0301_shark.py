%matplotlib inline

img_path = 'data/img/shark.jpg'
img = load_img(img_path, target_size=(224, 224))

x = img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input(x)

preds = kmodel.predict(x)

for pred in decode_predictions(preds, top=3)[0]:
    print(pred)

plt.imshow(img)
plt.axis('off')
