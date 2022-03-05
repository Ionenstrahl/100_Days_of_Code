from prettytable import PrettyTable

table = PrettyTable()
table.field_names = ["Pokemon", "Type 1", "Type 2"]
table.add_row(["Enton", "Water", ""])
table.add_row(["Nidoking", "Ground", "Poison"])
table.add_row(["Lohgock", "Fire", "Fight"])
table.add_row(["Menki", "Fight", ""])
# table.add_column("Pokemon", ["Pikachu", "Squirtle", "Charmander"])
table.align = "l"

print(table)

