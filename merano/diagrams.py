#!/usr/bin/python
#-*- coding: utf-8 -*-

### Import



import numpy as np
import pylab as plt



### 1 - Barplot to compare organism

def make_multiple_barplot(modules,label,value):
    """
    Make multiple barplot

    args:
        modules (list): modules' name
        label (list) : organism's name
        value (list) :values for each modules for each organism

    return:
        list [name,description]
    """
    x=np.arange(len(modules))
    width=0.8
    #fig, ax = plt.subplots()
    n=len(value)
    for i in range(n):
        plt.bar(x - width/2. + i/float(n)*width, value[i], 
                width=width/float(n), align="edge", label=label[i])

    
    plt.xticks(x,modules,rotation=45,horizontalalignment='right',fontweight='light')
    plt.title('Division of metabolisms within the bacteria')
    plt.tight_layout()
    plt.legend()
    name='multiple_barplot'
    plt.savefig('./Results/'+name, format='png')
    plt.close()
    description='Comparaison of presence of modules in each organismes'
    return [name,description]

### 2 - Barplot for one organism

def make_barplot(modules,label,value):
    """
    Make barplot

    args:
        modules (list): modules' name
        label (list) : organism's name
        value (list) :values for each modules for one organism

    return:
        list [name,description]
    """
    x=np.arange(len(modules))
    width=0.8

    plt.bar(x , value,width, align="edge", label=label)
    plt.xticks(x,modules,rotation=45,horizontalalignment='right',fontweight='light')
    plt.title('Division of metabolisms within ' + label)
    plt.tight_layout()
    plt.legend()
    name=('barplot_'+label)
    plt.savefig('./Results/'+name, format='png')
    plt.close()
    description=('Barplot illustrating the size of each module present in '+label)
    return [name,description]

### 3 - Pie chart represente proportion of modules in a organism

def make_pie(module,label,value):
    """
    Make pie

    args:
        modules (list): modules' name
        label (list) : organism's name
        value (list) :values for each modules for one organism

    return:
        list [name,description]
    """
    modules=np.array(module)
    values=np.array(value)
    fig, ax=plt.subplots(subplot_kw=dict(aspect='equal')) # Equal aspect ratio ensures the pie chart is circular.

    bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
    wedges, texts = ax.pie(values, wedgeprops=dict(width=1), startangle=+40)
    kw = dict(arrowprops=dict(arrowstyle="-"),bbox=bbox_props, zorder=0, va="center")
    for i, p in enumerate(wedges):
        percent = 100.*values/sum(values)
        ang = (p.theta2 - p.theta1)/2. + p.theta1
        y = np.sin(np.deg2rad(ang))
        x = np.cos(np.deg2rad(ang))
        horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
        connectionstyle = "angle,angleA=0,angleB={}".format(ang)
        kw["arrowprops"].update({"connectionstyle": connectionstyle})
        ax.annotate(['{1:1.2f} %'.format(v,n) for v,n in zip(modules, percent)][i], xy=(x, y), xytext=(1.35*np.sign(x), 1.4*y),horizontalalignment=horizontalalignment, **kw)

    ax.set_title('Division of metabolisms within '+label)
    plt.legend(modules, bbox_to_anchor=(2,0), loc="lower left", bbox_transform=plt.gcf().transFigure)
    name=('pie_'+label)
    plt.savefig('./Results/'+ name, format='png')
    plt.close()
    description=('Pie chart illustrating the percent of each module present in '+label)
    return [name,description]
    
