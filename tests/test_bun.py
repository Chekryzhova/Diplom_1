from practikum.bun import Bun
import data

class TestBun:
    def test_name_of_bun_true(self):
        bun = Bun(data.BUNS_NAME[0], data.PRICE[0])
        assert bun.name == data.BUNS_NAME[0]

    def test_price_of_bun_true(self):
        bun = Bun(data.BUNS_NAME[1], data.PRICE[1])
        assert bun.price == data.PRICE[1]
    def test_get_name_bun(self):
        bun = Bun(data.BUNS_NAME[2], data.PRICE[2])
        assert bun.get_name() == data.BUNS_NAME[2]

    def test_get_price_bun(self):
        bun = Bun(data.BUNS_NAME[3], data.PRICE[3])
        assert bun.get_price() == data.PRICE[3]