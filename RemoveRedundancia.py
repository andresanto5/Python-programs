#!/usr/bin/env python3

from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq

def cluster_fasta(fasta_file, identity_threshold):
	# Carrega sequências do arquivo fasta
	sequences = []
	for record in SeqIO.parse(fasta_file, "fasta"):
		sequences.append(record.seq)
		
	# Calcula a matriz de similaridade
	similarity_matrix = []
	for i, seq1 in enumerate(sequences):
		similarity_row = []
		for j, seq2 in enumerate(sequences):
			similarity = seq1 == seq2
			similarity_row.append(similarity)
		similarity_matrix.append(similarity_row)
		
	# Aplica o algoritmo de clusterização
	clusters = []
	for i, seq1 in enumerate(sequences):
		cluster = []
		for j, seq2 in enumerate(sequences):
			if similarity_matrix[i][j]:
				cluster.append(j)
		if len(cluster) > 1:
			clusters.append(cluster)
			
	# Seleciona o representante de cada cluster
	representatives = []
	for cluster in clusters:
		max_similarity = 0
		representative = None
		for i in cluster:
			similarity_sum = sum(similarity_matrix[i])
			if similarity_sum > max_similarity:
				max_similarity = similarity_sum
				representative = i
		representatives.append(representative)
		
	# Cria um novo arquivo fasta com as sequências representantes
	records = []
	for i, record in enumerate(SeqIO.parse(fasta_file, "fasta")):
		if i in representatives:
			records.append(record)
	SeqIO.write(records, "representatives.fasta", "fasta")

cluster_fasta("Def_sequencias.fasta", 0.9)
