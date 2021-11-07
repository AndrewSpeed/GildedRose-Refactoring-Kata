import pytest

from ..gilded_rose import Item, GildedRose

@pytest.fixture()
def item(sell_in=10, quality=40):
    return Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=sell_in, quality=quality)

def update_item(item):
    GildedRose([item]).update_quality()

class TestBackstagePasses():
    def test_backstage_passes_sell_in_of_eleven_increases_quality_by_1(self, item):
        item.sell_in = 11
        original_quality = item.quality

        update_item(item)

        assert item.sell_in == 10
        assert item.quality == original_quality + 1

    def test_backstage_passes_sell_in_less_than_eleven_increases_quality_by_2(self, item):
        item.sell_in = 10
        original_quality = item.quality

        update_item(item)

        assert item.sell_in == 9
        assert item.quality == original_quality + 2

    def test_backstage_passes_sell_in_less_than_six_increases_quality_by_3(self, item):
        item.sell_in = 5
        original_quality = item.quality

        update_item(item)

        assert item.sell_in == 4
        assert item.quality == original_quality + 3

    def test_backstage_passes_sell_in_of_zero_drops_quality_to_zero(self, item):
        item.sell_in = 0

        update_item(item)

        assert item.sell_in == -1
        assert item.quality == 0

    def test_backstage_passes_negative_sell_in_drops_quality_to_zero(self, item):
        item.sell_in = -1

        update_item(item)

        assert item.sell_in == -2
        assert item.quality == 0

    def test_backstage_passes_quality_of_50_does_not_increase(self, item):
        original_sell_in = item.sell_in
        item.quality = 50

        update_item(item)

        assert item.sell_in == original_sell_in - 1
        assert item.quality == 50