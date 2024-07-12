# FriendsDontLetFriendsPython
Friends don't let friends make certain types of data visualization - What are they and why are they bad.

This project is motivated by the popular data visualization do's and don't. I decided to create my own version in python, for two reasons. First, it allows me practice my python skills and two allows me reiterate the data visualization problems that can occur when good practices are not adhered to.

To see the original Friend don't let Friends
Reference [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.7542491.svg)](https://doi.org/10.5281/zenodo.7542491)

The `Scripts/` directory contains `.Python` files that generate the graphics shown below. 

Requirements
* Python
* Pandas
* Scipy
* Matplotlib 


# Table of Contents
## 1. Friends don't let Friends Make Bar Plots for Means Separation <a name = "Means seperation">

This has to be the first one. 
Means separation plots are some of the most common in scientific publications. 
We have two or more groups, which contains multiple observations; they may have different means, variances, and distributions. 
The task of the visualization is to show the means and the spread (dispersion) of the data. 

![No Bar Plots for Means Separation](https://github.com/tobbyxy/FriendsDontLetFriendsPython/tree/main/Figures/mean_seperation.png) 

In this example, two groups have similar means and standard deviations, but quite different distributions. **Are they really "the same"?**
Just don't use bar plot for means separation, or at least check a couple things before settling down on a bar plot. 



2. Friends don't let Friends
3. Friends don't let Friends