from scipy.stats import beta
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
def plot_with_fill(x, y, label):
    #x: probability/rate
    #y: probability density function
    lines = plt.plot(x, y, label=label, lw=2)
    plt.fill_between(x, 0, y, alpha=0.2, color=lines[0].get_c())

def posterior_distribution(control_alpha,control_beta,experiment_alpha, experiment_beta):
    #x: probability/rate
    #y: probability density function
    #updating posterior distribution
    i = 0
    if i != len(control):
        c_pos_alpha, c_posterior_beta = control_alpha[i] + control_alpha[i+1], control_beta[i] + control_beta[i+1]
        e_pos_alpha, e_posterior_beta = experiment_alpha[i] + experiment_alpha[i+1], experiment_beta[i] + experiment_beta[i+1]
        i+=1
    return c_pos_alpha,c_posterior_beta,e_pos_alpha,e_posterior_beta
 
x = x = np.linspace(0., 1, 1000) #random probability
