#(1)
#initial == "K"

#(2)
# 80 <= point <= 256

#(3)
# bmi < 20  or bmi > 25

#(4)
# year % 4 == 0

#(5)
# day not 28  and day not 30 and day not 31
# day != 28 and 30 and 31
# not(day in(28,30,31))

#3-3
# #(1)
# isError = False
# n = 0
# if isError == False and n < 100:
#     print("なにかしら表示")

# #(2)
# num = int(input("数字を入力してください>>"))
# if num % 2 == 0:
#     print("割り切れるので偶数です")
# else:
#     print("割り切れないので奇数です")

# #(3)
# talk = input("文字を入力してください")
# if talk == "こんにちは":
#     print("ようこそ!")
# elif talk == "景気は？":
#     print("ぼちぼちです")
# elif talk == "さようなら":
#     print("お元気で!") 
# else :
#     print("どうしました?")

#3-4

month = int(input("今は何月ですか？(数字を入力)>>"))
if month in [1,3,5,7,8,10,12]:
    print("31日までありますね")
else:
    if month != 2:
        print("30日までですね")
    else:
        print("1年で一番寒い月ですね")
    print("年が明けてから")
print("{}か月が過ぎました".format(month))
