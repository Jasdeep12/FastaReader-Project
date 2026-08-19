from typing import Iterator


class FileReader:
	"Handles reading from FASTA/FASTQ files."
	"Supports plain text and compressed files"

	def __init__(self, filepath: str):
		pass

	def read_lines(self) -> Iterator[str]:
		pass


	def read_in_chunks(self, chunk_size: int = 1000) -> Iterator[list]
		pass
