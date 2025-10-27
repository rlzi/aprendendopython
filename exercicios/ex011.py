larg = float(input("\033[92mDigite a Largura da Parede: \033[0m"))
alt = float(input("\033[92mDigite a Altura da Parede: \033[0m"))
area = larg * alt
print(f"Sua Parede Tem Dimensao de {larg} x {alt} e sua Area e De {area}m2")
tinta = area / 2
print(f"Para Pintar essa Parede, voce precisara de {tinta}L de tinta")