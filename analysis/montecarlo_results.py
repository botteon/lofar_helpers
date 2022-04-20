from glob import glob
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats
from scipy.stats import sem

def uncertainty(d_err):
    unc = 1/np.power(d_err, 2)
    return np.sqrt(1/np.sum(unc))
    # return np.sqrt(np.sum(unc)/(np.sum(unc)**2))

cellsize=27

a399_rudnick = glob(f'../ptp_results_{cellsize}/a399results_rudnick_*.txt')
a401_rudnick = glob(f'../ptp_results_{cellsize}/a401results_rudnick_*.txt')
bridge_rudnick = glob(f'../ptp_results_{cellsize}/bridgeresults_rudnick_*.txt')
a399_cb = glob(f'../ptp_results_{cellsize}/a399results_cb_*.txt')
a401_cb = glob(f'../ptp_results_{cellsize}/a401results_cb_*.txt')
bridge_cb = glob(f'../ptp_results_{cellsize}/bridgeresults_cb_*.txt')

# a399_rudnick = glob(f'../ptp_results/a399results_rudnick_*.txt')
# a399trail_rudnick = glob(f'../ptp_results/a399trailresults_rudnick_*.txt')
# a401_rudnick = glob('../ptp_results/a401results_rudnick_*.txt')
# bridge_rudnick = glob('../ptp_results/bridgeresults_rudnick_*.txt')
# a399_cb = glob('../ptp_results/a399results_cb_*.txt')
# a399trail_cb = glob('../ptp_results/a399trailresults_cb_*.txt')
# a401_cb = glob('../ptp_results/a401results_cb_*.txt')
# bridge_cb = glob('../ptp_results/bridgeresults_cb_*.txt')

a399_results_rudnick, a399_rudnick_err, a399_pearson, a399_pearson_err, a399_spearman, a399_spearman_err = [], [], [], [], [], []
a401_results_rudnick, a401_rudnick_err, a401_pearson, a401_pearson_err, a401_spearman, a401_spearman_err = [], [], [], [], [], []
bridge_results_rudnick, bridge_rudnick_err, bridge_pearson, bridge_pearson_err, bridge_spearman, bridge_spearman_err = [], [], [], [], [], []
a399_results_cb, a399_cb_err, a399_pearson_cb, a399_pearson_cb_err, a399_spearman_cb, a399_spearman_cb_err = [], [], [], [], [], []
a401_results_cb, a401_cb_err, a401_pearson_cb, a401_pearson_cb_err, a401_spearman_cb, a401_spearman_cb_err = [], [], [], [], [], []
bridge_results_cb, bridge_cb_err, bridge_pearson_cb, bridge_pearson_cb_err, bridge_spearman_cb, bridge_spearman_cb_err = [], [], [], [], [], []

for a339 in a399_cb:
    with open(a339) as f:
        lines = f.readlines()
        a399_pearson_cb.append(float(lines[-4].split()[0].replace('(','').replace(',','')))
        a399_pearson_cb_err.append(float(lines[-3].split()[-1]))
        a399_spearman_cb.append(float(lines[-2].split()[0].replace('(','').replace(',','')))
        a399_spearman_cb_err.append(float(lines[-1].split()[-1]))
        a399_results_cb.append(float(lines[3].replace('Linear regression slope is ', '').split()[0]))
        a399_cb_err.append(float(lines[3].replace('Linear regression slope is ', '').split()[-1]))

for a401 in a401_cb:
    with open(a401) as f:
        lines = f.readlines()
        a401_pearson_cb.append(float(lines[-4].split()[0].replace('(','').replace(',','')))
        a401_pearson_cb_err.append(float(lines[-3].split()[-1]))
        a401_spearman_cb.append(float(lines[-2].split()[0].replace('(','').replace(',','')))
        a401_spearman_cb_err.append(float(lines[-1].split()[-1]))
        a401_results_cb.append(float(lines[3].replace('Linear regression slope is ', '').split()[0]))
        a401_cb_err.append(float(lines[3].replace('Linear regression slope is ', '').split()[-1]))


for bridge in bridge_cb:
    with open(bridge) as f:
        lines = f.readlines()
        bridge_pearson_cb.append(float(lines[-4].split()[0].replace('(','').replace(',','')))
        bridge_pearson_cb_err.append(float(lines[-3].split()[-1]))
        bridge_spearman_cb.append(float(lines[-2].split()[0].replace('(','').replace(',','')))
        bridge_spearman_cb_err.append(float(lines[-1].split()[-1]))
        bridge_results_cb.append(float(lines[3].replace('Linear regression slope is ', '').split()[0]))
        bridge_cb_err.append(float(lines[3].replace('Linear regression slope is ', '').split()[-1]))


for a339rudnick in a399_rudnick:
    with open(a339rudnick) as f:
        lines = f.readlines()
        a399_pearson.append(float(lines[-4].split()[0].replace('(','').replace(',','')))
        a399_pearson_err.append(float(lines[-3].split()[-1]))
        a399_spearman.append(float(lines[-2].split()[0].replace('(','').replace(',','')))
        a399_spearman_err.append(float(lines[-1].split()[-1]))
        a399_results_rudnick.append(float(lines[3].replace('Linear regression slope is ', '').split()[0]))
        a399_rudnick_err.append(float(lines[3].replace('Linear regression slope is ', '').split()[-1]))

for a401rudnick in a401_rudnick:
    with open(a401rudnick) as f:
        lines = f.readlines()
        a401_pearson.append(float(lines[-4].split()[0].replace('(','').replace(',','')))
        a401_pearson_err.append(float(lines[-1].split()[-1]))
        a401_spearman.append(float(lines[-2].split()[0].replace('(','').replace(',','')))
        a401_spearman_err.append(float(lines[-1].split()[-1]))
        a401_results_rudnick.append(float(lines[3].replace('Linear regression slope is ', '').split()[0]))
        a401_rudnick_err.append(float(lines[3].replace('Linear regression slope is ', '').split()[-1]))

for bridgerudnick in bridge_rudnick:
    with open(bridgerudnick) as f:
        lines = f.readlines()
        bridge_pearson.append(float(lines[-4].split()[0].replace('(','').replace(',','')))
        bridge_pearson_err.append(float(lines[-1].split()[-1]))
        bridge_spearman.append(float(lines[-2].split()[0].replace('(','').replace(',','')))
        bridge_spearman_err.append(float(lines[-1].split()[-1]))
        bridge_results_rudnick.append(float(lines[3].replace('Linear regression slope is ', '').split()[0]))
        bridge_rudnick_err.append(float(lines[3].replace('Linear regression slope is ', '').split()[-1]))

print('UV-Subtract:')
print(f'Slope A399: {np.sum(np.divide(a399_results_cb, np.power(a399_cb_err, 2)))/np.sum(1/np.power(a399_cb_err,2))} +- '
      f'{sem(a399_results_cb)*np.sqrt(np.sum(np.power(a399_cb_err/np.sum(np.power(a399_cb_err, 2)), 2)))}')
print(f'Pearson R A399: {np.mean(a399_pearson_cb)} +- {sem(a399_pearson_cb)}')
print(f'Spearman R A399: {np.mean(a399_spearman_cb)} +- {sem(a399_spearman_cb)}')

print(f'Slope A401: {np.sum(np.divide(a401_results_cb, np.power(a401_cb_err, 2)))/np.sum(1/np.power(a401_cb_err,2))} +- '
      f'{sem(a401_results_cb)*np.sqrt(np.sum(np.power(a401_cb_err/np.sum(np.power(a401_cb_err, 2)), 2)))}')
print(f'Pearson R A401: {np.mean(a401_pearson_cb)} +- {sem(a401_pearson_cb)}')
print(f'Spearman R A401: {np.mean(a401_spearman_cb)} +- {sem(a401_spearman_cb)}')

print(f'Slope Bridge: {np.sum(np.divide(bridge_results_cb, np.power(bridge_cb_err, 2)))/np.sum(1/np.power(bridge_cb_err,2))} +- '
      f'{sem(bridge_results_cb)*np.sqrt(np.sum(np.power(bridge_cb_err/np.sum(np.power(bridge_cb_err, 2)), 2)))}')
print(f'Pearson R bridge: {np.mean(bridge_pearson_cb)} +- {sem(bridge_pearson_cb)}')
print(f'Spearman R bridge: {np.mean(bridge_spearman_cb)} +- {sem(bridge_spearman_cb)}')

print('\nRudnick:')
print(f'Slope A399: {np.sum(np.divide(a399_results_rudnick, np.power(a399_rudnick_err, 2)))/np.sum(1/np.power(a399_rudnick_err,2))} +- '
      f'{sem(a399_results_rudnick)*np.sqrt(np.sum(np.power(a399_rudnick_err/np.sum(np.power(a399_rudnick_err, 2)), 2)))}')
print(f'Pearson R A399: {np.mean(a399_pearson)} +- {sem(a399_pearson)}')
print(f'Spearman R A399: {np.mean(a399_spearman)} +- {sem(a399_spearman)}')

print(f'Slope A401: {np.sum(np.divide(a401_results_rudnick, np.power(a401_rudnick_err, 2)))/np.sum(1/np.power(a401_rudnick_err,2))} +- '
      f'{sem(a401_results_rudnick)*np.sqrt(np.sum(np.power(a401_rudnick_err/np.sum(np.power(a401_rudnick_err, 2)), 2)))}')
print(f'Pearson R A401: {np.mean(a401_pearson)} +- {sem(a401_pearson)}')
print(f'Spearman R A401: {np.mean(a401_spearman)} +- {sem(a401_spearman)}')

print(f'Slope bridge: {np.sum(np.divide(bridge_results_rudnick, np.power(bridge_rudnick_err, 2)))/np.sum(1/np.power(bridge_rudnick_err,2))} +- {sem(bridge_results_rudnick)*np.sqrt(np.sum(np.power(bridge_rudnick_err/np.sum(np.power(bridge_rudnick_err, 2)), 2)))}')
print(f'Pearson R bridge: {np.mean(bridge_pearson)} +- {sem(bridge_pearson)}')
print(f'Spearman R bridge: {np.mean(bridge_spearman)} +- {sem(bridge_spearman)}')

print('\nTotal:')
a399_tot = a399_results_rudnick+a399_results_cb
a399_err = a399_rudnick_err+a399_cb_err
a399_pearson_tot = a399_pearson+a399_pearson_cb
a399_pearson_err = a399_pearson_err + a399_pearson_cb_err
a399_spearman_tot = a399_spearman+a399_spearman_cb
a399_spearman_err = a399_spearman_err + a399_spearman_cb_err
print(f'Slope A399: {np.sum(np.divide(a399_tot, np.power(a399_err, 2)))/np.sum(1/np.power(a399_err,2))} +- '
      f'{uncertainty(a399_err)}')
print(f'Pearson R A399: {np.sum(np.divide(a399_pearson_tot, np.power(a399_pearson_err, 2)))/np.sum(1/np.power(a399_pearson_err,2))} +- '
      f'{uncertainty(a399_pearson_err)}')
print(f'Spearman R A399: {np.sum(np.divide(a399_spearman_tot, np.power(a399_spearman_err, 2)))/np.sum(1/np.power(a399_spearman_err,2))} +- '
      f'{uncertainty(a399_spearman_err)}')


a401_tot = a401_results_rudnick+a401_results_cb
a401_err = a401_rudnick_err+a401_cb_err
a401_pearson_tot = a401_pearson+a401_pearson_cb
a401_pearson_err = a401_pearson_err + a401_pearson_cb_err
a401_spearman_tot = a401_spearman+a401_spearman_cb
a401_spearman_err = a401_spearman_err + a401_spearman_cb_err
print(f'Slope 401: {np.sum(np.divide(a401_tot, np.power(a401_err, 2)))/np.sum(1/np.power(a401_err,2))} +- '
      f'{uncertainty(a401_err)}')
print(f'Pearson R A401: {np.sum(np.divide(a401_pearson_tot, np.power(a401_pearson_err, 2)))/np.sum(1/np.power(a401_pearson_err,2))} +- '
      f'{uncertainty(a401_pearson_err)}')
print(f'Spearman R A401: {np.sum(np.divide(a401_spearman_tot, np.power(a401_spearman_err, 2)))/np.sum(1/np.power(a401_spearman_err,2))} +- '
      f'{uncertainty(a401_spearman_err)}')

bridge_tot = bridge_results_rudnick+bridge_results_cb
bridge_err = bridge_rudnick_err+bridge_cb_err
bridge_pearson_tot = bridge_pearson+bridge_pearson_cb
bridge_pearson_err = bridge_pearson_err + bridge_pearson_cb_err
bridge_spearman_tot = bridge_spearman+bridge_spearman_cb
bridge_spearman_err = bridge_spearman_err + bridge_spearman_cb_err
print(f'Slope bridge: {np.sum(np.divide(bridge_tot, np.power(bridge_err, 2)))/np.sum(1/np.power(bridge_err,2))} +- '
      f'{uncertainty(bridge_err)}')
print(f'Pearson R Bridge: {np.sum(np.divide(bridge_pearson_tot, np.power(bridge_pearson_err, 2)))/np.sum(1/np.power(bridge_pearson_err,2))} +- '
      f'{uncertainty(bridge_pearson_err)}')
print(f'Spearman R Bridge: {np.sum(np.divide(bridge_spearman_tot, np.power(bridge_spearman_err, 2)))/np.sum(1/np.power(bridge_spearman_err,2))} +- '
      f'{uncertainty(bridge_spearman_err)}')


# print(scipy.stats.normaltest(bridge_results_cb))
# plt.hist(bridge_results_rudnick)
# plt.hist(bridge_results_cb)
# plt.show()