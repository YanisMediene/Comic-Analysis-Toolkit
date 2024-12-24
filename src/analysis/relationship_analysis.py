def analyze_relationships(detections):
    # Example of associating balloons with characters
    relationships = []
    for balloon in detections["balloons"]:
        nearest_character = find_nearest(balloon, detections["characters"])
        relationships.append({"balloon": balloon, "character": nearest_character})
    return relationships
