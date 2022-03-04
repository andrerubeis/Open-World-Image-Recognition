import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
import numpy as np

def average_list_rounded(list1, list2, list3):
    l = [np.round((a + b +c )/3, 3) for a,b,c in zip(list1, list2, list3)]
    return l
def average_dict_rounded(dict1, dict2, dict3):
    d = {}
    for k, _ in dict1.items():
        d[k] = [np.round((a + b +c )/3, 3) for a,b,c in zip(dict1[k], dict2[k], dict3[k])]
    return d
# bic_24 = [0.832, 0.738, 0.6463333333333333, 0.608, 0.5534, 0.5058333333333334, 0.4562857142857143, 0.424375, 0.3788888888888889, 0.3641]
# bic_42 = [0.816, 0.7395, 0.6903333333333334, 0.62175, 0.5552, 0.5108333333333334, 0.45685714285714285, 0.431875, 0.39544444444444443, 0.3628]
#
# l = [np.round((a + b)/2, 3) for a,b in zip(bic_24, bic_42)]
# print(l)
# 1) Closed world without rejection accuracy
icarl_24 = [0.864, 0.746, 0.6593333333333333, 0.60275, 0.5598]
icarl_42 = [0.839, 0.738, 0.6946666666666667, 0.6345, 0.573]
icarl_1993 = [0.801, 0.752, 0.6913333333333334, 0.63825, 0.565]

bic_24 = [0.811, 0.734, 0.634, 0.5885, 0.5272]
bic_42 = [0.812, 0.7395, 0.6926666666666667, 0.627, 0.5548]
bic_1993 = [0.765, 0.738, 0.668, 0.60325, 0.539]

icarl_cwa_no_rej = average_list_rounded(icarl_24, icarl_42, icarl_1993)
bic_cwa_no_rej = average_list_rounded(bic_24, bic_42, bic_1993)

# 2) Closed world with rejection accuracy
icarl_24 ={'0.3': [0.863, 0.7455, 0.658, 0.5995, 0.5534],
           '0.4': [0.863, 0.741, 0.6476666666666666, 0.58975, 0.5394],
           '0.5': [0.858, 0.7365, 0.632, 0.57025, 0.5152],
           '0.6': [0.848, 0.7175, 0.6076666666666667, 0.54275, 0.4814],
           '0.7': [0.837, 0.6975, 0.5796666666666667, 0.50975, 0.4444],
           '0.8': [0.82, 0.6685, 0.5516666666666666, 0.471, 0.3996]}
icarl_42 = {'0.3': [0.839, 0.738, 0.6926666666666667, 0.63175, 0.568],
            '0.4': [0.837, 0.734, 0.6846666666666666, 0.61875, 0.5542],
            '0.5': [0.833, 0.726, 0.6723333333333333, 0.60075, 0.526],
            '0.6': [0.826, 0.707, 0.6493333333333333, 0.572, 0.4924],
            '0.7': [0.821, 0.69, 0.626, 0.54475, 0.455],
            '0.8': [0.806, 0.6665, 0.5863333333333334, 0.505, 0.41]}

icarl_1993 = {'0.3': [0.801, 0.752, 0.6893333333333334, 0.63225, 0.556],
              '0.4': [0.801, 0.747, 0.6813333333333333, 0.619, 0.5372],
              '0.5': [0.797, 0.7355, 0.6676666666666666, 0.5975, 0.5084],
              '0.6': [0.783, 0.713, 0.64, 0.56375, 0.4772],
              '0.7': [0.762, 0.6875, 0.6096666666666667, 0.53125, 0.4358],
              '0.8': [0.747, 0.66, 0.573, 0.4855, 0.3898]}


bic_24 = {'0.3': [0.819, 0.7325, 0.6296666666666667, 0.58075, 0.5194],
          '0.4': [0.813, 0.7275, 0.615, 0.56575, 0.4996],
          '0.5': [0.803, 0.7165, 0.59, 0.532, 0.469],
          '0.6': [0.784, 0.689, 0.552, 0.49675, 0.4292],
          '0.7': [0.759, 0.666, 0.5123333333333333, 0.45725, 0.3892],
          '0.8': [0.715, 0.631, 0.4716666666666667, 0.4075, 0.3328]}
bic_42 = {'0.3': [0.806, 0.7385, 0.691, 0.6205, 0.5492],
          '0.4': [0.804, 0.7305, 0.6833333333333333, 0.60225, 0.532],
          '0.5': [0.796, 0.718, 0.6656666666666666, 0.57275, 0.5062],
          '0.6': [0.774, 0.696, 0.6336666666666667, 0.53825, 0.4678],
          '0.7': [0.752, 0.664, 0.6036666666666667, 0.49775, 0.4352],
          '0.8': [0.728, 0.626, 0.5583333333333333, 0.45675, 0.3866]}

bic_1993 = {'0.3': [0.751, 0.7375, 0.6663333333333333, 0.59875, 0.5292],
            '0.4': [0.746, 0.7315, 0.6516666666666666, 0.58225, 0.5102],
            '0.5': [0.739, 0.717, 0.6303333333333333, 0.54925, 0.4778],
            '0.6': [0.713, 0.691, 0.5953333333333334, 0.51325, 0.4372],
            '0.7': [0.698, 0.6585, 0.5556666666666666, 0.4745, 0.3954],
            '0.8': [0.661, 0.6215, 0.51, 0.4335, 0.3486]}

icarl_cwa_with_rej = average_dict_rounded(icarl_24, icarl_42, icarl_1993)
bic_cwa_with_rej = average_dict_rounded(bic_24, bic_42, bic_1993)
# 3) Open World Accuracy
icarl_24 = {'0.3': [0.0032, 0.0124, 0.0314, 0.0596, 0.0844],
            '0.4': [0.0246, 0.0534, 0.0994, 0.1434, 0.201],
            '0.5': [0.0684, 0.129, 0.1978, 0.267, 0.3282],
            '0.6': [0.1376, 0.2244, 0.315, 0.3862, 0.4608],
            '0.7': [0.2034, 0.3156, 0.4256, 0.497, 0.5742],
            '0.8': [0.2838, 0.4206, 0.531, 0.6094, 0.6822]}

icarl_42 = {'0.3': [0.003, 0.0126, 0.0372, 0.0574, 0.1004],
            '0.4': [0.0236, 0.0606, 0.1088, 0.1518, 0.2274],
            '0.5': [0.0726, 0.1294, 0.2036, 0.2744, 0.3526],
            '0.6': [0.147, 0.23, 0.3074, 0.3936, 0.469],
            '0.7': [0.2146, 0.3238, 0.4108, 0.5014, 0.5744],
            '0.8': [0.2916, 0.4172, 0.5218, 0.6086, 0.6692]}
icarl_1993 = {'0.3': [0.0054, 0.0142, 0.0338, 0.0586, 0.091],
              '0.4': [0.0358, 0.0652, 0.108, 0.15, 0.2058],
              '0.5': [0.0894, 0.14, 0.209, 0.2702, 0.3304],
              '0.6': [0.1772, 0.2368, 0.3158, 0.3898, 0.4602],
              '0.7': [0.2564, 0.3268, 0.4194, 0.5032, 0.573],
              '0.8': [0.3458, 0.4326, 0.5228, 0.6078, 0.6722]}

bic_24 = {'0.3': [0.0114, 0.0184, 0.0598, 0.0882, 0.123],
          '0.4': [0.0566, 0.0752, 0.1732, 0.219, 0.2792],
          '0.5': [0.1248, 0.1732, 0.311, 0.3678, 0.437],
          '0.6': [0.2226, 0.2892, 0.4494, 0.5168, 0.5736],
          '0.7': [0.315, 0.407, 0.5682, 0.6258, 0.6876],
          '0.8': [0.413, 0.5256, 0.674, 0.7388, 0.7884]}

bic_42 = {'0.3': [0.0062, 0.0268, 0.0508, 0.101, 0.0932],
          '0.4': [0.0434, 0.1026, 0.1512, 0.2308, 0.2248],
          '0.5': [0.1078, 0.2126, 0.2724, 0.3678, 0.3766],
          '0.6': [0.2132, 0.3402, 0.3916, 0.4966, 0.505],
          '0.7': [0.3134, 0.4552, 0.4976, 0.6024, 0.6138],
          '0.8': [0.414, 0.558, 0.6072, 0.7056, 0.7156]}

bic_1993 = {'0.3': [0.0104, 0.0198, 0.049, 0.0678, 0.1106],
            '0.4': [0.0524, 0.0792, 0.15, 0.1884, 0.256],
            '0.5': [0.1302, 0.1696, 0.2728, 0.3378, 0.4138],
            '0.6': [0.2366, 0.3006, 0.3922, 0.4726, 0.5488],
            '0.7': [0.325, 0.4092, 0.5082, 0.5796, 0.6714],
            '0.8': [0.4286, 0.5266, 0.6234, 0.6884, 0.7744]}

icarl_owa = average_dict_rounded(icarl_24, icarl_42, icarl_1993)
bic_owa = average_dict_rounded(bic_24, bic_42, bic_1993)

naive_strategy_db_icarl = pd.DataFrame({'CW no rejection' : icarl_cwa_no_rej ,
                           'CW with rejection' : icarl_cwa_with_rej['0.5'],
                           'Open World' : icarl_owa['0.5'],
                           'OWH': [0.14, 0.225, 0.311, 0.371, 0.408]}, index=list(range(10, 60, 10)))
naive_strategy_db_BiC = pd.DataFrame({'CW no rejection' : bic_cwa_no_rej ,
                           'CW with rejection' : bic_cwa_with_rej['0.5'],
                           'Open World' : bic_owa['0.5'],
                           'OWH': [0.209, 0.294, 0.392, 0.434, 0.443]}, index=list(range(10, 60, 10)))
print('Global threshold 0.5 ')
print('\n iCaRL\n ')
print(naive_strategy_db_icarl.transpose())
print('\n BiC \n')
print(naive_strategy_db_BiC.transpose())
# print to csv
naive_strategy_db_icarl.transpose().to_csv("icarl05_results.csv")
naive_strategy_db_BiC.transpose().to_csv("bic05_results.csv")

stats_08 = pd.DataFrame({'CW no rejection' : bic_cwa_no_rej,
    'CW with rejection' : bic_cwa_with_rej['0.8'],
                         'Open World' : bic_owa['0.8'],
                         'OWH' : [0.524, 0.578, 0.566, 0.537, 0.484]}, index=list(range(10, 60, 10)))
print('Global threshold 0.8 - BiC ')
print(stats_08.transpose())
stats_08.transpose().to_csv("bic08_results.csv")




