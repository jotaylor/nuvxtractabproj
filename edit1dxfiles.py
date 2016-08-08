import numpy as np
from stistools import calstis
import calcos
from astropy.io import fits
from costools import splittag
from stsci.tools import teal
from costools import x1dcorr
import glob
from matplotlib import pyplot as plt
plt.style.use(['seaborn-muted'])
from stsci.convolve import boxcar

origfile = 'w5g1439sl_1dx.fits'
outfolder = '/Users/esnyder/Desktop/trainingproject/new1dxfiles/'

hdulist = fits.open(origfile)

data = hdulist[1].data

len = np.size(data['height'])

#data.columns

#make new arrays
ints = np.array([7,13,17,23,27,33,37,43,47,53,57],dtype='int16')

for num in ints:

	newcolumn = np.ones(len,dtype='int16')*num

	#put into the file 
	data['height'] = newcolumn

	#write new file to output folder
	hdulist.writeto(outfolder + origfile.split('.')[0].split('_')[0] + '_' + str(num) + '.fits', clobber=True)

