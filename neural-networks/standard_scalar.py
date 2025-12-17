from math import sqrt

def normalize_feature(x: float, mean: float, sd: float) -> float:
    """Normalizes a single feature based on given data"""
    return (x - mean) / sd

def normalize(data: list[float]) -> list[float]:
    """Normalizes the given data (array)"""
    mean = sum(data) / len(data)
    sum_deviation_square = 0
    for x in data:
        sum_deviation_square += (x - mean) ** 2

    sd = sqrt(sum_deviation_square / len(data))

    result_data = []

    for x in data:
        normalized_x = normalize_feature(x, mean, sd)
        result_data.append(normalized_x)

    return result_data

data_provided = [10.0, 20.0, 30.0, 40.0, 50.0]
normalized_data = normalize(data_provided)

print(f"Original data: {data_provided}")
print(f"Normalized data: {normalized_data}")
