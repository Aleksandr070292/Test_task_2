import math


class AreaCalculator:
    @staticmethod
    def circle_area(radius):
        return math.pi * radius ** 2

    @staticmethod
    def triangle_area(side1, side2, side3):
        semi_perimeter = (side1 + side2 + side3) / 2
        return math.sqrt(semi_perimeter * (semi_perimeter - side1) * (semi_perimeter - side2) * (semi_perimeter - side3))

    @staticmethod
    def is_right_triangle(side1, side2, side3):
        sides = [side1, side2, side3]
        sides.sort()
        return sides[0]**2 + sides[1]**2 == sides[2]**2


# Юнит-тесты
def run_tests():
    # Тест для вычисления площади круга
    assert AreaCalculator.circle_area(5) == 25 * math.pi

    # Тест для вычисления площади треугольника
    assert math.isclose(AreaCalculator.triangle_area(3, 4, 5), 6)

    # Тест для проверки, является ли треугольник прямоугольным
    assert AreaCalculator.is_right_triangle(3, 4, 5) == True

    print("All tests passed successfully!")


if __name__ == "__main__":
    run_tests()
