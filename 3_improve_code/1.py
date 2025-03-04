def read_sales_data(file1, file2):
    with open(file1) as f:
        sales_h1 = f.read().splitlines()
    with open(file2) as f:
        sales_h2 = f.read().splitlines()
    return sales_h1, sales_h2

def amount_total_avg(sales_h1, sales_h2):
    sales = sales_h1 + sales_h2
    sales_amounts = []
    for s in sales:
        amount_str = s.split(':')[1]
        amount = int(amount_str.replace(",", ""))
        sales_amounts.append(amount)
    total = sum(sales_amounts)
    avg = total / len(sales_amounts)
    return total, avg

def write_sales_data(total, avg, output):
    with open(output, 'w') as f:
        f.write(f"売上合計: {total:,}\n")
        f.write(f"売上平均: {avg:,}\n")

def main():
    input_1 = "./1_data/月別売上_2024年上半期.txt"
    input_2 = "./1_data/月別売上_2024年下半期.txt"
    output  = "./1_data/年間売上_2024年.txt"
    sales_h1, sales_h2 = read_sales_data(input_1, input_2)
    total, avg = amount_total_avg(sales_h1, sales_h2)
    write_sales_data(total, avg, output)

if __name__ == '__main__':
    main()