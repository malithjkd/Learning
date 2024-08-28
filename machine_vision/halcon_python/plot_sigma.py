# python enviroment - "py11"

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Data_Y
data_Y = [516.7556016, 516.7386053, 516.7521835, 516.7264784, 516.7399818, 516.7232673, 516.7562577, 516.7434614, 516.7518168, 516.7188187, 516.7539228, 516.7516242, 516.7172544, 516.7116481, 516.7136885, 516.7180437, 516.7149152, 516.7155336, 516.7232375, 516.7380444, 516.7243552, 516.6879626, 516.7033876, 516.691008, 516.7533984, 516.7245683, 516.6979367, 516.7375984, 516.7195944, 516.719896, 516.730174, 516.7165799, 516.7296039, 516.7106525, 516.6864467, 516.7197492, 516.7161831, 516.731653, 516.7329572, 516.7223411, 516.717324, 516.708951, 516.747219, 516.724902, 516.7482094, 516.7395387, 516.7183157, 516.7028094, 516.7372642, 516.7651386, 516.7402451, 516.7228782, 516.7531009, 516.7643251, 516.7402655, 516.7218122, 516.7303592, 516.777221, 516.7389227, 516.7463595, 516.7280458, 516.7244626, 516.755712, 516.7488733, 516.7348042]
# Data_X
data_X = [626.4601085,626.4658575,626.4704845,626.4525167,626.4509151,626.446974,626.4450056,626.4308697,626.4554132,626.4551456,626.4481521,626.4463754,626.464103,626.4473866,626.4740703,626.473025,626.4869319,626.4897143,626.4735664,626.4790575,626.4979005,626.5005408,626.4966385,626.5051917,626.4631342,626.4731155,626.4904101,626.4982454,626.4719056,626.4999646,626.4896128,626.4711774,626.4812092,626.4776677,626.519637,626.493747,626.494573,626.4557043,626.4916098,626.4761756,626.4972961,626.450799,626.471327,626.4720284,626.4568243,626.4704725,626.4491289,626.4844264,626.4666268,626.4687948,626.4773811,626.4886209,626.4658382,626.4707141,626.4890602,626.4735587,626.4447496,626.45231,626.4684224,626.4329067,626.4524481,626.4953845,626.4897307,626.5000388,626.4811499]

# shift data to zero location
# Data_Y
data =[0.025486357,0.008490103,0.022068234,-0.003636807,0.009866537,-0.006847926,0.026142484,0.013346217,0.021701535,-0.011296533,0.023807529,0.021508938,-0.012860865,-0.018467151,-0.016426744,-0.012071557,-0.015200038,-0.01458159,-0.006877774,0.007929197,-0.005760071,-0.042152645,-0.026727615,-0.039107267,0.023283214,-0.005546948,-0.032178515,0.007483176,-0.010520844,-0.010219239,5.87349E-05,-0.0135353,-0.000511344,-0.019462777,-0.043668577,-0.01036607,-0.01393209,0.001537768,0.002842011,-0.007774161,-0.012791259,-0.021164199,0.017103732,-0.00521323,0.018094138,0.009423489,-0.01179954,-0.027305866,0.007148929,0.035023341,0.010129878,-0.007236989,0.022985713,0.034209822,0.010150306,-0.008303017,0.000244017,0.047105804,0.008807454,0.016244237,-0.002069478,-0.005652624,0.025596729,0.018758046,0.004688984]
# Data_X
data_X_shift =[-0.012720284,-0.006971346,-0.002344324,-0.020312134,-0.021913739,-0.025854767,-0.027823221,-0.041959064,-0.017415579,-0.017683201,-0.024676748,-0.026453412,-0.008725789,-0.02544216,0.001241531,0.000196218,0.014103122,0.016885464,0.000737597,0.006228727,0.025071736,0.027711988,0.023809741,0.032362945,-0.009694553,0.000286671,0.017581252,0.025416613,-0.000923162,0.027135781,0.016784006,-0.001651373,0.008380436,0.004838863,0.046808156,0.020918246,0.021744166,-0.017124487,0.018781047,0.003346788,0.024467324,-0.022029843,-0.001501767,-0.000800441,-0.016004526,-0.002356338,-0.023699903,0.01159765,-0.006201969,-0.00403397,0.004552297,0.015792052,-0.006990569,-0.002114666,0.01623141,0.000729864,-0.028079156,-0.020518775,-0.004406381,-0.039922057,-0.020380693,0.022555654,0.016901938,0.027210026,0.008321087]



data_np = np.array(data)
zeros= np.zeros(data_np.shape[0])

# Calculate mean and standard deviation
mean = np.mean(data)
std_dev = np.std(data)

# Create the histogram
plt.hist(data, bins=30, density=False, alpha=0.6, color='g')

# Plot the PDF
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, mean, std_dev)
plt.plot(x, p/3, 'k', linewidth=1)

# Mark sigma values
plt.axvline(x=mean-std_dev, color='r', linestyle='--', label='-1σ')
plt.axvline(x=mean+std_dev, color='r', linestyle='--', label='+1σ')
plt.axvline(x=mean-2*std_dev, color='b', linestyle='--', label='-2σ')
plt.axvline(x=mean+2*std_dev, color='b', linestyle='--', label='+2σ')
plt.axvline(x=mean-3*std_dev, color='g', linestyle='--', label='-3σ')
plt.axvline(x=mean+3*std_dev, color='g', linestyle='--', label='+3σ')
plt.axvline(x=np.min(data), color='k',linestyle='--', label='Minimum')
plt.axvline(x=np.max(data), color='k',linestyle='--', label='Maximum')
plt.scatter(data[:],zeros[:], color='r',marker='.' )

plt.xlabel('Y aixs position value (µm)')
plt.ylabel('Occurrence')
plt.title('Histogram of Y axis variation with Normal Curve and Sigma Values')
plt.legend()
plt.show()
