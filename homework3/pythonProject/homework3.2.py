test_result:int=int(input("enter the test result:"))
if 0<= test_result<=40:
    print("try harder next time")
elif 41<=test_result<=60:
    print("you're getting there, need some more work")
elif 61<=test_result<=80:
    print("pretty good")
elif 81<=test_result<=95:
    print("awesome")
elif 96<=test_result<=100:
    print("excellent! you're a star")
else:
    print("illegal grade")