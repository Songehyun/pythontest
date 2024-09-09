# 기본
# my_name = input("이름을 입력하세요: ")

# def print_name(name):
#     print(f"내이름은 {name} 입니다.")

# print_name(my_name)


# 쉬운방법
# my_sung = input("성씨를 입력하세요: ")
# my_name = input("이름을 입력하세요: ")

# def print_name(sung, name):
#     print(f"내이름의 성씨는 {sung} 이고, 내 이름은 {name} 입니다.")

# print_name(my_sung, my_name)


# 논리 생각해보기
my_fullname = input("이름을 입력하세요 : ")
def print_name(name):
    print(f"내이름의 성씨는 {name[0]} 이고, 내 이름은 {name[1] + name[2]} 입니다.")

print_name(my_fullname)