import math

def main():
    A0 = float(input("请输入初始活度："))
    T_half = float(input("请输入半衰期："))
    delta_t = float(input("请输入时间段长度："))
    direction = input("请输入‘之前（0）’或‘之后（1）’：")

    lambda_ = math.log(2) / T_half

    if direction == "1":
        A = A0 * math.exp(-lambda_ * delta_t)
        print(f"{delta_t} 时间之后的活度为：{A}")
    elif direction == "0":
        A = A0 * math.exp(lambda_ * delta_t)
        print(f"{delta_t} 时间之前的活度为：{A}")
    else:
        print("输入无效，请输入‘之前’或‘之后’。")

if __name__ == "__main__":
    main()
    
# 10675 12836 16182 63108
# 79.16 109.61 90.78