import os
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
from functools import partial
import multiprocessing as mp

rootdir = '/user/esnyder/nuvxtractabproj/'

subdirlist = ['smov4', 'cycle17', 'cycle18', 'cycle19', 'cycle20', 'cycle21', 'cycle22', 'cycle23']

reffiles = ['w5g1439sl_13.fits', 'w5g1439sl_33.fits', 'w5g1439sl_53.fits', 'w5g1439sl_17.fits', 'w5g1439sl_37.fits', 'w5g1439sl_57.fits', 'w5g1439sl_23.fits', 'w5g1439sl_43.fits', 'w5g1439s_l7.fits', 'w5g1439sl_27.fits', 'w5g1439sl_47.fits']

def parallel_cal(files, outputfolder):
    pool = mp.Pool(processes=10)
    calfunc = partial(calibrate_files, outputfolder)
    pdb.set_trace()
    pool.map(calfunc, files)

def calibrate_files(outputfolder, item):
	calcos.calcos(item ,outdir=outputfolder)

def edit_cal_files():
    for subdir in subdirlist:
    	mydir = os.path.join(rootdir, subdir)
    	rawfiles = glob.glob(os.path.join(mydir, '*_rawtag.fits'))
    	for ref in reffiles:
    		outputfolder = os.path.join(mydir, ref.split('_')[1].split('.')[0])
    		for myfile in rawfiles:
    			fits.setval(myfile, 'XTRACTAB', value = '/user/esnyder/nuvxtractabproj/new1dxfiles/' + str(ref), ext = 0)
    		asnfiles = glob.glob(os.path.join(mydir, '*_asn.fits'))
    		parallel_cal(asnfiles, outputfolder)


if __name__ == "__main__":
    edit_cal_files()
