# neural-network
Everything related to the neural networks I really need to explore

To test **Fifa/nn.py** with predefined weights and bias - type:
```
python3 nn.py '[0.7367558056631766, 0.45169329115720835]' 13.96682537688979
```

I actually worked out the derivatives for *Gradient Descent* myself so the formulas might sometimes occur invalid.  

**fifa/nn.py** is a single (hidden) layer Neural Network.  
 
For activation function I used *ReLU* so for some random weights a restart will be needed as the net will most likely overshoot the minima.  
Error function is a simple as possible. *Squared loss function* was applied.  
  
Same was put into **sumation/nn.py**. The goal of this NN is to predict the sum of two values.  
