def selecter(firsttext, selecttext, amount):
    if firsttext:
        print(firsttext)
    if selecttext:
        print(selecttext)
    while True:
        try:
            num = int(input("> "))
            if 0 <= num <= amount:
                break
        except ValueError:
            pass
        print("入力が無効")
    return num
