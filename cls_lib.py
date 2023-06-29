class multiple_function():

    def bmi():
        BMI = int(input('Enter the BMI Index: '))
        if BMI <= 18.4 :
            print('Under Weight')

        elif BMI <= 24.9 :
            print('healthy')
        elif BMI <= 29.9:
            print('over weight')
        else  :
            print('very over weight')
    
    def sub ():
        subfields_1 = ("Sub-fields in AI are:","Machine Learning","Neural Networks","Vision","Robotic","speech Processing",
                 "Natural Language Processing")

        for temp_1 in subfields_1:
            print(temp_1)
        
    def oddeven():
        num = int(input("Enter a number:"))
        if num % 2 ==0 :
            print(num,"is even number")
        else:
            print(num,"is odd number")
    
    def eligible ():
        s = input("gender:")
        gender = s.upper()
        age = int(input("your age :"))
        if age >= 27 and gender == "MALE":
            print("ELIGIBLE")
        elif age >= 24 and gender =="FEMALE":
            print("ELIGIBLE")
        else:
            print("NOT EILGIBLE")

    def percentage ():
        sub_1 = int(input("subject1="))
        sub_2 = int(input("subject2="))
        sub_3 = int(input("subject3="))
        sub_4 = int(input("subject4="))
        sub_5 = int(input("subject5="))
        total = sub_1+sub_2+sub_3+sub_4+sub_5

        percent = (total/500)*100
        print("Total:",total)
        print("percentage=",percent)

    def triangle():
        height = int(input("height:"))
        breadth = int(input("breadth:"))
        area_formula = ((height*breadth)/2)
        area_of_triangle = area_formula
        print("area formula = ((height*breadth)/2)")
        print("area of triangle:",area_formula)
        height_1 = int(input("height1:"))
        height_2 = int(input("height2:"))
        breadth_1 = int(input("breadth1:"))
        perimeter = height_1+height_2+breadth_1
        print("perimeter = height_1+height_2+breadth_1")
        print("perimeter of triangle:",perimeter)