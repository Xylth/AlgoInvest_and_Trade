from dataclasses import dataclass, field

@dataclass
class Validation:
    """
    Classe pour représenter les validations effectuées sur le dataset
    """
    all_entries: int = 0
    invalid_costs: int = 0
    invalid_performances: int = 0
    duplicates: int = 0
    valid_entries: int = 0
    
    def to_dict(self):
        return {
            "all_entries" : self.all_entries,
            "invalid_costs": self.invalid_costs,
            "invalid_performances": self.invalid_performances,
            "duplicates": self.duplicates,
            "valid_entries": self.valid_entries
        }

@dataclass
class Stats:
    """
    Classe pour représenter les statistiques d'un attribut dans le dataset validé
    """
    min: float = 0.0
    max: float = 0.0
    mean: float = 0.0
    median: float = 0.0
    stdev: float = 0.0
    
    def to_dict(self):
        return {
            "min": self.min,
            "max": self.max,
            "mean": self.mean,
            "median": self.median,
            "stdev": self.stdev,
        }

@dataclass
class Analysis:
    """
    Classe pour représenter les statistiques du dataset validé
    """
    cost: Stats = field(default_factory=Stats)
    performance: Stats = field(default_factory=Stats)
    gain: Stats = field(default_factory=Stats)
    
    def to_dict(self):
        return {
            "cost" : self.cost.to_dict(),
            "performance" : self.performance.to_dict(),
            "gain" : self.gain.to_dict()
        }

@dataclass
class Report:
    """
    Classe pour représenter le rapport d'exploration du dataset
    """
    file_name: str = ""
    validation: Validation = field(default_factory=Validation)
    analysis: Analysis = field(default_factory=Analysis)
    
    def to_dict(self):
        return {
            "file name" : self.file_name,
            "validation" : self.validation.to_dict(),
            "analysis" : self.analysis.to_dict()
        }
        
    