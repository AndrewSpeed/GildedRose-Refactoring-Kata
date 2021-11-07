import pytest

from ..gilded_rose import Item, GildedRose

@pytest.fixture()
def item(sell_in=10, quality=40):
    return Item(name="Aged Brie", sell_in=sell_in, quality=quality)

def update_item(item):
    GildedRose([item]).update_quality()

class TestBrie():
    def test_brie_positive_sell_in_increases_quality_by_1(self, item):
        item.sell_in = 1
        original_quality = item.quality

        update_item(item)

        assert item.sell_in == 0
        assert item.quality == original_quality + 1

    def test_brie_sell_in_of_zero_increases_quality_by_2(self, item):
        item.sell_in = 0
        original_quality = item.quality

        update_item(item)

        assert item.sell_in == -1
        assert item.quality == original_quality + 2

    def test_brie_negative_sell_in_increases_quality_by_2(self, item):
        item.sell_in = -1
        original_quality = item.quality

        update_item(item)

        assert item.sell_in == -2
        assert item.quality == original_quality + 2

    def test_brie_quality_of_50_does_not_increase(self, item):
        original_sell_in = item.sell_in
        item.quality = 50

        update_item(item)

        assert item.sell_in == original_sell_in - 1
        assert item.quality == 50