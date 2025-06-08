def get_crop_recommendation(season: str, soil: str) -> str:
    recommendations = {
        'summer': {'loamy': 'Maize', 'clayey': 'Sugarcane', 'sandy': 'Groundnut'},
        'winter': {'loamy': 'Wheat', 'clayey': 'Mustard', 'sandy': 'Barley'},
        'monsoon': {'loamy': 'Paddy', 'clayey': 'Jute', 'sandy': 'Millets'}
    }
    return recommendations.get(season.lower(), {}).get(soil.lower(), "No recommendation found.")
