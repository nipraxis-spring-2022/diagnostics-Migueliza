import numpy as np
import numpy.typing as npt


def iqr_detector(measures: npt.NDArray[float], iqr_proportion: float=1.5) -> npt.NDArray[bool]:
    """ Detect outliers in `measures` using interquartile range.

    Returns a boolean vector of same length as `measures`, where True means the
    corresponding value in `measures` is an outlier.

    Call Q1, Q2 and Q3 the 25th, 50th and 75th percentiles of `measures`.

    The interquartile range (IQR) is Q3 - Q1.

    An outlier is any value in `measures` that is either:

    * > Q3 + IQR * `iqr_proportion` or
    * < Q1 - IQR * `iqr_proportion`.

    See: https://en.wikipedia.org/wiki/Interquartile_range

    Parameters
    ----------
    measures : 1D array
        Values for which we will detect outliers
    iqr_proportion : float, optional
        Scalar to multiply the IQR to form upper and lower threshold (see
        above).  Default is 1.5.

    Returns
    -------
    outlier_tf : 1D boolean array
        A boolean vector of same length as `measures`, where True means the
        corresponding value in `measures` is an outlier.
    """
    q1 = _compute_percentile(array=measures, percentile=25)
    q3 = _compute_percentile(array=measures, percentile=75)
    iqr = q3 - q1

    outlier_thresshold_1 = q3 + (iqr * iqr_proportion)
    outlier_thresshold_2 = q1 - (iqr * iqr_proportion)

    mask_1 = measures > outlier_thresshold_1
    mask_2 = measures < outlier_thresshold_2

    return np.logical_or(mask_1, mask_2)

def _compute_percentile(array: npt.NDArray, percentile: float, method: str='linear') -> float:
    """Computes percentile using numpy.percentile method.

    Parameters
    ----------
    array : NDArray
        array along which to compute the percentiles
    percentile : float
        Represents the th percentile to compute the desired quartile
    method : str
        Represents the method to use to compute the percentile

    Returns
    -------
        float
            quartile for a given percentile
    """
    return np.percentile(array, percentile, method=method)
