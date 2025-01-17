def mask_account_card(account_number: str) -> None:

    numbers = ""
    letters = ""
    for number in account_number:
        if number.isdigit():
            numbers += number
        elif not number.isdigit():
            letters += number
    if letters == "Счет ":
        mask_numbers = f"**{numbers[-4:]}"
    elif letters != "Счет ":
        mask_numbers = f"{numbers[:4]} {numbers[4:6]}** **** {numbers[-4:]}"

    return letters + mask_numbers


def get_date(data: str) -> None:

    new_data = f"{data[8:10]}.{data[5:7]}.{data[0:4]}"
    return new_data


print(mask_account_card(str(input("Введите номер или счет: "))))
print(get_date("2024-03-11T02:26:18.671407"))
