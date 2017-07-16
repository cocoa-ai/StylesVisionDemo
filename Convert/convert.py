import coremltools

coreml_model = coremltools.converters.caffe.convert(('finetune_flickr_style.caffemodel', 'deploy.prototxt'), image_input_names = 'data', class_labels = 'styles.txt')
coreml_model.author = 'Sergey Karayev'
coreml_model.license = 'Unknown'
coreml_model.short_description = 'Finetuning CaffeNet on Flickr Style'
coreml_model.input_description['data'] = 'An image.'
coreml_model.output_description['prob'] = 'The probabilities for each style type, for the given input.'
coreml_model.output_description['classLabel'] = 'The most likely style of image, for the given input.'
coreml_model.save('FlickrStyle.mlmodel')
