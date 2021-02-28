#Made by Anjanay Raina

'''
- This is the skeleton code, wherein you have to write the logic for each of the
functions defined below.

- Feel free to add new helper functions, but DO NOT modify/delete the given functions.

- You MUST complete the functions defined below, except the ones that are already defined.
'''
discount={"HELLE25":[25000,25,5000],"CHILL50":[50000,50,10000]}
y=False
d1={0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
d={0:["Tshirt"      , "Apparels"     , 500],1:["Trousers"    , "Apparels"     , 600],2:["Scarf"       , "Apparels"     , 250]
   ,3:["Smartphone"  , "Electronics"  , 20000],4:["iPad"        , "Electronics"  , 30000],5:["Laptop" ,      "Electronics"  , 50000],
   6:["Eggs"        , "Eatables"     , 5],7:["Chocolate"   , "Eatables"     , 10],8:["Juice"       , "Eatables"     , 100],
   9:["Milk"        , "Eatables"     , 45]}
def remove0(n):
    p=[]
    for i in n:
        if i !=0:
            p.append(i)
    return p


def show_menu():
    '''
    Description: Prints the menu as shown in the PDF

    Parameters: No paramters

    Returns: No return value
    '''
    print("""=================================================
                       MY BAZAAR
=================================================
    Hello! Welcome to my grocery store!
    Following are the products available in the shop:

    -------------------------------------------------
    CODE | DESCRIPTION |   CATEGORY   | COST (Rs)
    -------------------------------------------------
      0  | Tshirt      | Apparels     | 500
      1  | Trousers    | Apparels     | 600
      2  | Scarf       | Apparels     | 250
      3  | Smartphone  | Electronics  | 20,000
      4  | iPad        | Electronics  | 30,000
      5  | Laptop      | Electronics  | 50,000
      6  | Eggs        | Eatables     | 5
      7  | Chocolate   | Eatables     | 10
      8  | Juice       | Eatables     | 100
      9  | Milk        | Eatables     | 45
    ------------------------------------------------

Would you like to buy in bulk? (y or Y / n or N):""",end="")




def get_regular_input():
    discount = {"HELLE25": [25000, 25, 5000], "CHILL50": [50000, 50, 10000]}
    y = False
    d1 = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
    d = {0: ["Tshirt", "Apparels", 500], 1: ["Trousers", "Apparels", 600], 2: ["Scarf", "Apparels", 250]
        , 3: ["Smartphone", "Electronics", 20000], 4: ["iPad", "Electronics", 30000],
         5: ["Laptop", "Electronics", 50000],
         6: ["Eggs", "Eatables", 5], 7: ["Chocolate", "Eatables", 10], 8: ["Juice", "Eatables", 100],
         9: ["Milk", "Eatables", 45]}

    def remove0(n):
        p = []
        for i in n:
            if i != 0:
                p.append(i)
        return p

    r=[]
    for i in range(10):
        r.append(0)
    '''
    Description: Takes space separated item codes (only integers allowed).
    Include appropriate print statements to match the output with the
    screenshot provided in the PDF.

    Parameters: No parameters

    Returns: Returns a list of integers of length 10, where the i_th
    element represents the quantity of the item with item code i.
    '''
    print("Enter the item codes (space-separated):",end="")
    n = list(map(int, list(input().split(" "))))
    for i in n:
        if (i<0 or i>9):
            print("One or more value/values were given wrong and they will be discarded")
            continue
        else:
            d1[i]+=1
            r[i]+=1


    return r




def get_bulk_input():
    discount = {"HELLE25": [25000, 25, 5000], "CHILL50": [50000, 50, 10000]}
    y = False
    d1 = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
    d = {0: ["Tshirt", "Apparels", 500], 1: ["Trousers", "Apparels", 600], 2: ["Scarf", "Apparels", 250]
        , 3: ["Smartphone", "Electronics", 20000], 4: ["iPad", "Electronics", 30000],
         5: ["Laptop", "Electronics", 50000],
         6: ["Eggs", "Eatables", 5], 7: ["Chocolate", "Eatables", 10], 8: ["Juice", "Eatables", 100],
         9: ["Milk", "Eatables", 45]}

    def remove0(n):
        p = []
        for i in n:
            if i != 0:
                p.append(i)
        return p

    '''
    Description: Takes inputs (only integers allowed) from a bulk buyer.
    For details, refer PDF. Include appropriate print statements to match
    the output with the screenshot provided in the PDF.

    Parameters: No parameters

    Returns: Returns a list of integers of length 10, where the i_th
    element represents the quantity of the item with item code i.
    '''
    r=[]
    for i in range(10):
        r.append(0)
    p=[]
    while True:
        print("Enter code and quantity (leave blank to stop):", end="")

        n=input()


        if(n==""):
            print("Your order has been finalized.")
            return r
        n = list(n.split())
        n = list(map(int, n))

        if((n[1])<0):
            print("Invalid quantity. Try again.")
            continue
        if((n[0])<0 or (n[0])>9):
            print("Invalid quantity. Try again.")
            continue

        else:

            print(f"You added {n[1]} {d[n[0]][0]}")
            d1[n[0]]+=n[1]
            r[n[0]]+=n[1]






def print_order_details(n):

    discount = {"HELLE25": [25000, 25, 5000], "CHILL50": [50000, 50, 10000]}
    y = False
    d1 = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
    d = {0: ["Tshirt", "Apparels", 500], 1: ["Trousers", "Apparels", 600], 2: ["Scarf", "Apparels", 250]
        , 3: ["Smartphone", "Electronics", 20000], 4: ["iPad", "Electronics", 30000],
         5: ["Laptop", "Electronics", 50000],
         6: ["Eggs", "Eatables", 5], 7: ["Chocolate", "Eatables", 10], 8: ["Juice", "Eatables", 100],
         9: ["Milk", "Eatables", 45]}

    def remove0(n):
        p = []
        for i in n:
            if i != 0:
                p.append(i)
        return p
    '''
    Description: Prints the details of the order in a manner similar to the
    sample given in PDF.

    Parameters: Takes a list of integers of length 10, where the i_th
    element represents the quantity of the item with item code i.

    Returns: No return value
    '''
    k=0
    for i in n:
        d1[k]=i
        k+=1
    print("""-------------------------------------------------
    ORDER DETAILS
    -------------------------------------------------""")
    k=0
    p=n
    p=remove0(p)
    for i in range(10):
        if(d1[i]!=0):
            print(f"[{k}] {d[i][0]}*{d1[i]}=Rs{d[i][2]}*{d1[i]}=Rs{d[i][2] * d1[i]}")
            k += 1





def calculate_category_wise_cost(quantities):
    '''
    Description: Calculates the category wise cost using the quantities
    provided. Include appropriate print statements to match the output with the
    screenshot provided in the PDF.

    Parameters: Takes a list of integers of length 10, where the i_th
    element represents the quantity of the item with item code i.

    Returns: A 3-tuple of integers in the following format:
    (apparels_cost, electronics_cost, eatables_cost)
    '''
    discount = {"HELLE25": [25000, 25, 5000], "CHILL50": [50000, 50, 10000]}
    y = False
    d1 = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
    d = {0: ["Tshirt", "Apparels", 500], 1: ["Trousers", "Apparels", 600], 2: ["Scarf", "Apparels", 250]
        , 3: ["Smartphone", "Electronics", 20000], 4: ["iPad", "Electronics", 30000],
         5: ["Laptop", "Electronics", 50000],
         6: ["Eggs", "Eatables", 5], 7: ["Chocolate", "Eatables", 10], 8: ["Juice", "Eatables", 100],
         9: ["Milk", "Eatables", 45]}

    def remove0(n):
        p = []
        for i in n:
            if i != 0:
                p.append(i)
        return p
    n=quantities

    k=0
    for i in n:
        d1[k]=i
        k+=1
    print("""-------------------------------------------------
           CATEGORY-WISE COST
-------------------------------------------------""")

    suma = 0
    sume = 0
    sumeat = 0
    k = 0
    for i in range(10):
        if (i < 3):
            suma += d[i][2] * d1[i]
        if (i >= 3 and i < 6):
            sume += d[i][2] * d1[i]
        if (i >= 6 and i < 10):
            sumeat += d[i][2] * d1[i]

    print("Apparels = Rs", suma)

    print("Electronics = Rs", sume)

    print("Eatables = Rs", sumeat)

    apparels_cost, electronics_cost, eatables_cost=suma,sume,sumeat
    return (int(apparels_cost), int(electronics_cost), int(eatables_cost))



def get_discount(cost, discount_rate):
    '''
    Description: This is a helper function. DO NOT CHANGE THIS.
    This function must be used whenever you are calculating discounts.

    Parameters: Takes 2 parameters:
    - cost: Integer
    - discount_rate: Float: 0 <= discount_rate <= 1

    Returns: The discount on the cost provided.
    '''
    return int(cost * discount_rate)


def calculate_discounted_prices(apparels_cost, electronics_cost, eatables_cost):
    discount = {"HELLE25": [25000, 25, 5000], "CHILL50": [50000, 50, 10000]}
    y = False
    d1 = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
    d = {0: ["Tshirt", "Apparels", 500], 1: ["Trousers", "Apparels", 600], 2: ["Scarf", "Apparels", 250]
        , 3: ["Smartphone", "Electronics", 20000], 4: ["iPad", "Electronics", 30000],
         5: ["Laptop", "Electronics", 50000],
         6: ["Eggs", "Eatables", 5], 7: ["Chocolate", "Eatables", 10], 8: ["Juice", "Eatables", 100],
         9: ["Milk", "Eatables", 45]}

    def remove0(n):
        p = []
        for i in n:
            if i != 0:
                p.append(i)
        return p
    '''
    Description: Calculates the discounted category-wise price, if applicable.
    Include appropriate print statements to match the output with the
    screenshot provided in the PDF.

    Parameters: Takes 3 integer parameters:
    - apparels_cost: 	cost for the category 'Apparels'
    - electronics_cost: cost for the category 'Electronics'
    - eatables_cost: 	cost for the category 'Eatables'

    Returns: A 3-tuple of integers in the following format:
    (discounted_apparels_cost, discounted_electronics_cost, discounted_eatables_cost).
    '''
    print("""-------------------------------------------------
        DISCOUNTS
-------------------------------------------------""")
    dis1 = apparels_cost
    dis2 = electronics_cost
    dis3 = eatables_cost

    if (apparels_cost >= 2000):
        print(f"[APPAREL] Rs {apparels_cost} - Rs {(apparels_cost) / 10} = Rs {9 * (apparels_cost) / 10}")
        apparels_cost = 9 * (apparels_cost) / 10

    if (electronics_cost >= 25000):
        print(f"[ELECTRONICS] Rs {electronics_cost} - Rs {(electronics_cost) / 10} = Rs {9 * (electronics_cost) / 10}")
        electronics_cost = 0.9 * (electronics_cost)

    if (eatables_cost >= 500):
        print(f"[EATABLES] Rs {eatables_cost} - Rs {(eatables_cost) / 10} = Rs {9 * (eatables_cost) / 10}")
        eatables_cost = 0.9 * (eatables_cost)

    print(f"TOTAL DISCOUNT = Rs {(dis1 - apparels_cost) + (dis2 - electronics_cost) + (dis3 - eatables_cost)}")
    print(f"TOTAL COST = Rs {((apparels_cost) + (electronics_cost) + (eatables_cost))}")
    return (int(apparels_cost), int(electronics_cost), int(eatables_cost))




def get_tax(cost, tax):
    '''
    Description: This is a helper function. DO NOT CHANGE THIS.
    This function must be used whenever you are calculating discounts.

    Parameters: Takes 2 parameters:
    - cost: Integer
    - tax: 	Float: 0 <= tax <= 1

    Returns: The tax on the cost provided.
    '''
    return int(cost * tax)


def calculate_tax(apparels_cost, electronics_cost, eatables_cost):
    discount = {"HELLE25": [25000, 25, 5000], "CHILL50": [50000, 50, 10000]}
    y = False
    d1 = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
    d = {0: ["Tshirt", "Apparels", 500], 1: ["Trousers", "Apparels", 600], 2: ["Scarf", "Apparels", 250]
        , 3: ["Smartphone", "Electronics", 20000], 4: ["iPad", "Electronics", 30000],
         5: ["Laptop", "Electronics", 50000],
         6: ["Eggs", "Eatables", 5], 7: ["Chocolate", "Eatables", 10], 8: ["Juice", "Eatables", 100],
         9: ["Milk", "Eatables", 45]}

    def remove0(n):
        p = []
        for i in n:
            if i != 0:
                p.append(i)
        return p
    '''
    Description: Calculates the total cost including taxes.
    Include appropriate print statements to match the output with the
    screenshot provided in the PDF.

    Parameters: Takes 3 integer parameters:
    - apparels_cost: 	cost for the category 'Apparels'
    - electronics_cost: cost for the category 'Electronics'
    - eatables_cost: 	cost for the category 'Eatables'

    Returns: A 2-tuple of integers in the following format:
    (total_cost_including_tax, total_tax)
    '''
    dis1 = apparels_cost
    dis2 = electronics_cost
    dis3 = eatables_cost
    print("""-------------------------------------------------
    TAX
-------------------------------------------------""")

    print(f"[APPAREL] Rs {apparels_cost} * 0.1= Rs {11 * (apparels_cost) / 10}")
    apparels_cost = 11 * (apparels_cost) / 10

    print(f"[ELECTRONICS] Rs {electronics_cost} * 0.15 = Rs {11.5 * (electronics_cost) / 10}")
    electronics_cost = 11.5 * (electronics_cost) / 10

    print(f"[EATABLES] Rs {eatables_cost} * 0.05 = Rs {10.05 * (eatables_cost) / 10}")
    eatables_cost = 10.5 * (eatables_cost) / 10

    print(f"TOTAL TAX = Rs {(-dis1 + apparels_cost) + (-dis2 + electronics_cost) + (-dis3 + eatables_cost)}")
    (-dis1 + apparels_cost) + (-dis2 + electronics_cost) + (-dis3 + eatables_cost)
    print(f"TOTAL COST = Rs {((apparels_cost) + (electronics_cost) + (eatables_cost))}")

    total_cost_including_tax = (apparels_cost) + (electronics_cost) + (eatables_cost)

    total_tax = (-dis1 + apparels_cost) + (-dis2 + electronics_cost) + (-dis3 + eatables_cost)



    return (int(total_cost_including_tax), int(total_tax))




def apply_coupon_code(total_cost):
    discount = {"HELLE25": [25000, 25, 5000], "CHILL50": [50000, 50, 10000]}

    d1 = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
    d = {0: ["Tshirt", "Apparels", 500], 1: ["Trousers", "Apparels", 600], 2: ["Scarf", "Apparels", 250]
        , 3: ["Smartphone", "Electronics", 20000], 4: ["iPad", "Electronics", 30000],
         5: ["Laptop", "Electronics", 50000],
         6: ["Eggs", "Eatables", 5], 7: ["Chocolate", "Eatables", 10], 8: ["Juice", "Eatables", 100],
         9: ["Milk", "Eatables", 45]}

    def remove0(n):
        p = []
        for i in n:
            if i != 0:
                p.append(i)
        return p

    '''
    Description: Takes the coupon code from the user as input (case-sensitive).
    For details, refer the PDF. Include appropriate print statements to match
    the output with the screenshot provided in the PDF.

    Parameters: The total cost (integer) on which the coupon is to be applied.

    Returns: A 2-tuple of integers:
    (total_cost_after_coupon_discount, total_coupon_discount)
    '''
    print("""-------------------------------------------------
    COUPON CODE
-------------------------------------------------""")
    dis1 = 0
    while True:
        n = input("Enter Coupon Code(else leave blank):")
        if (n == "HELLE25"):
            if (total_cost >= discount["HELLE25"][0]):
                if (0.25 * (total_cost) >= 5000):
                    total_cost = total_cost - 5000
                    dis1 = 5000

                else:
                    total_cost = total_cost - 0.25 * (total_cost)
                    dis1 = 0.25 * (total_cost)

                break
            else:
                print("Invalid coupon code. Try again.")
                continue

        elif (n == "CHILL50"):
            if (total_cost >= discount["CHILL50"][0]):
                if (0.5 * (total_cost) >= 10000):
                    total_cost = total_cost - 10000
                    dis1 = 10000

                else:
                    total_cost = total_cost - 0.5 * (total_cost)
                    dis1 = 0.5 * (total_cost)
                break
            else:
                print("Invalid coupon code. Try again.")
                continue

        elif n == "":
            print("No Coupon Code applied.")
            break


        else:
            print("Invalid Coupon Code , please try again")
            continue
    print(f"TOTAL DISCOUNT = Rs {dis1}")
    print(f"TOTAL COST = Rs {total_cost}")
    return (int(total_cost), int(dis1))




def main():
    '''
    Description: This is the main function. All production level codes usually
    have this function. This function will call the functions you have written
    above to design the logic. You will see how splitting your code into specialised
    functions makes the code easier to read, write and debug. Include appropriate
    print statements to match the output with the screenshots provided in the PDF.

    Parameters: No parameters

    Returns: No return value
    '''
    show_menu()
    global y

    while True:
        n = input()
        n.lower()
        if (n == 'y'):
            y=True
            x= get_bulk_input()
            break


        elif (n == 'n'):
            x=get_regular_input()
            break

        else:
            print("Please enter correct input!!")
    print_order_details(x)
    x,y,z= calculate_category_wise_cost(x)
    x,y=calculate_tax(x,y,z)
    apply_coupon_code(x)






if __name__ == '__main__':
	main()