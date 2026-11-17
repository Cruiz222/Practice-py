def data_translator():
    while True:
        data = input("\nEnter data:\n").strip()

        print(f"Original data: {data} | Type: {type(data)}")
        print(f"As string: {str(data)}")

        try:
            point = float(data)
            print(f"As float: {point} | Type: {type(point)}")

            num = int(point)
            print(f"As integer: {num} | Type: {type(num)}")

            binary = bin(num)
            print(f"As binary: {binary} | Type: {type(binary)}")

        except ValueError:
            print("Conversion failed: input is not a valid number.")

        again = input("\nDo you want to try again? (Yes/No):\n").strip().lower()
        if again not in ("yes", "y"):
            print("Goodbye!")
            break

data_translator()
