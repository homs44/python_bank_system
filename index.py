
import os

#화면 지우는 함수
def clear():
    os.system('cls')

# 계정을 저장하는 리스트
accounts = []

# 메뉴 출력 함수
def printMenu():
    print("="*20)
    print("뱅킹 서비스")
    print("1. 사용자 추가")
    print("2. 송금")
    print("3. 잔고확인")
    print("4. 전체 계좌 출력")
    print("프로그램 종료를 원하시면 0번을 입력하세요")
    print("="*20)

# 계좌 정보 출력
def printAccount(title, account, isShowPassword):
    print("*"*20)
    print(title)
    print("이름     : {0}".format(account["name"]))
    print("계좌     : {0}".format(account["address"]))
    if isShowPassword:
        print("비밀번호 : {0}".format(account["password"]))
    print("잔고     : {0}".format(account["balance"]))
    print("*"*20)

#계좌 추가하는 함수
def addAccount():
    print("계좌 개설")
    name = input("이름을 입력하세요 : ")
    address= input("계좌 주소를 입력하세요 : ")
    password = input("비밀번호를 입력하세요 : ")
    balance = int(input("잔고를 입력하세요 : "))

    account = {
        "name" : name,
        "address" : address,
        "password": password,
        "balance" : balance
    }

    accounts.append(account)

    printAccount("개설된 계좌 정보입니다.", account, True)
    
#계좌 전체 출력하는 함수
def printAllAccountAddress():
    print("전체 계좌 수: {0}".format(len(accounts)))
    print("*"*20)
    for account in accounts:
        print("계좌번호 : {0}".format(account["address"]))
    print("*"*20)

#잔고 확인하는 함수
def checkMyBalance():
    print("잔고 확인")

    address = None
    password = None

    address = input("계좌번호를 입력하세요 : ")
    password = input("비밀번호를 입력하세요 : ")

    for account in accounts:
        if account["address"] !=address:
            continue

        if account["password"] == password :
            printAccount("계좌 정보 입니다.", account, False)
        else:
            print("잘못된 비밀번호 입니다.")
        
        return
    
    print("등록되지 않은 계좌 입니다.")


def transfer():
    print("송금")
    
    myAddress = None
    myPassword = None

    otherAddress = None

    money = None

    myAddress = input("당신의 계좌번호를 입력하세요 : ")
    myPassword = input("비밀번호를 입력하세요 : ")
    otherAddress = input("상대방 계좌번호를 입력하세요 : ")
    money = int(input("송금할 금액을 입력하세요 : "))

    myAccount = None
    otherAccount = None

    # 내 계좌 있는지 비밀번호는 맞는지 잔고는 충분한지
    for account in accounts:
        if account["address"] != myAddress:
            continue
        
        if account["password"] == myPassword:
            myAccount = account
        break

    if myAccount is None:
        print("잘못된 접근입니다.")
        return

    if myAccount["balance"] < money:
        print("잔고가 부족합니다.")
        return

    # 상대방 계좌는 있는지 
    for account in accounts:
        if account["address"] != otherAddress:
            continue
        
        otherAccount = account
        break

    if otherAccount is None:
        print("상대방 계좌가 없습니다.")
        return

    # 송금

    myAccount["balance"] = myAccount["balance"] - money
    otherAccount["balance"] = otherAccount["balance"] + money


while(True):
    printMenu()
    input_text = input("원하시는 서비스를 선택하세요 : ")
    
    clear()

    if input_text == "1":
        addAccount()

    elif input_text =="2":
        transfer()

    elif input_text =="3":
        checkMyBalance()

    elif input_text =="4":
        printAllAccountAddress()

    elif input_text == "0" :
        break

    else:
        print("잘못 입력하셨습니다.")

    input("아무 키나 누르시면 메인으로 돌아갑니다.")
    clear()

print("프로그램이 종료되었습니다.")