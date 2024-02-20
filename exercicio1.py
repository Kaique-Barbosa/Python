# crie um app pyton:
#  Nome= isadora
#  sal_bruto = 8756
#  ir = 8% do sal_ bruto
#  inss = 5% do sal bruto
#   salario liquido = sal bruto - ir - inss

nome = "kaique" 
salario_bruto = 8756
inposto_do_anor = 0.08 * salario_bruto
inposto_De_velhice = 0.05 * salario_bruto

salario_liquido = salario_bruto - inposto_do_anor - inposto_De_velhice

print(f"OLá {nome}. O seu salario liquido é de: {salario_liquido:.2f} ")