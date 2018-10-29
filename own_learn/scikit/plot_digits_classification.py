"""
================================
Recognizing hand-written digits
================================

An example showing how the scikit-learn can be used to recognize images of
hand-written digits.

This example is commented in the
:ref:`tutorial section of the user manual <introduction>`.

"""
print(__doc__)

# Author: Gael Varoquaux <gael dot varoquaux at normalesup dot org>
# License: BSD 3 clause

# Standard scientific Python imports
import matplotlib.pyplot as plt

# Import datasets, classifiers and performance metrics
from sklearn import datasets, svm, metrics

# The digits dataset
digits = datasets.load_digits()

print("digits=",len(digits));
print("digits.images=",len(digits.images));
print("digits.target=",len(digits.target));

# The data that we are interested in is made of 8x8 images of digits, let's
# have a look at the first 4 images, stored in the `images` attribute of the
# dataset.  If we were working from image files, we could load them using
# matplotlib.pyplot.imread.  Note that each image must have the same size. For these
# images, we know which digit they represent: it is given in the 'target' of
# the dataset.
images_and_labels = list(zip(digits.images, digits.target))

print("images_and_labels[:4]=",images_and_labels[:4]);

for index, (image, label) in enumerate(images_and_labels[:4]):
    plt.subplot(3, 4, index + 1)
    plt.axis('off')
    plt.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
    plt.title('Training: %i' % label)

#plt.show()

for index, (image, label) in enumerate(images_and_labels[4:8]):
    plt.subplot(3, 4, index + 5)
    plt.axis('off')
    plt.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
    plt.title('Training: %i' % label)

#plt.show()

# To apply a classifier on this data, we need to flatten the image, to
# turn the data in a (samples, feature) matrix:
n_samples = len(digits.images)

data = digits.images.reshape((n_samples, -1))
print("len(data)=",len(data))
print("data[:1]=",data[:1])


# Create a classifier: a support vector classifier
classifier = svm.SVC(gamma=0.001)




print(":n_samples-",n_samples)
# We learn the digits on the first half of the digits
classifier.fit(data[: int(n_samples / 2)], digits.target[: int(n_samples / 2)])
print("digits.target[: int(n_samples / 2)]=",digits.target[int(n_samples / 2-1): int(n_samples / 2)])

# Now predict the value of the digit on the second half:

expected = digits.target[int(n_samples / 2):]
predicted = classifier.predict(data[int(n_samples / 2):])
#expected = digits.target[:int(n_samples / 2)]
#predicted = classifier.predict(data[:int(n_samples / 2)])
print("predicted=",predicted)

print("Classification report for classifier %s:\n%s\n"
      % (classifier, metrics.classification_report(expected, predicted)))
print("Confusion matrix:\n%s" % metrics.confusion_matrix(expected, predicted))

images_and_predictions = list(zip(digits.images[int(n_samples / 2):], predicted))
for index, (image, prediction) in enumerate(images_and_predictions[:4]):
    plt.subplot(3, 4, index + 9)
    plt.axis('off')
    plt.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
    plt.title('Prediction: %i' % prediction)

plt.show()

import pickle

s = pickle.dump(classifier,open('data.pkl', 'wb'))
print("s=",s)
clf = pickle.load(open('data.pkl','rb'))
print("clf=",clf)

dataNew=data[2:3]

predictedNew = clf.predict(dataNew)
print("predictedNew=",predictedNew) 

