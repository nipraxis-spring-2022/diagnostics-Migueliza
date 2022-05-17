""" Scan outlier metrics
"""

import numpy as np


def dvars(img):
    """Calculate dvars metric on Nibabel image `img`

    The dvars calculation between two volumes is defined as the square root of
    (the sum of the (voxel differences squared) divided by the number of
    voxels).

    Parameters
    ----------
    img : nibabel image

    Returns
    -------
    dvals : 1D array
        One-dimensional array with n-1 elements, where n is the number of
        volumnes in `img`.
    """
    data = img.get_fdata()
    diff_vols = np.diff(data, axis=-1)

    return np.sqrt(np.mean(diff_vols ** 2, axis=(0, 1, 2)))
