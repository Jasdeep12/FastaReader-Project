from dataclasses import dataclass
from typing  import Optional


@dataclass
class Sequence:
	"Represents a Biological Sequence -> DNA, RNA, or Protein"
	
	header: str
	sequence : str
	quality: Optional[str] = None

	@property
	def length(self) -> int:
		"Gets Sequence Length"
		return len(self.sequence)
	
	@property
	def identifier(self) -> str:
		"Grabs Sequence Identifier, first whitespace delimited token"
		return self.header.split()[0]

	@property
	def description(self) -> str:
		"Extract description"

		parts = self.header.split(None,1)
		return parts[1] if len.parts > 1 else ""

	def __repr__(self) -> str:
		s_info = f", quality = {len(self.quality)}bp" if self.quality else ""
		return f"Sequence({self.identifier}, {self.length}bp{s_info}"


