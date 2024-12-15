# Лабораторная работа 1-2
# Иванов Никита
from typing import List
import csv
import numpy as np
from mathstats import MathStats
import matplotlib.pyplot as plt
from datetime import datetime

FILE = 'Retail.csv'
FILE2 = 'MarketingSpend.csv'


def main():
    # запускающая функция
    data = read_data(FILE)

    # Проверка значений
    c = count_invoice(data[:5])
    print(f'Всего инвойсов (invoices): {c}')  # 2
    c = count_invoice(data[:11])
    print(f'Всего инвойсов (invoices): {c}')  # 5
    c = count_invoice(data)
    print(f'Всего инвойсов (invoices): {c}')  # 16522

    # Пример проверки работы с классом MathStats
    data2 = MathStats(FILE2)
    slice_test1 = data2.data[:2]  # первые две строки данных
    slice_test2 = data2.data[::]  # слайс со всеми данными
    print(len(slice_test2))

    # Пример работы функций get_mean
    print(data2.get_mean(slice_test1))  # (4500.0, 2952.43)
    print(data2.get_mean(slice_test2))
    plot_marketing_spend(FILE2)


def read_data(file: str) -> List[dict]:
    """
        считывание данных и возвращение значений в виде списка из словарей
        """
    data = []
    with open(file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for _r in reader:
            row = _r
            data.append(row)
    return data


def count_invoice(data: List[dict]) -> int:
    """
        Подсчет количества различных инвойсов в списке
        """
    invoices = [el['InvoiceNo'] for el in data]  # Генератор списка
    count = len(set(invoices))
    return count


def count_different_values(data: List[dict], key: str) -> int:
    """
        Функция должна возвращать число различных значений для столбца key в списке data

        key - InvoiceNo или InvoiceDate или StockCode
        """
    values = [el[key] for el in data]  # Генератор списка
    count = len(set(values))
    return count


def get_total_quantity(data: List[dict], stock_code: str) -> int:
    """
        Возвращает общее количество проданного товара для данного stock_code
        """
    total_quantity = sum(
        [el['Quantity'] for el in data if el['StockCode'] == stock_code])
    return total_quantity


def plot_marketing_spend(filename):
    data = read_data(filename)
    monthly = monthly_sum(data)

    fig, ax = plt.subplots(figsize=(9.2, 5))
    ax.invert_yaxis()

    for m in monthly:
        off = ax.barh(m["Month"],
                      m["Offline Spend"],
                      left=0,
                      label="Offline Spend",
                      color="g")
        on = ax.barh(m["Month"],
                     m["Online Spend"],
                     left=m["Offline Spend"],
                     label="Online Spend",
                     color="c")
        ax.bar_label(off, label_type='center', color='k')
        ax.bar_label(on, label_type='center', color='k')

    for i, m in enumerate(monthly):
        total = m["Offline Spend"] + m["Online Spend"]
        ax.text(total + 10,
                i + 1.1,
                round(total),
                ha='center',
                weight='bold',
                color='black')

    plt.xlabel("Spend")
    plt.xticks()
    plt.ylabel("Month")
    plt.yticks(list(range(1, 13)))
    plt.title("Online and Offline Spending")

    ax.legend(["Offline Spend", "Online Spend"])
    plt.show()


def sum_by_month(data, month):
    offline = 0
    online = 0
    for d in data:
        c = datetime.strptime(d["InvoiceDate"], "%Y-%m-%d")
        if c.month == month:
            offline += int(d["Offline Spend"])
            online += int(d["Online Spend"])
    return offline, online


def monthly_sum(data):
    months = []

    for i in range(1, 13):
        off, on = sum_by_month(data, i)
        months.append({"Month": i, "Offline Spend": off, "Online Spend": on})

    months = sorted(months, key=lambda x: x["Month"])
    return months


if __name__ == "__main__":
    main()
