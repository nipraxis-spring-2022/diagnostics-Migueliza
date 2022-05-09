import numpy as np
import nibabel as nib

from numpy.typing import ArrayLike


def spm_global(vol: ArrayLike) -> ArrayLike:
    """Calculate SPM global metric for array `vol`.

    Parameters
    ----------
    vol : ArrayLike
        Array giving image data, usually 3D.

    Returns
    -------
    ArrayLike
        SPM global metric for `vol`
    """
    T = np.mean(vol) / 8

    return np.mean(vol[vol > T])


def get_spm_globals(file_name: str) -> ArrayLike:
    """Calculate SPM global metrics for volumes in image filename `file_name`.

    Parameters
    ----------
    file_name : str
        Filename of file containing 4D image

    Returns
    -------
    spm_vals : ArrayLike
        SPM global metric for each 3D volume in the 4D image.
    """
    img = nib.load(file_name)
    data = img.get_fdata()
    spm_vals = np.empty(img.shape[-1])
    for i, vol in enumerate(range(img.shape[-1])):
        spm_vals[i] = spm_global(data[..., vol])

    return spm_vals
