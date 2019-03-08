"""
A short script to add the RADESYS keyword to Pan-STARRS1 image cutouts.
This is to help some packages/softwares (like ds9 v8.0) read the WCS info properly.
For more information, please see:
https://outerspace.stsci.edu/display/PANSTARRS/PS1+DR2+caveats#PS1DR2caveats-FITSimageformatquirks

Developed by Arash Bahramian (https://bersavosh.github.io/).
"""

import argparse
from astropy.io import fits

def parser():
    """
    A simple parser for commandline arguments
    """
    parser = argparse.ArgumentParser(description="A short script to add the RADESYS keyword to Pan-STARRS1 image cutouts.\
                                                  This is to help some packages/softwares (like ds9 v8.0) read the WCS info properly.\
                                                  For more information, please see:\
                                                  https://outerspace.stsci.edu/display/PANSTARRS/PS1+DR2+caveats#PS1DR2caveats-FITSimageformatquirks")

    parser.add_argument('path', type=str, help='Path to the Pan-STARRS1 image cutouts fits file.')
    args = parser.parse_args()
    return args

def wcs_correction(path):
    """
    Adding RADESYS keyword to panstar image cutouts
    """
    with fits.open(path, mode='update') as hdul:
        hdul[0].header['RADESYS'] = 'FK5'
        hdul.flush()  

wcs_correction(parser().path)
