#!/usr/bin/env python3

from Bio import SeqIO

# Define o nome do arquivo tabular de entrada
input_file = "Def_Candidatas2.txt"

# Define o nome do arquivo fasta de entrada
fasta_file = "Emiliana_huxleyi.fasta"

# Define o nome do arquivo fasta de saída
output_file = "Def_sequencias.fasta"

# Cria um dicionário para armazenar as sequências do arquivo fasta
sequences_dict = SeqIO.to_dict(SeqIO.parse(fasta_file, "fasta"))

# Abre o arquivo de saída para escrita
with open(output_file, "w") as out_file:
	# Abre o arquivo tabular de entrada para leitura
	with open(input_file, "r") as in_file:
		# Loop sobre as linhas do arquivo tabular
		for line in in_file:
			# Separa a linha em colunas
			columns = line.strip().split("\t")
			# Verifica se a primeira coluna contém um identificador de sequência
			if columns[0] in sequences_dict:
				# Se a sequência está presente no arquivo fasta, salva a sequência no arquivo de saída
				SeqIO.write(sequences_dict[columns[0]], out_file, "fasta")
				
print("Concluído!")
