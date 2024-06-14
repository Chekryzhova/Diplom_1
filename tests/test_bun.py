from practikum.bun import Bun
import data

class TestBun:

    def test_get_name_bun(self):
        bun = Bun(data.BUNS_NAME[2], data.PRICE[2])
        assert bun.get_name() == data.BUNS_NAME[2]

    def test_get_price_bun(self):
        bun = Bun(data.BUNS_NAME[3], data.PRICE[3])
        assert bun.get_price() == data.PRICE[3]