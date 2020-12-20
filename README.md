# Rosenblatt Perceptron Training

## Abstract
The Perceptron can be described as the foundation to Artificial Neural Networks as we know it today. It was particularly popular in the 60s when it was proven to always converge to a solution if it exists, for a linearly separable dataset. This project utilizes this convergence characteristic of the Perceptron to describe the relationship between the linear separability of a dichotomy and the ratio (<img src="https://render.githubusercontent.com/render/math?math=\alpha">) of the population size to the number of features. It was observed that for <img src="https://render.githubusercontent.com/render/math?math=1.0\leq \alpha \leq 3.0">, the probability that a dataset is linearly separable decreases with increasing values of <img src="https://render.githubusercontent.com/render/math?math=\alpha">. It was also observed that for a large number of features, this relation became more steep and gets close to a step function as predicted by a theorem. The results also showed that the threshold c for label classification by the Perceptron does not truly affect the classification performance of the perceptron. It further showed that using a clamped input for the Perceptron in order to find solutions for inhomogeneous linearly separable datasets slightly improved the chance of successful training by the Perceptron on randomly sampled datasets.

## How to run the experiments
- Make sure you have Python 3.7.6 installed
- `python -m pip install --upgrade pip`
- `pip install -r requirements.txt`
- `python Qls_Pls.py`
- `python different_N.py`
- `python different_c.py`
- `python homogeneous.py`


## Parameter Description
<img src="https://render.githubusercontent.com/render/math?math=Q_{ls}\implies"> Fraction of successful runs<br/>
<img src="https://render.githubusercontent.com/render/math?math=P_{ls}\implies"> Probability that a dichotomy is linearly separable<br/>
<img src="https://render.githubusercontent.com/render/math?math=n_D\implies"> Number of random populations used to calculate fraction of successful runs<br/>
<img src="https://render.githubusercontent.com/render/math?math=P\implies"> Population size<br/>
<img src="https://render.githubusercontent.com/render/math?math=N\implies"> Size of feature vector<br/>
<img src="https://render.githubusercontent.com/render/math?math=n_{max}\implies">Maximum number of epochs for the Perceptron to find a solution<br/>
<img src="https://render.githubusercontent.com/render/math?math=\alpha\implies"> P/N<br/>
<img src="https://render.githubusercontent.com/render/math?math=c\implies"> Classification threshold (default: > 0)
## Experiment Description
- **Experiment 1**: Comparison of <img src="https://render.githubusercontent.com/render/math?math=Q_{ls}"> and <img src="https://render.githubusercontent.com/render/math?math=P_{ls}">
	This experiment compares the fraction of successful runs of the Perceptron with the probability that a dichotomy is linearly separable.<br/>
Parameters: <img src="https://render.githubusercontent.com/render/math?math=0.75\leq\alpha\leq3.0,N=20,n_D=50,n_{max}=100"><br/>
source file: `Qls_Pls.py`

- **Experiment 2**:  Comparison of  different values of N
This experiment compares the effects that different values of N have on <img src="https://render.githubusercontent.com/render/math?math=Q_{ls}">.<br/>
Parameters: $0.75\leq\alpha\leq3.0,N=[20,100,200], n_D=50,n_{max}=100$<br/>
source file: `different_N.py`

- **Experiment 3**: Comparison of different values of c
This experiment compares the effects that different values of c have on <img src="https://render.githubusercontent.com/render/math?math=Q_{ls}">.<br/>
Parameters: <img src="https://render.githubusercontent.com/render/math?math=0.75\leq\alpha\leq3.0,N=20, c=[default, 0.05, 0.1,0.2], n_D=500,n_{max}=100"><br/>
source file: `different_c.py`

- **Experiment 4**: Effect of using a clamped input for the Perceptron
This experiment observes the effects that adding a clamped input (-1) for the Perceptron on the success of the training. It compares this technique to the default used in previous experiments which can not find solutions to inhomogeneous linearly separable dichotomies.<br/>
Parameters: <img src="https://render.githubusercontent.com/render/math?math=0.75\leq\alpha\leq3.0,N=20, n_D=500,n_{max}=100"><br/>
source file: `homogeneous.py`

## Results
**Experiment 1**
<img src="results/PlsQls.png" width="400" >
**Experiment 2**
<img src="results/differentN.png" width="400" >
**Experiment 3**
<img src="results/different_c.png" width="400" >
**Experiment 4**
<img src="results/homogeneous.png" width="400" >


## Authors
- [Brown Ogum](https://github.com/brown532)
- [Juanjo Guerrero](https://github.com/juanjoguerrero8)


