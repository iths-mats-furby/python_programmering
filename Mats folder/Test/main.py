def smallest(list):
    small= list[0]
    for i in list:
        if i<small:
            small=i
    return small

def main():
    print("I'm in the main method")

list=[3, 9, 7, 3, 6, 5, 7, 24, 6]
#list
print("smallest in ",list,"is")
print(smallest(list))

if __name__ == "__main__":
    main() # call on the main function