from sdatools.core.utils import SeriesLike, max_SeriesLike, min_SeriesLike


def test_max_SeriesLike():
    data = [-1, 0, 1, 3, 4]
    max = max_SeriesLike(data)
    assert max == 4


def test_min_SeriesLike():
    data = [-1, 0, 1, 3, 4]
    min = min_SeriesLike(data)
    assert min == -1
