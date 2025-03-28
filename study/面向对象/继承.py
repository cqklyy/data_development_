class Phone:
    IMEI = None
    producer = "cqk"

    def call_by_5g(self):
        print("使用5g网络进行通话")

# 定义子类，复写父类成员
class MyPhone(Phone):
    product="lyy"  #复写父类的属性进行覆盖

    def call_by_5g(self):
        print("开启CPU单核模式")
        print(f"父类被覆盖的成员属性：{super().producer}")
        Phone.call_by_5g(self)

phone=MyPhone()
print(phone.product)
phone.call_by_5g()