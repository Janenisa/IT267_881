from cusorder import customer,order #รียกแพคเกจกับโมดูล

cus = customer.Customer("Jame", "Nonthaburi")
ord = order.Order("15-06-2022","packed")

print(f'Order of {cus.cus_name} on {ord.date} is {ord.status}')