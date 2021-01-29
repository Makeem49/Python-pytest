from calculator import Calculator, CalculatorError, MyError
import pytest



"""Grouping each test task into groups """
class TestAdd:  
    def test_add(self):
        calculator = Calculator()
        result = calculator.add(5, 7)
        assert 12 == result

    @pytest.mark.parametrize('a,b,expected', [
        (1,2,3),
        (2,2,4),
        (3,2,5),
        (4,2,6),
        (5,2,7),
        (6,2,8),
        (7,2,9),
        (8,2,10)
    ])
    def test_add_int(self,a,b,expected):
        calculator = Calculator()
        result = calculator.add_int(a,b)
        assert result == expected


    def test_add_int_another(self):
        calculator = Calculator()
        with pytest.raises(MyError):
            result = calculator.add_int(99,0)
        

    def test_wierder_stuff(self):
        calculator = Calculator()
        with pytest.raises(CalculatorError):
            result = calculator.add('hello', 'wolrd')
    
    

"""Grouping each test task into groups """
class TestSubtract:
    def test_substract(self):
        calculator = Calculator()
        result = calculator.subtract(7,2)
        assert 5 == result


    def test_subtract(self):
        calculator = Calculator()
        result = calculator.multiply(2,4)
        assert 8 == result



"""Grouping each test task into groups """
class TestDivide:
    def test_divide(self):
        calculator = Calculator()
        result = calculator.divide(10,2)
        assert 5 == result

    def test_divide_by_zero(self):
        calculator = Calculator()
        with pytest.raises(CalculatorError):
            result = calculator.divide(9, 0)





    











