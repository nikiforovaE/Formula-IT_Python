capacity_mb = 1.44
pages_in_book = 100
str_in_page = 50
sym_in_str = 25
b_on_sym = 4
print("Количество книг, помещающихся на дискету:",
      round(capacity_mb * 1024 * 1024 // (pages_in_book * str_in_page * sym_in_str * b_on_sym)))
