import pytest
from app import bubblesort

sortedhugelist = [i for i in range(5000)]

test_data = [[0,1,2,3,4], [9,8,7,6,5,4,3,2,1],[100,1,200,2,30,4,], [1,1,2,1,1],[2,1,10,5,3,8,7,11,0], sortedhugelist]

@pytest.mark.parametrize('list_to_sort', test_data)
def test_bubblesort(list_to_sort):
    expected_output = sorted(list_to_sort)
    sorted_list = bubblesort(list_to_sort)
    assert sorted_list == expected_output
