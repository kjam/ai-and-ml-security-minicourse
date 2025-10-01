main(dataset_name="MNIST", 
     model_name="cleverhans", 
     detection="FeatureSqueezing?squeezers=bit_depth_5,median_filter_2_2&distance_measure=l1&fpr=0.05",
     attacks="FGSM?eps=0.1;BIM?eps=0.1&eps_iter=0.02;JSMA?targeted=next"
     )
