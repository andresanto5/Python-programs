#!/usr/bin/env python3

# Bibliotecas necessárias
import pandas as pd

# Lista para armazenar os nomes das proteínas e suas sequências
names = []
sequences = []

# Abra o arquivo FASTA
with open("file.fasta", "r") as file:
	# Variável para armazenar a sequência atual
	seq = ""
	# Loop através de cada linha do arquivo
	for line in file:
		# Verifique se a linha atual começa com ">"
		if line.startswith(">"):
			# Se já houver uma sequência armazenada, adicione o nome da proteína e a sequência às listas
			if seq:
				names.append(name)
				sequences.append(seq)
				seq = ""
			# Armazene o nome da proteína
			name = line[1:].strip()
		# Caso contrário, adicione a linha à sequência
		else:
			seq += line.strip()
	# Adicione a última sequência às listas
	names.append(name)
	sequences.append(seq)
	
# Crie um dataframe com as informações
df = pd.DataFrame({"Sequence": sequences, "Protein": names})

# Salve o dataframe como um arquivo CSV
df.to_csv("fasta_table.csv", index=False)
