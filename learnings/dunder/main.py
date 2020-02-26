from account import Account


def validate_transaction(acc, amount_to_add):
    with acc as a:
        print(f"Adding {amount_to_add} to account")
        a.add_transaction(amount_to_add)
        print(f"New balance would be : {a.balance}")
        if a.balance < 0:
            raise ValueError("Cannot have negative balance")


def main():
    acc = Account('bob', 10)
    acc.add_transaction(20)
    acc.add_transaction(-10)
    acc.add_transaction(50)
    acc.add_transaction(-20)
    acc.add_transaction(30)

    print(acc.balance)

    print(len(acc))

    print(acc[1])

    print(reversed(acc))

    acc2 = Account('tim', 100)
    acc2.add_transaction(20)
    acc2.add_transaction(40)

    print(acc2.balance)

    print(acc2 < acc)
    print(acc2 > acc)
    print(acc2 == acc)

    acc3 = acc2 + acc

    print(acc3)
    print(acc3.amount)
    print(acc3.balance)

    acc3()

    acc4 = Account('sue', 10)
    print(f"Balance start: {acc4.balance}")
    validate_transaction(acc4, 20)
    print(f"Balance now: {acc4.balance}")

    try:
        validate_transaction(acc4, -50)
    except ValueError as exc:
        print(exc)

    print(f"Balance end: {acc4.balance}")


if __name__ == "__main__":
    main()
