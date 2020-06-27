<h1 align="center">Human/Cat face classifier</h1>

## Introduction
Classifier is an app that download images to your local machine and then classify them.
Classification based in Human/Cat faces.
with an efficient processing power with GPU you can train your haarcascade_*.xml to achieve better results.  

## content
download a collection of images, then uses opencv library for classification.
<p align="center"><img src="https://github.com/virtualio/classifier/blob/master/img/img10.jpg" width="400" height="400"></p>
in this example you can see that with my cpu proessing power I couldn't achieve good results for object detection.

## minimal requirement
- 64-bit Processor
- tensorflow

## framework
- [OpenCV](https://opencv.org/)

## Future TODO
classifier written in the flow, with no much efforts for modular programming. the idea was just to show "done better than nothing"
* there are two options to take this project to the next level:
- option one: using Beautifulsoup library to download images from wider range of domains.
- option two: since a video is a set of images it is possible to do live classification for videos (while loop)
              an object could be human walking, distance between two moving objects, face emotions, etc ..
              for this there is a need for extra deep lerning libraries/frameworks such as:
              [TensorFlow](https://www.tensorflow.org/) and [Keras](https://keras.io/)
              
* it would be great to install the software in a rasberry pi for a demo.
              
