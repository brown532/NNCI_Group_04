# Rosenblatt Perceptron Training

## Abstract
The Perceptron can be described as the foundation to Artificial Neural Networks as we know it today. It was particularly popular in the 60s when it was proven to always converge to a solution if it exists, for a linearly separable dataset. This project utilizes this convergence characteristic of the Perceptron to describe the relationship between the linear separability of a dichotomy and the ratio ($\alpha$) of the population size to the number of features. It was observed that for $1.0\leq \alpha \leq 3.0$, the probability that a dataset is linearly separable decreases with increasing values of $\alpha$. It was also observed that for a large number of features, this relation became more steep and gets close to a step function as predicted by a theorem. The results also showed that the threshold (c) for label classification by the Perceptron does not truly affect the classification performance of the perceptron. It further showed that using a clamped input for the Perceptron in order to find solutions for inhomogeneous linearly separable datasets slightly improved the chance of successful training by the Perceptron on randomly sampled datasets.

## How to run the experiments
###Make sure you have Python 3.7.6 installed
###python -m pip install --upgrade pip
###pip install -r requirements.txt
###python launchModel.py

## Overview of program files
TBD

## Requirements
TBD 

## Authors
- [brown532](https://github.com/brown532)
- [juanjoguerrero8](https://github.com/juanjoguerrero8)


