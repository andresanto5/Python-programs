#!/usr/bin/env python3

# Importa o módulo BioPython
from Bio import SeqIO

# Define o nome do arquivo multifasta
input_file = "representatives.fasta"

# Pede ao usuário para informar o número máximo de sequências por arquivo
max_seqs_per_file = int(input("Informe o número máximo de sequências por arquivo: "))

# Lê o arquivo multifasta e separa as sequências em listas de tamanho máximo igual a max_seqs_per_file
records = []
i = 1
for record in SeqIO.parse(input_file, "fasta"):
	records.append(record)
	if i % max_seqs_per_file == 0:
		output_file = f"arquivo_{i//max_seqs_per_file}.fasta"
		SeqIO.write(records, output_file, "fasta")
		records = []
	i += 1
	
# Escreve as últimas sequências no último arquivo, se houver
if len(records) > 0:
	output_file = f"arquivo_{i//max_seqs_per_file + 1}.fasta"
	SeqIO.write(records, output_file, "fasta")
	
print("Processo concluído!")
