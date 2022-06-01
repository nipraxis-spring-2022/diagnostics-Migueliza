import numpy as np
import os.path as op

from findoutlie import iqr_detector

MY_DIR = op.dirname(__file__)


def test_iqr_detector():
    # From: http://www.purplemath.com/modules/boxwhisk3.htm
    example_values = np.array(
        [10.2, 14.1, 14.4, 14.4, 14.4, 14.5, 14.5, 14.6, 14.7, 14.7, 14.7, 14.9, 15.1, 15.9, 16.4]
    )
    is_outlier = iqr_detector(example_values, 1.5)
    print(example_values[is_outlier])
    assert np.all(example_values[is_outlier] == [10.2, 15.9, 16.4])
    # Test not-default value for outlier proportion
    is_outlier = iqr_detector(example_values, 0.5)
    assert np.all(example_values[is_outlier] == [10.2, 14.1, 15.1, 15.9, 16.4])


if __name__ == '__main__':
    # File being executed as a script
    test_iqr_detector()
    print('Tests passed')
