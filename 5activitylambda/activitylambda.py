import math

def half_life_decay_constant(value):
    return math.log(2) / value

def main():
    # choice = input("请输入数值: ")
    value = float(input("请输入数值: "))

    decay_constant = half_life_decay_constant(value)
    print(f"转换后为: {decay_constant}")

if __name__ == "__main__":
    main()