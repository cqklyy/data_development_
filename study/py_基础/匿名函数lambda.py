def test_fuc(compute):
    result = compute(1, 2)
    print(f"结果是：{result}")


# test_fuc(lambda x, y: x + y)

def compute(x,y):
    return x+y

test_fuc(compute)