# python은 oop 객체지향 프로그램을 지원함
# class 는 객체를 만드는 설계도
# 객체는 class를 인스턴스화 해서 생성함

class coffeeFranchise:
    # init 생성자라고하며 class를 인스턴스 화 할때
    # 필요한 인자값이 있다면 정의 해야함(없다면 안해도 됨.)
    # self 란 ?
    def __init__(self, nm, beans=None, menu=None,):
        self.branch_name = nm
        self.beans = beans
        self.menu = menu

    def make_ame(self): #class에 종속되어 있는 함수를 메서드 라고함
        if self.menu:
            print (f"{self.branch_name}에서는 {self.beans}으로 {self.menu}를 만듦")
        elif self.beans:
            print(f"{self.branch_name}에서는 {self.beans}으로 커피를 만듦")
        else:
            print(f"{self.branch_name}에서는 신선한 커피를 제공합니다.")
#------------------------------ 정의 되어 있는 class 일 뿐 ------------------------------#


#------------------------------- 인스턴스 화 해서 실핼하기 -------------------------------#
future = coffeeFranchise("미래융합점", "미래 블랜드", "미래 라떼")
city = coffeeFranchise("둔산점")
mok = coffeeFranchise("목원대점", "말차파우더", "말차라떼")

future.make_ame() #인스턴스 메서드 초풀
mok.make_ame()
city.make_ame()