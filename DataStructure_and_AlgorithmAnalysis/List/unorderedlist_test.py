from unorderedlist import UnorderedList
import pytest


@pytest.fixture
def sample_list():
    lst = UnorderedList()
    lst.append(10)
    lst.append(20)
    lst.insert(1, 15)
    lst.insert(0, None)
    lst.insert(-1, 25)
    return lst


def test_size(sample_list):
    assert sample_list.size() == 5


def test_index(sample_list):
    assert sample_list.index(None) == 0
    assert sample_list.index(15) == 2
    assert sample_list.index(25) == 3
    with pytest.raises(ValueError):
        sample_list.index(999)


def test_search(sample_list):
    assert sample_list.search(20) is True
    assert sample_list.search(99) is False


def test_insert_bounds(sample_list):
    with pytest.raises(IndexError):
        sample_list.insert(42, 1)
    with pytest.raises(IndexError):
        sample_list.insert(-10, 1)


def test_remove(sample_list):
    sample_list.remove(15)
    assert sample_list.size() == 4
    with pytest.raises(ValueError):
        sample_list.remove(999)


def test_add_builds_reversed_list():
    lst = UnorderedList()
    lst.add(5)
    lst.add(10)
    assert lst.size() == 2
    assert lst.index(10) == 0
    assert lst.index(5) == 1


def test_append_preserves_order():
    lst = UnorderedList()
    lst.append(1)
    lst.append(2)
    lst.append(3)
    assert lst.size() == 3
    assert lst.index(3) == 2


def test_insert_negative_position(sample_list):
    sample_list.insert(-2, 17)
    assert sample_list.index(17) == sample_list.size() - 3


def test_pop_returns_values(sample_list):
    assert sample_list.pop() == 20
    assert sample_list.size() == 4
    assert sample_list.pop(0) is None
    assert sample_list.size() == 3


def test_pop_out_of_range(sample_list):
    with pytest.raises(IndexError):
        sample_list.pop(99)
    with pytest.raises(IndexError):
        sample_list.pop(-10)


def test_is_empty_transitions():
    lst = UnorderedList()
    assert lst.is_empty()
    lst.add(1)
    assert lst.is_empty() is False
    lst.pop()
    assert lst.is_empty()

