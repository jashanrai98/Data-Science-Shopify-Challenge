def find_average_order_value(filename):
    df = pd.read_csv(filename)
    order_amount_column = df["order_amount"]
    order_quantity_column = df["total_items"]
    i = 0
    total_consumer_cost = 0
    total_business_cost = 0
    number_of_rows_in_consumer_orders = 0
    number_of_rows_in_business_orders = 0
    maximum_number_of_sneakers_direct_to_consumer = 10
    for row in order_quantity_column:
        if row < maximum_number_of_sneakers_direct_to_consumer:
            total_consumer_cost = total_consumer_cost + order_amount_column[i]
            number_of_rows_in_consumer_orders = number_of_rows_in_consumer_orders + 1
        else:
            total_business_cost = total_business_cost + order_amount_column[i]
            number_of_rows_in_business_orders = number_of_rows_in_business_orders + 1
        i = i + 1
    print(round((total_consumer_cost / number_of_rows_in_consumer_orders), 2))
    print(round((total_business_cost / number_of_rows_in_business_orders), 2))
