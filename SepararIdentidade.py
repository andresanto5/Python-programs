#!/usr/bin/env python3

from Bio import SeqIO
import math

# Define o nome do arquivo multifasta de entrada
arquivo = "representatives1.fasta"

# Define o número de sequências que cada arquivo de saída deve ter (arredondado para cima)
num_seq_por_arquivo = math.ceil(len(list(SeqIO.parse(arquivo, "fasta"))) / 2)

# Define os nomes dos arquivos de saída
arquivo_saida1 = "arquivo_saida1.fasta"
arquivo_saida2 = "arquivo_saida2.fasta"

# Abre os arquivos de saída e grava as sequências correspondentes
with open(arquivo_saida1, "w") as output1, open(arquivo_saida2, "w") as output2:
	seq_counter = 0  # Contador de sequências
	for record in SeqIO.parse(arquivo, "fasta"):
		# Seleciona o arquivo de saída correto com base no número de sequências já gravadas
		if seq_counter < num_seq_por_arquivo:
			SeqIO.write(record, output1, "fasta")
		else:
			SeqIO.write(record, output2, "fasta")
		seq_counter += 1
		
