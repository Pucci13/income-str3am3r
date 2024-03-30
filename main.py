def calculate_total(income, expense):
    return income - expense

if __name__ == '__main__':
    salary = int(input("Please imput your salary (monthly): "))
    rent = int(input("How much u spend on rent: "))
    print("You make around " + str(calculate_total(salary, rent)) + " a month")
    if calculate_total(salary, rent) > 1000:
        print("You kinda making bank ngl, keep up the drip my g")

