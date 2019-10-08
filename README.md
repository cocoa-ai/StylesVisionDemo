# Styles Vision Demo

A Demo application using `Vision` and `CoreML` frameworks to detect the most
likely style of the given image.

<div align="center">
<img src="https://github.com/cocoa-ai/StylesVisionDemo/blob/master/Screenshot.png" alt="StylesVisionDemo" width="300" height="534" />
</div>

## Model

This demo is based on the "Finetuning CaffeNet on Flickr Style" neural network
classifier, which was converted from original [Caffe model](https://gist.github.com/sergeyk/034c6ac3865563b69e60)
to [CoreML model](https://drive.google.com/file/d/0B1ghKa_MYL6maFFWR3drLUFNQ1E/view?usp=sharing)
using [coremltools](https://pypi.python.org/pypi/coremltools) python package.

## Requirements

- Xcode 9
- iOS 11

## Installation

```sh
git clone https://github.com/cocoa-ai/StylesVisionDemo.git
cd StylesVisionDemo
pod install
open Styles.xcworkspace/
```

Download the [CoreMl model](https://drive.google.com/file/d/1aF-3p8zyrTzFE1tPpdBgLeWa0kanCN--/view?usp=sharing)
and add the file to "Resources" folder in the project's directory.

Build the project and run it on a simulator or a device with iOS 11.

## Conversion

```sh
cd Convert
./download.sh
python convert.py
```

## Author

Vadym Markov, markov.vadym@gmail.com

## Credits

Original "Finetuning CaffeNet on Flickr Style" [Caffe model](https://gist.github.com/sergeyk/034c6ac3865563b69e60)

## References
- [Caffe Model Zoo](https://github.com/caffe2/caffe2/wiki/Model-Zoo)
- [Apple Machine Learning](https://developer.apple.com/machine-learning/)
- [Vision Framework](https://developer.apple.com/documentation/vision)
- [CoreML Framework](https://developer.apple.com/documentation/coreml)
- [coremltools](https://pypi.python.org/pypi/coremltools)
