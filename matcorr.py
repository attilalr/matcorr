#coding=utf-8

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

class mcorr:
  def __init__(self, *args, **kwargs):

    self.df = None

    # default parameters
    cmap = "YlGnBu"
    vmin = 0
    vmax = 1
    fmt = '.2g'
    annot = True
    cbar = True
    self.verbose = 1

    if kwargs: # if we have keyword parameters
      if 'cmap' not in kwargs.keys():
        kwargs['cmap'] = cmap
      if 'vmin' not in kwargs.keys():
        kwargs['vmin'] = vmin
      if 'vmax' not in kwargs.keys():
        kwargs['vmax'] = vmax
      if 'fmt' not in kwargs.keys():
        kwargs['fmt'] = fmt
      if 'annot' not in kwargs.keys():
        kwargs['annot'] = annot
      if 'cbar' not in kwargs.keys():
        kwargs['cbar'] = cbar
      if 'verbose' in kwargs.keys():
        self.verbose = kwargs['verbose']
        del kwargs['verbose'] # delete to send the dict do sns.heatmap
    else: # if there is no keyword parameters we have to create kwargs dict
      kwargs = {}
      kwargs['cmap'] = cmap
      kwargs['vmin'] = vmin
      kwargs['vmax'] = vmax
      kwargs['fmt'] = fmt
      kwargs['annot'] = annot
      kwargs['cbar'] = cbar

    self.kwargs = kwargs

    if args and self.verbose:
      print 'Warning: positional arguments are ignored.'

  def show_matrix(self):
    try:
      plt.clf()
      sns.heatmap(self.df.corr(), **self.kwargs)
      plt.show()
    except:
      print 'Problem when ploting corr matrix. Check your data.' 

  def writefig(self, filename):
    try:
      plt.clf()
      sns.heatmap(self.df.corr(), **self.kwargs)
      plt.savefig(filename)
    except:
      print 'Problem when writing corr matrix. Check your data.' 

  def add_col(self, label, data):
    try:
      if data.size != self.df.ix[:,0].size:
        print 'Warning: adding column with different size.'
      self.df[label] = pd.Series(data, index=self.df.index)
    except:
      data = [(label, data)]
      self.df = pd.DataFrame.from_items(data)

