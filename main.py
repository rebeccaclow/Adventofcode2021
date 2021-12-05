from day01 import day01_part01, day01_part02
from utils import read_input


if __name__ == '__main__':
     test_depths = read_input("Day1Test.txt")
     depths = read_input("Day1.txt")
     print(day01_part01(test_depths))
     print(day01_part01(depths))
     print(day01_part02(test_depths))
     print(day01_part02(depths))


