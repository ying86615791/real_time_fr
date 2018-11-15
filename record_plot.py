
#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt

# six exp of ETFL(ce) on CK, MMI, Oulu-CASIA
# =============================================================================
# import numpy as np
# plt.figure(figsize=(4, 4), dpi=90)
# n_groups = 3
# index = np.arange(n_groups)
# bar_width = 0.23
# opacity = 1.0
# index_baseline = [-1,0,3]
# 
# # CK+ Oulu-CASIA MMI
# ce = [94.40, 98.30, 100, 97.5, 100, 94.7, 100]
# 
# ce_in_ck = [98.60, 98.30, 100, 98.0, 100, 100 , 100]
# ce_in_ck = [85.0,  93.8,  72.5, 85, 86.3, 100 , 100]
# 
# 
# plt.grid(True, linestyle = "--", axis="y")
# plt.rc('axes', axisbelow=True) 
# #plt.plot(index_baseline,baseline,color = 'peru', linestyle='--',label='Baseline', linewidth=1.5)
# 
# #plt.plot(index_baseline,only_center,color = 'c', linestyle='--',label='ETFL(ce)', linewidth=1.5)
# 
# rects2 = plt.bar(index, margin1, bar_width,alpha=opacity, color='c',label=r'$\alpha=1.0$')
# 
# rects2 = plt.bar(index+bar_width, margin2, bar_width,alpha=opacity, color='b',label=r'$\alpha=2.0$')
# 
# rects3 = plt.bar(index+bar_width*2, margin3, bar_width,alpha=opacity, color='r',label=r'$\alpha=3.0$')  
# 
# ax = plt.gca()
# #ax.set_xticks([0.15, 0.68, 0.97])
# #ax.set_yticks([97, 98, 99, 100])
# 
# #plt.xlabel(r'$\alpha$',fontsize=13)
# plt.ylabel('Accuracy (%)',fontsize=13)
# plt.xticks(index + bar_width*1, ('CK+', 'Oulu-CASIA', 'MMI'),fontsize=11)
# plt.ylim(75,100)
# plt.xlim(-0.3,2.775)
# plt.legend(fontsize=10,loc='upper right')
# plt.tight_layout()
# #plt.savefig('/home/hy/margin_cmp.pdf')
# plt.show()
# =============================================================================

# margin plot on CK, MMI, Oulu-CASIA, FER2013
# =============================================================================
# import numpy as np
# from matplotlib import font_manager
# chf = font_manager.FontProperties(fname='/usr/share/fonts/truetype/freefont/FreeSerif.ttf', size=18)
# 
# plt.figure(figsize=(9, 6), dpi=90)
# n_groups = 4
# index = np.arange(n_groups)
# bar_width = 0.22
# opacity = 1.0
# index_baseline = [-1,0,3]
# 
# # CK+ Oulu-CASIA MMI
# margin1 = [98.15, 85.63, 79.68, 72.444]
# margin2 = [98.68, 85.83, 80.68, 72.917]
# margin3 = [99.03, 86.25, 82.34, 73.224]
# margin4 = [97.56, 85.21, 79.85, 72.499]
# 
# 
# plt.grid(True, linestyle = "--", axis="y")
# plt.rc('axes', axisbelow=True) 
# #plt.plot(index_baseline,baseline,color = 'peru', linestyle='--',label='Baseline', linewidth=1.5)
# 
# #plt.plot(index_baseline,only_center,color = 'c', linestyle='--',label='ETFL(ce)', linewidth=1.5)
# 
# rects0 = plt.bar(index+bar_width, margin1, bar_width,alpha=opacity, color='c',label=r'$\alpha=1.0$')
# 
# rects1 = plt.bar(index+bar_width*2, margin2, bar_width,alpha=opacity, color='b',label=r'$\alpha=2.0$')
# 
# rects2 = plt.bar(index+bar_width*3, margin3, bar_width,alpha=opacity, color='r',label=r'$\alpha=3.0$')  
# 
# rects3 = plt.bar(index+bar_width*4, margin4, bar_width,alpha=opacity, color='steelblue',label=r'$\alpha=4.0$')  
# 
# for a,b in zip(index+bar_width, margin1):
#     plt.text(a, b+0.05, '%.2f' % b, ha='center', va= 'bottom', color='c', fontsize=10)
# for a,b in zip(index+bar_width*2, margin2):
#     plt.text(a, b+0.05, '%.2f' % b, ha='center', va= 'bottom', color='b', fontsize=10)
# for a,b in zip(index+bar_width*3, margin3):
#     plt.text(a, b+0.05, '%.2f' % b, ha='center', va= 'bottom', color='r', fontsize=10)
# for a,b in zip(index+bar_width*4, margin4):
#     plt.text(a, b+0.05, '%.2f' % b, ha='center', va= 'bottom', color='steelblue', fontsize=10)
# 
# ax = plt.gca()
# #ax.set_xticks([0.15, 0.68, 0.97])
# #ax.set_yticks([97, 98, 99, 100])
# 
# #plt.xlabel(r'$\alpha$',fontsize=13)
# plt.ylabel('Accuracy (%)',fontsize=18)
# plt.xticks(index + bar_width*2.4555, ('CK+', 'Oulu-CASIA', 'MMI', 'FER2013'),fontsize=18)
# plt.yticks(fontsize=18)
# plt.ylim(70,100)
# plt.xlim(-0.05,4.13)
# plt.legend(fontsize=18,loc='upper right', prop=chf)
# plt.tight_layout()
# plt.savefig('/home/hy/margin_cmp.pdf')
# plt.show()
# =============================================================================

# =============================================================================
# # baseline ETFL(CE) ETFL(ce+in) plot on CK, MMI, Oulu-CASIA
# import numpy as np
# from matplotlib import font_manager
# chf = font_manager.FontProperties(fname='/usr/share/fonts/truetype/freefont/FreeSerif.ttf',size=18)
# 
# plt.figure(figsize=(7, 5), dpi=90)
# n_groups = 3
# index = np.arange(n_groups)*1.3
# bar_width = 0.28
# opacity = 1.0
# 
# # CK+ Oulu-CASIA MMI
# baseline = [95.63, 82.92, 79.88]
# fesr_sp = [96.82, 84.17, 81.66]
# fesr_jt = [99.34, 88.13, 84.81]
# 
# 
# plt.grid(True, linestyle = "--", axis="y")
# plt.rc('axes', axisbelow=True) 
# 
# rects2 = plt.bar(index, baseline, bar_width,alpha=opacity, color='c',label=r'BASELINE')
# 
# rects2 = plt.bar(index+bar_width, fesr_sp, bar_width,alpha=opacity, color='b',label=r'FESR_SP')
# 
# rects3 = plt.bar(index+bar_width*2, fesr_jt, bar_width,alpha=opacity, color='r',label=r'FESR_JT')  
# 
# for a,b in zip(index, baseline):
#     plt.text(a, b+0.05, '%.2f' % b, ha='center', va= 'bottom', color='c', fontsize=10)
# for a,b in zip(index+bar_width, fesr_sp):
#     plt.text(a, b+0.05, '%.2f' % b, ha='center', va= 'bottom', color='b', fontsize=10)
# for a,b in zip(index+bar_width*2, fesr_jt):
#     plt.text(a, b+0.05, '%.2f' % b, ha='center', va= 'bottom', color='r', fontsize=10)
#     
# ax = plt.gca()
# #ax.set_xticks([0.15, 0.68, 0.97])
# #ax.set_yticks([97, 98, 99, 100])
# 
# #plt.xlabel(r'$\alpha$',fontsize=13)
# ax.spines['top'].set_visible(False)
# plt.ylabel('Accuracy (%)',fontsize=18)
# plt.xticks(index + bar_width*1, ('CK+', 'Oulu-CASIA', 'MMI'),fontsize=18)
# plt.yticks(fontsize=18)
# plt.ylim(70,100)
# plt.xlim(-0.35,3.5)
# plt.legend(fontsize=18,loc='upper right', prop=chf)
# plt.tight_layout()
# plt.savefig('/home/hy/joint_cmp.pdf')
# plt.show()
# =============================================================================

# intra-class RGBP plot on CK, MMI, Oulu-CASIA
import numpy as np
from matplotlib import font_manager
chf = font_manager.FontProperties(fname='/usr/share/fonts/truetype/freefont/FreeSerif.ttf',size=18)

plt.figure(figsize=(10, 6), dpi=90)
n_groups = 3
index = np.arange(n_groups)*1.6
bar_width = 0.22
opacity = 0.85

# CK+ Oulu-CASIA MMI
baseline = [95.63, 82.92, 79.88]
fesr_sl = [96.82, 84.17, 81.66]
fesr_jlnoIL = [97.48, 85.21, 82.80]
fesr_jlnoRGBP = [98.33, 86.32, 83.2143]
fesr_jl = [99.34, 88.13, 84.81]
fesr_real = [97.48, 83.46, 81.50]


plt.grid(True, linestyle = "--", axis="y")
plt.rc('axes', axisbelow=True) 

rects0 = plt.bar(index+bar_width, baseline, bar_width,alpha=opacity, color='steelblue',label=r'BASELINE')

rects1 = plt.bar(index+bar_width*2, fesr_sl, bar_width,alpha=opacity, color='c',label=r'FESR_SL')

rects2 = plt.bar(index+bar_width*3, fesr_jlnoIL, bar_width,alpha=opacity, color='b',label=r'FESR_JL-IL')

rects3 = plt.bar(index+bar_width*4, fesr_jlnoRGBP, bar_width,alpha=opacity, color='orchid',label=r'FESR_JL-RGBP')  

rects4 = plt.bar(index+bar_width*5, fesr_jl, bar_width,alpha=opacity, color='r',label=r'FESR_JL')  

# rects5 = plt.bar(index+bar_width*6, fesr_real, bar_width,alpha=opacity, color='sienna',label=r'FESR_Real')

for a,b in zip(index+bar_width, baseline):
    plt.text(a, b+0.05, '%.2f' % b, ha='center', va= 'bottom', color='steelblue', fontsize=10)
for a,b in zip(index+bar_width*2, fesr_sl):
    plt.text(a, b+0.05, '%.2f' % b, ha='center', va= 'bottom', color='c', fontsize=10)
for a,b in zip(index+bar_width*3, fesr_jlnoIL):
    plt.text(a, b+0.05, '%.2f' % b, ha='center', va= 'bottom', color='b', fontsize=10)
for a,b in zip(index+bar_width*4, fesr_jlnoRGBP):
    plt.text(a, b+0.05, '%.2f' % b, ha='center', va= 'bottom', color='orchid', fontsize=10)
for a,b in zip(index+bar_width*5, fesr_jl):
    plt.text(a, b+0.05, '%.2f' % b, ha='center', va= 'bottom', color='r', fontsize=10)
# for a,b in zip(index+bar_width*6, fesr_real):
#     plt.text(a, b+0.05, '%.2f' % b, ha='center', va= 'bottom', color='sienna', fontsize=10)
    
ax = plt.gca()
#ax.set_xticks([0.15, 0.68, 0.97])
#ax.set_yticks([97, 98, 99, 100])
ax.spines['top'].set_visible(False)

#plt.xlabel(r'$\alpha$',fontsize=13)
plt.ylabel('Accuracy (%)',fontsize=18)
plt.xticks(index + bar_width*3., ('CK+', 'Oulu-CASIA', 'MMI', 'FER2013'),fontsize=18)
plt.yticks(fontsize=18)
plt.ylim(70,100)
plt.xlim(-0.07,4.8)
plt.legend(fontsize=18,loc='upper right', prop=chf)
plt.tight_layout()
plt.savefig('/home/hy/fesr_cmp.pdf')
plt.show()

# SSW plot on CK, MMI, Oulu-CASIA
# =============================================================================
# import numpy as np
# plt.figure(figsize=(6, 5), dpi=90)
# n_groups = 4
# index = np.arange(n_groups)
# bar_width = 0.3
# opacity = 1.0
# index_baseline = [-1,0,3]
# 
# # CK+ Oulu-CASIA MMI
# no_ssw = [97.92, 85.63, 80.16, 72.444]
# with_ssw = [99.03, 86.25, 82.34, 73.224]
# 
# 
# plt.grid(True, linestyle = "--", axis="y")
# plt.rc('axes', axisbelow=True) 
# 
# rects2 = plt.bar(index+bar_width, no_ssw, bar_width,alpha=opacity, color='b',label=r'no SSW')
# 
# rects3 = plt.bar(index+bar_width*2, with_ssw, bar_width,alpha=opacity, color='r',label=r'with SSW')  
# 
# for a,b in zip(index+bar_width, no_ssw):
#     plt.text(a, b+0.05, '%.2f' % b, ha='center', va= 'bottom', color='b', fontsize=8)
# for a,b in zip(index+bar_width*2, with_ssw):
#     plt.text(a, b+0.05, '%.2f' % b, ha='center', va= 'bottom', color='r', fontsize=8)
#     
# ax = plt.gca()
# #ax.set_xticks([0.15, 0.68, 0.97])
# #ax.set_yticks([97, 98, 99, 100])
# 
# #plt.xlabel(r'$\alpha$',fontsize=13)
# plt.ylabel('Accuracy (%)',fontsize=13)
# plt.xticks(index + bar_width*1.445, ('CK+', 'Oulu-CASIA', 'MMI'),fontsize=11)
# plt.ylim(70,100)
# plt.xlim(-0.14,4)
# plt.legend(fontsize=15,loc='upper right')
# plt.tight_layout()
# plt.savefig('/home/hy/ssw_cmp.pdf')
# plt.show()
# =============================================================================

# lambda plot on FER2013
# =============================================================================
# lam_inter = [0.001,0.005,0.01,0.05,0.1]
# marks = ['0.001','0.005','0.01','0.05','0.1']
# #margin1
# margin1_center0001 = [72.249,72.527,72.694,72.388,72.388]
# margin1_center0005 = [72.36,72.834,72.694,72.527,72.639]
# margin1_center001 = [72.137,73.084,72.555,72.444,72.221]
# margin1_center005 = [72.165,72.221,72.221,72.444,72.221]
# margin1_center01 = [72.583,72.75,72.834,72.583,72.639]
# margin1_y = [margin1_center0001,margin1_center0005,margin1_center001,margin1_center005,margin1_center01]
# 
# inter0 = [72.053,71.803,71.831,72.249,72.137]
# margin1_inter0001 = [72.249,72.36,72.137,72.165,72.583]
# margin1_inter0005 = [72.527,72.834,73.084,72.221,72.75]
# margin1_inter001 = [72.694,72.694,72.555,72.221,72.834]
# margin1_inter005 = [72.388,72.527,72.444,72.444,72.583]
# margin1_inter01 = [72.388,72.639,72.221,72.221,72.639]
# 
# #margin2
# margin2_center0001 = [72.666,72.193,72.081,72.917,71.914]
# margin2_center0005 = [72.081,72.137,72.249,72.499,71.97]
# margin2_center001 = [72.221,72.583,72.499,72.109,71.775]
# margin2_center005 = [72.499,72.165,72.249,72.917,72.471]
# margin2_center01 = [72.583,72.499,72.416,72.527,72.945]
# margin2_y = [margin2_center0001,margin2_center0005,margin2_center001,margin2_center005,margin2_center01]
# 
# margin2_inter0001 = [72.666,72.081,72.221,72.499,72.583]
# margin2_inter0005 = [72.193,72.137,72.583,72.165,72.499]
# margin2_inter001 = [72.081,72.249,72.499,72.249,72.416]
# margin2_inter005 = [72.917,72.499,72.109,72.917,72.527]
# margin2_inter01 = [72.332,72.224,72.276,72.471,72.945]
# 
# #margin3
# margin3_inter0001 = [72.471,72.444,72.555,72.444,72.973]
# margin3_inter0005 = [72.834,72.36,72.527,72.722,73.029]
# margin3_inter001 = [72.666,72.75,73.057,72.834,72.75]
# margin3_inter005 = [72.694,72.304,72.221,73.168,72.889]
# margin3_inter01 = [72.694,73.029,72.694,72.722,72.722]
# 
# 
# 
# import numpy as np
# plt.figure(figsize=(8, 6), dpi=90)
# n_groups = 5
# index = np.arange(n_groups)
# index_baseline = [-1,0,1,2,5.5]
# plt.plot(index,inter0,color = 'darkred', linestyle='--',label=r'$\lambda_{in}=0$')
# plt.plot(index,margin3_inter0001,color = 'red',label=r'$\lambda_{in}=0.001$')
# plt.plot(index,margin3_inter0005,color = 'green',label=r'$\lambda_{in}=0.005$')
# plt.plot(index,margin3_inter001,color = 'purple',label=r'$\lambda_{in}=0.01$')
# plt.plot(index,margin3_inter005,color = 'orange',label=r'$\lambda_{in}=0.05$')
# plt.plot(index,margin3_inter01,color = 'blue',label=r'$\lambda_{in}=0.1$')
# plt.xlabel(r'$\lambda_{ce}$',fontsize=13)
# plt.ylabel('Accuracy (%)',fontsize=13)
# plt.xticks(index, ('0.001', '0.005', '0.01', '0.05', '0.1'),fontsize=11)
# plt.legend(fontsize=11,loc='upper right')
# plt.ylim(71.5,74.5)
# plt.xlim(0,4)
# plt.savefig('/home/hy/cop_in_margin3.pdf')
# plt.show()
# =============================================================================

# =============================================================================
# c = ['orange', 'deepskyblue', '#00ff00', '#00ffff', 'red', 
#      '#ff00ff', '#990000', '#999900', '#009900', '#009999']
# for idx,item in enumerate(margin2_y):
#     print idx
#     plt.plot(lam_inter,item,label=marks[idx],linewidth=3,color=c[idx],marker='.'
#     ,markersize=12)
# plt.legend() 
# plt.show() 
# =============================================================================

# cmp baseline plot on FER2013 
# =============================================================================
# import numpy as np
# plt.figure(figsize=(8, 6), dpi=90)
# n_groups = 5
# index = np.arange(n_groups)
# bar_width = 0.15
# opacity = 1.0
# index_baseline = [-1,0,1,2,5.5]
# baseline = [71.413,71.413,71.413,71.413,71.413]
# inter0_center = [72.053,71.803,71.831,72.249,72.137]
# margin1_center = [72.694,72.834,73.084,72.444,72.834]
# margin2_center = [72.917,72.499,72.583,72.917,72.945]
# margin3_center = [72.834,73.029,73.057,73.168,73.029]
# plt.plot(index_baseline,baseline,color = 'darkred', linestyle='--',label='Baseline')
# rects1 = plt.bar(index, inter0_center, bar_width,alpha=opacity, color='orange',label=r'$\lambda_{in}=0$ (ce)')
# rects2 = plt.bar(index+bar_width, margin1_center, bar_width,alpha=opacity, color='g',label=r'$\alpha=1.0$ (ce+in)')
# rects3 = plt.bar(index+bar_width*2, margin2_center, bar_width,alpha=opacity, color='b',label=r'$\alpha=2.0$ (ce+in)')  
# rects4 = plt.bar(index+bar_width*3, margin3_center, bar_width,alpha=opacity, color='r',label=r'$\alpha=3.0$ (ce+in)')
# plt.xlabel(r'$\lambda_{ce}$',fontsize=13)
# plt.ylabel('Accuracy (%)',fontsize=13)
# plt.xticks(index + bar_width, ('0.001', '0.005', '0.01', '0.05', '0.1'),fontsize=11)
# plt.ylim(71,74)
# plt.xlim(-0.3,4.8)
# plt.legend(fontsize=11,loc='upper left')
# plt.savefig('/home/hy/cop_ce_in.pdf')
# plt.show()
# =============================================================================


# =============================================================================
# import matplotlib.pyplot as plt
# import numpy as np
# 
# 
# def f(t):
#     'A damped exponential'
#     s1 = np.cos(2 * np.pi * t)
#     e1 = np.exp(-t)
#     return s1 * e1
# 
# 
# t1 = np.arange(0.0, 5.0, .2)
# 
# l = plt.plot(t1, f(t1), 'ro')
# plt.setp(l, 'markersize', 30)
# plt.setp(l, 'markerfacecolor', 'C')
# 
# plt.show()
# 
# plt.figure()
# 
# x=np.linspace(0,5,50)
# y = 2/(1+np.power(np.e,-(x+0)))-1
# plt.plot(x,y,linewidth=3)
# plt.xlim(-0.3,4)
# plt.show()
# =============================================================================