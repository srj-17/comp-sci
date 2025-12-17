def normalize_feature(x: float, min_x: float, max_x: float) -> float:
    """Normalizes a single feature based on given data"""
    return (x - min_x) / (max_x - min_x)

def normalize(data: list[float]) -> list[float]:
    """Normalizes the given data (array)"""
    min_data = min(data)
    max_data = max(data)
    result_data = []

    for x in data:
        normalized_x = normalize_feature(x, min_data, max_data)
        result_data.append(normalized_x)

    return result_data

data_provided = [10.0, 20.0, 30.0, 40.0, 50.0]
normalized_data = normalize(data_provided)

print(f"Original data: {data_provided}")
print(f"Normalized data: {normalized_data}")
