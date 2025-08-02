class SummaryStatistics:
    """A class to compute summary statistics for a list of numbers."""
    
    def __init__(self, data: list[float]):
        if not data:
            raise ValueError("Data list cannot be empty.")
        self.data = data
    

    def sample_mean(self) -> float:
        """Calculate the sample mean, bar(x), of a list of numbers:
        bar(x) = sum(x_i) / n"""
        return sum(self.data) / len(self.data)
    

    def sample_variance(self, data: list[float]) -> float:
        """Calculate the sample variance, s^2, of a list of numbers: 
        s^2 = (1 / (n - 1)) * sum((x_i - bar(x))^2)"""
        if len(self.data) < 2:
            raise ValueError("Data list must contain at least two elements.")
        mean = self.sample_mean(data)
        return sum((x - mean) ** 2 for x in self.data) / (len(self.data) - 1)
    