-: DOCUMENTATION by PANKAJ KUMAR:- 

During making this project, I followed all the instructions very carefully.
I executed, trained this model multiple times, and noticed below specified things:

I started with a baseline equal to the Neural Network used in the lecture to classify
MNIST images:
- epochs: 15
- img(width,height): 30x30
- num_categories: 43
- test_size: 0.4
AND 
- 1 conv layer with 32, 3x3 filters,
- 1 pooling layer with 2x2 pool size,
- 1 hidden layer with 128 neurons, activation function(ReLU) and 0.5 dropout
- optimizer: adam
- loss: categorical_crossentrophy
- metrics: accuracy

and from there, I varied one parameter at a time to see its influence in
accuracy.

*At the very beginning, I got 94.93% accuray.
![output1](https://github.com/gumsum-kaur/pk-cs50ai/assets/54205121/2bcdb131-cb67-45da-bf4a-37b964bfd9cf)



*2nd time, I've changed only dropout to 0.1, and got 95.16% accuray at this (1 conv layer with 32, 3x3 filters, 1 Dense Layer and epochs 15).
![output2](https://github.com/gumsum-kaur/pk-cs50ai/assets/54205121/ea3b9e09-db70-4a7c-8471-a8d67c7566bb)


3rd time, I've used:
- 1 conv layer with 32 filters, and 3x3 kernel,
- MaxPooling 2x2
- 3 hidden layers of 128 neurons each,
- dropout 0.1,
- and epochs 15
So at this phase, I got 96.71% accuray.
![output3](https://github.com/gumsum-kaur/pk-cs50ai/assets/54205121/5a90b09a-46dd-450e-8df7-7ea2fd6cf879)


*4th time, I've just decresed the training times i.e., epochs value to 10. So, at the below specifications:

- 1 conv layer with 32 filters, and 3x3 kernel,
- MaxPooling 2x2
- 3 hidden layers of 128 neurons each,
- dropout 0.1,
- and epochs 10

I got 94.78% accuray.
![output4](https://github.com/gumsum-kaur/pk-cs50ai/assets/54205121/79ec01b5-fd36-4bb6-8982-39d14c0bb85d)



So, the best combinations of parameters I found resulted in an testing accuracy of 96.71% at (1 conv layer with 32 filters, and 3x3 kernel, MaxPooling 2x2, 3 hidden layers of 128 neurons each, dropout 0.1, and epochs 15).

So, the winning architecture is:
- 1 conv layer with 32 3x3 filters,
- 1 pooling layer with 2x2 pool size,
- 3 hidden layers with 128 neurons each
- 0.1 dropout and epochs 15.

Afterwards, I searched for inspiration in famous ConvNet architectures.
I interweaved convolutional and pooling layers with different parameters,
but best I found was 96.71% accuray at this combination (1 conv layer with 32, 3x3 filters, 3 Dense Layers, 0.1 dropout and epochs 15) for this dataset.
