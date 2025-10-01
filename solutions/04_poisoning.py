print('Original poisoning attempt moved spam {}'.format(
    top_poisoned_spam[0][0] - top_spam[0][0]))

X_poisoned = spam_model.steps[0][1].transform(
    [x[0] for x in my_poisoned_data] * 10000)
y_poisoned = [x[1] for x in my_poisoned_data] * 10000
spam_model.steps[1][1].partial_fit(X_poisoned, y_poisoned)
feature_names = spam_model.steps[0][1].get_feature_names()
top_repoisoned_spam = sorted(zip(spam_model.steps[1][1].coef_[0],
                       feature_names), reverse=True)[:10]

free_index = spam_model.steps[0][1].get_feature_names().index('free')
free_coeff = spam_model.steps[1][1].coef_[0][free_index]
print('Second poisoning attempt moved spam {}'.format(
    free_coeff - top_spam[0][0]))
