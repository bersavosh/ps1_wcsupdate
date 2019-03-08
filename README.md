# ps1_wcsupdate
A short script to add RADESYS keyword to Pan-STARRS1 image cutouts obtained from [the MAST archive](https://ps1images.stsci.edu/cgi-bin/ps1cutouts). This is to help some packages/softwares (like ds9 v8.0) read the WCS info properly. For more information about the issue, see [here](https://outerspace.stsci.edu/display/PANSTARRS/PS1+DR2+caveats#PS1DR2caveats-FITSimageformatquirks).

To run it:
```
$ python ps1_wcs_corr.py ps1_cutout.fits
```
