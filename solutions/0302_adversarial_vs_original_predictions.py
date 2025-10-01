adv_preds = kmodel.predict(adv_x)
print('Adversarial predictions:')
for pred in decode_predictions(adv_preds, top=10)[0]:
    print(pred)

orig_preds = kmodel.predict(img_x)
print('Original predictions:')
for pred in decode_predictions(orig_preds, top=10)[0]:
    print(pred)
