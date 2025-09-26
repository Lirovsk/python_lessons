file = open("C:\\Users\\Arauj\\Documents\\Vscode\\python_lessons\\manipulating files\\test.txt", "r")
i=0

# This lçine will search for the letter v in the file and print the line number and the line itself
# Essa linha vai procurar a letra v no arquivo e imprimir o número da linha e a própria linha
for line in file.readlines():
    i+=1
    if "v" in line.lower():
        print(f"v is in the line {i}: {line}")
    