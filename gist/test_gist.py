import pytest


def test_our_first_test() -> None:
    assert 1 == 1


@pytest.mark.skip
def test_should_be_skipped() -> None:
    assert 1 == 2


@pytest.mark.skipif(4 > 1, reason="Skipped because 4 > 1")
def test_should_be_skipped_if() -> None:
    assert 1 == 2
