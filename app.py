import random as rd

if __name__ == "__main__":
    reslt_fortune = ["大凶","凶","末吉","小吉","中吉","吉","大吉"]

    print(f"今日の運勢は. . . {rd.choice(reslt_fortune)}")