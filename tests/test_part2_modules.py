
from modules.discount import DiscountEngine
from modules.order import OrderCalculator

def test_order_calculator_uses_discount_engine():
    de = DiscountEngine()
    calc = OrderCalculator(de)

    assert calc.final_total(120.0, 0.19) == 128.52 # 10% OFF
    assert calc.final_total(60.0, 0.19) == 67.83 # 5% OFF
    assert calc.final_total(240.0, 0.19) == 242.76 # 15% OFF
    assert calc.final_total(40.0, 0.19) == 47.6 # No descuento
    
