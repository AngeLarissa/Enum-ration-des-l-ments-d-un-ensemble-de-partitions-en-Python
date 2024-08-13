def decimal_to_binary(number: int):
    binary_num = bin(number)
    binary_num = binary_num[2:]
    return binary_num

def binary_to_decimal(binary_num: str):
    decimal = int(binary_num, 2)
    return decimal

def generate_list(lenght):
    elements_list = []
    for i in range(lenght+1):
        elements_list.append(i)
    return elements_list

def position_to_element(elements_list, lenght: int, position: int):
    if(position <= 2**lenght and position>0):
        position -= 1
        binary_num = decimal_to_binary(position)
        element=[]
        j = lenght
        for i in range(len(binary_num)-1, -1,-1):
            if(binary_num[i]=="1"):
                element.insert(0, elements_list[j])
            j -= 1
        element = tuple(element)
        return element
    else:
        return "POSITION INVALIDE"

def element_to_position(elements_list, lenght, element):
    binary_num = ""
    for i in element:
        if not i in elements_list:
            return f"BAD ELEMENT: {i} not present in the general set.\n"
    for i in elements_list:
        if i in element:
            binary_num += "1"
        else:
            binary_num += "0"
    return binary_to_decimal(binary_num)+1

def main():
    choice = 1
    while choice != 0:
        print("""
        press 0 TO QUIT.
              1 to have THE POSITION of an element.
              2 to give an element and have its position.
        """)
        choice = int(input("Your choice: >  "))
        if choice and 0<choice<3:
            lenght = int(input("\nEnter the set lenght: "))
            elements_list = generate_list(lenght)
        match choice:
            case 0: break
            case 1:
                position = int(input("\nEnter the element's position in the whole p-partition set:  "))
                if(position <= 2**lenght and position>0):
                    print(f"\nThe Element at position {position} is: {position_to_element(elements_list, lenght, position)}\n")
                else:
                    print("\nTHIS POSITION IS INVALID!!!!\n")
            case 2:
                element = []
                num = int(input("How many numbers has the element: "))
                for i in range(num):
                    element.append(int(input(f"Enter number {i+1}: ")))
                position = element_to_position(elements_list, lenght, element)
                if str(position)[0] == "B":
                    print("\n", position)

                    print(f"The element {element} is at position {position} in the general set")
        
   

main()
