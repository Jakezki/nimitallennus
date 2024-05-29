def save_user_data(name, age, filename='user_data.txt'):
    with open(filename, 'a') as file:
        file.write(f"Name: {name}, Age: {age}\n")

def main():
    name = input("Nimesi: ")
    age = input("Ikäsi: ")
    save_user_data(name, age)
    print("Tallennettu onnistuneesti.")

if __name__ == "__main__":
    main()
