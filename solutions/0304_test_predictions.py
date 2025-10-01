## See predictions
for img in advs_images:
    img = np.expand_dims(img[0].numpy().copy(), axis=0)
    img = preprocess_input(img)

    adv_preds = kmodel.predict(img)
    print('Adversarial predictions:')
    for pred in decode_predictions(adv_preds, top=3)[0]:
        print(pred)
