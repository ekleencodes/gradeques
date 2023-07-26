def grade_criteria(marks):
    if marks >= 90:
        return "A+"
    elif 80 <= marks < 90:
        return "A"
    elif 70 <= marks < 80:
        return "B"
    elif 60 <= marks < 70:
        return "C"
    elif 50 <= marks < 60:
        return "D"
    else:
        return "FAIL"
def valid():
    while True:
        try:
            marks=float(input("Enter marks"))
            if 0 <= marks <= 100:
                return marks
            else:
                print("Marks should be between 0-100")
        except ValueError:
            print("Invalid input")
def main():
    while True:
        marks=valid()
        grade=grade_criteria(marks)
        print(f"Grade: {grade}")
        choice=input("Another students grade(y/n)")
        if choice.lower() != 'y':
            print("Done")
            break
if __name__=="__main__":
    main()