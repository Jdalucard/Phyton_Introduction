# This is a sample function  simple
def hello(args):
    print("Hello,", args)


hello("WORLD".capitalize())


# created function with variable


def Hello_two(name, sex):
    sex.lower()
    if sex == "women":
        print("Hello Ms.", name.capitalize())
    else:
        print("Hello Mr.", name.capitalize())


Hello_two("daniels", "women")
Hello_two("Lucy", "women")


# created valued que retorted the value


def created_Password(num):
    chars = "abcdefghij"
    num_integer = str(num)
    num = int(num_integer[0])
    c1 = num - 2
    c2 = num
    c3 = num - 5
    password = f"{chars[c1]}{chars[c2]}{chars[c3]}{num * 2}"
    return password


print(created_Password(1))


# *args utils number params
def my_sum(*nums):
    return sum(nums)


print(my_sum(5445, 545441, 445848, 88484151, 845415))
