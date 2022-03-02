import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as sc
def hyp_test(population_mean, sample_mean, sample_std, sample_size, tail_flag, alpha=0.05):
    '''
    Function arguments: alpha-Provide the significance level(By Default it takes 0.05, only takes 0.1, 0.09, 0.08, 0.07, 0.06, 0.04, 0.03, 0.02)
                        population_mean-Provide the mean value of the population(Mandatory)
                        sample_mean-Provide the mean value of the sample(Mandatory)
                        sample_std-Provide the standard deviation of the sample(Mandatory)
                        sample_size-Provide the sample size(Mandatory)
                        tail_flag-Provide 1 for upper-tailed test, 2 for lower-tailed test and 3 for two-tailed test
    '''
    z = {'0.05': 1.68, '0.025': 1.95, '0.02': 2.05, '0.015': 2.17, '0.01': 2.32, '0.03': 1.88, '0.035': 1.81, '0.04': 1.75, '0.045': 1.69}
    try:
        z_stats = (sample_mean-population_mean) / (sample_std/(sample_size**0.5))
    except:
        print("Enter correct value of sample size")
        print("The value provided for sample size is 0 Proceeding calculation with sample size 2")
        z_stats = (sample_mean-population_mean) / (sample_std/(2**0.5))
    mu = 0
    sigma = 1 ** 0.5
    x = np.linspace(mu - 4*sigma, mu + 4*sigma, 100)
    if int(tail_flag) == 1 and alpha in [0.1, 0.09, 0.08, 0.07, 0.06, 0.05, 0.04, 0.03, 0.02]:
        if z_stats >= z[str(alpha)]:
            print("This is a Z-distribution")
            print("Null Hypothesis is rejected")
        else:
            print("This is a Z-distribution")
            print("Null Hypothesis accepted")
        plt.plot(x, sc.norm.pdf(x, mu, sigma))
        plt.axvline(x = z[str(alpha)], color = 'r', label = 'z-alpha')
        plt.axvline(x = z_stats, color='g', label='z-stat')
        plt.legend()
        plt.show()
    elif int(tail_flag) == 2 and alpha in [0.1, 0.09, 0.08, 0.07, 0.06, 0.05, 0.04, 0.03, 0.02]:
        if z_stats <= -z[str(alpha)]:
            print("This is a Z-distribution")
            print("Null Hypothesis is rejected")
        else:
            print("This is a Z-distribution")
            print("Null Hypothesis accepted")
        plt.plot(x, sc.norm.pdf(x, mu, sigma))
        plt.axvline(x = -z[str(alpha)], color = 'r', label = 'z-alpha')
        plt.axvline(x = z_stats, color='g', label='z-stat')
        plt.legend()
        plt.show()
    elif int(tail_flag) == 3:
        if (z_stats >= z[str(alpha/2)]) or (z_stats <= -z[str(alpha/2)]) and alpha in [0.1, 0.09, 0.08, 0.07, 0.06, 0.05, 0.04, 0.03, 0.02]:
            print("This is a Z-distribution")
            print("Null Hypothesis is rejected")
        else:
            print("This is a Z-distribution")
            print("Null Hypothesis accepted")
        plt.plot(x, sc.norm.pdf(x, mu, sigma))
        plt.axvline(x = z[str(alpha/2)], color = 'r', label = 'z-alpha')
        plt.axvline(x = -z[str(alpha/2)], color = 'r')
        plt.axvline(x = z_stats, color='g', label='z-stat')
        plt.legend()
        plt.show()
# sample function call with arguments
# hyp_test(12, 13.25, 3.2, 40, 1)
# hyp_test(6, 6.1, 0.2, 30, 3)