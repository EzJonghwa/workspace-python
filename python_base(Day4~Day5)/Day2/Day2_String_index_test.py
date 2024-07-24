# #@ 이전의 닉네임,도메인 받아내기
# e_mail= input("이메일을 입력해주세요: ")
# print("닉네임은:"+ e_mail[:e_mail.find('@')])
# print("도메인은:"+ e_mail[e_mail.find('@')+1:])
# abc = e_mail
# print(abc) 

e_mail= input("이메일을 입력해주세요: ")
abc = e_mail.find('@')
print("닉네임은:"+ e_mail[:abc])
print("도메인은:"+ e_mail[abc+1:])

