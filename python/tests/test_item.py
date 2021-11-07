import pytest

from ..gilded_rose import Item, GildedRose

@pytest.fixture()
def item(sell_in=10, quality=40):
    return Item(name="Normal Item", sell_in=sell_in, quality=quality)

def update_item(item):
    GildedRose([item]).update_quality()

class TestItem():
    def test_normal_item_positive_sell_in_decreases_quality_by_1(self, item):
        item.sell_in = 1
        original_quality = item.quality

        update_item(item)

        assert item.sell_in == 0
        assert item.quality == original_quality - 1

    def test_normal_item_sell_in_of_zero_decreases_quality_by_2(self, item):
        item.sell_in = 0
        original_quality = item.quality

        update_item(item)

        assert item.sell_in == -1
        assert item.quality == original_quality - 2

    def test_normal_item_negative_sell_in_decreases_quality_by_2(self, item):
        item.sell_in = -1
        original_quality = item.quality

        update_item(item)

        assert item.sell_in == -2
        assert item.quality == original_quality - 2

    def test_normal_item_quality_of_zero_does_not_decrease(self, item):
        original_sell_in = item.sell_in
        item.quality = 0

        update_item(item)

        assert item.sell_in == original_sell_in - 1
        assert item.quality == 0
