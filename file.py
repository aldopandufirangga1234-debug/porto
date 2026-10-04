def write_log(massage):
    with open("output.txt", "a") as file:
        file.write(massage + "\n")

write_log("hallo")