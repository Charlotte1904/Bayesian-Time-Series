# Bayesian-Time-Series

Using Bayesian Inference on Time Series Data

Bayes' Theorem 

![logo](image/bayes.png, width = 50)

- The method was invented in the 18th century by an English Presbyterian minister named Thomas Bayes — by some accounts to calculate the probability of God’s existence. 

# Objective 

The goal of this repo is to summarize the idea of Frequentist and Bayesian. Bayesian Inference is proven to be powerful in terms of optimization and sampling method. However, it is still not very popular on day-to-day business analytics. I include three different examples using Bayes Inference to analyze enrollment rate, conversion rate, crime rate and taxi pick up rate. We can use Bayesian Inference to do Bayesian A/B Testing and to calculate the best whatever rate by incorporating historical data to the most recent values. Bayesian method weighted for the most recent data and helps to balance out odd days that have extremely low or high values or/and have inconsistent pattern with the rest of the dataset. 

1. Udacity A/B Testing

2. Crime Rate in San Francisco groupby date and neighborhood

3. Taxi Pick up in New York groupby date and taxi company


# Frequentist vs Bayesian 

- In Frequentist statistics, we assume the parameter(s) of interest are fixed constants. We focus on computing the likelihood Prob(Data | Parameter), the probability we see the observed set of data points given the parameter of interest.


- In Bayesian statistics, we having uncertainty surrounding our parameter(s) of interest, and we mathematically capture our priori uncertainty about these parameters in a prior distribution, formally represented as Prob(Parameter). We focus on computing the posterior distribution Prob(Parameter | Data), representing our posteriori uncertainty surrounding the parameter of interest after we have observed data.

  -  Null Hypothesis :  no significant difference

  - p-value : probability that the null hypothesis is correct

  - Confidence Interval : “if we would have repeated this test many times, and would have calculated a different confidence interval for each case, then in 95% of the times the actual conversion rate would fall within this interval.”

# Why Bayes Rules ?

•	Time: weighted on recency - the most recent values will be weighted more

•   Smoothing effect - balance out rare events - events that have unexpected high numbers

•	Prior belief - incorporate knowledge domain or expertise 

•	Attitudes toward risk - have probability for every statement/decision

For Bayesians, probabilities are fundamentally related to their knowledge about an event. This means, for example, that in a Bayesian view, we can meaningfully talk about the probability that the true conversion rate lies in a given range, and that probability codifies our knowledge of the value based on prior information and/or available data.


# False Positive Rate

- Testing at alpha = 0.05 means your statistical test yielding a result as extreme or more extreme by random chance (assuming a given null hypothesis is true) occurs with probability 0.05. 

- If you run 26 statistical tests, then an upper bound on the expected number of false positives is 26*0.05 = 1.3.

 This means in our above scenario, our data scientist can expect to have at least one false positive result, and unfortunately, the false positive result is the one she reported to her boss.


# Interpretability 


 So instead of saying “we could not reject the null hypothesis that the conversion rate of A is equal to that of B with a p-value of 0.102,” we can state “there is a 89.1% chance that the conversion rate of A is better than B.”

In this example this means that this client has a 10.9% chance of losing money (around 200 thousand) when they implement the variation, but also a 89.1% chance that it will increase revenue (of around 660 thousand). Probably every manager would like these odds and implement the variation.
