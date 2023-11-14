print("すべての質問に y または n で答えてください")
has_money = input("お金に余裕はありますか？ >>")
if has_money == "y":
    is_hungry = input("お腹がすごく空いてますか？>>")
    is_drink = input("ビールを飲みたいですか？>>")

    if  is_hungry == "y" and is_drink == "y":
        print("焼肉はいかがですか")
    elif  is_hungry == "y":
        print("カレーはいかがですか")
    elif is_drink == "y":
        print("焼き鳥はいかがですか")
    else:
        print("パスタはいかがですか")
    is_snack = input("夜食は必要ですか？>>")

    if is_snack == "y":
        print("コンビニのチキンはいかがですか")
    else:
        print("家で食べましょう")