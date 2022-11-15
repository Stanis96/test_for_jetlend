import pandas as pd

filename = "test.xlsx"
df = pd.read_excel(filename)


def handle_excel():
    df["registration_date"] = pd.to_datetime(df["registration_date"], format="%Y-%m-%d")
    find_date = df[df["registration_date"] <= "2021-12-31"]
    sum_amount = find_date["amount"].sum()
    print(f"Сумма всех займов для компаний, зарегистрированных не позднее 2021 года:{sum_amount}\n")

    print("Сумма займов для каждого из рейтингов:")

    rating_sum = df.groupby(["rating"]).agg(sum=("amount", "sum"))
    print(rating_sum)


if __name__ == "__main__":
    handle_excel()
