import re

PATTERN = r"^P"

if re.match(PATTERN, "Peter"):
    print("Match")
else:
    print("No Match")

# sempre que possivel evite o uso de regex, dada sua complexidade e dificuldade de manutencao/explicacao para outras pessoas

# veja um exemplo de como evitar regex em um caso simples

if "Peter".startswith("P"):
    print("Match")
else:
    print("No Match")
    
# mais simples, mais facil de entender e manter, sem uso de nenhuma biblioteca externa
# a mesma funcionalidade, de maneira mais simples