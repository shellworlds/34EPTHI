#!/usr/bin/env python3
"""
Enhanced Cancer Detection Metrics for EPITHILIAL POC
"""

def calculate_risk_score(cell_features):
    """
    Calculate cancer risk score based on epithelial cell features
    
    Args:
        cell_features: List of feature values [size, ratio, irregularity]
    
    Returns:
        tuple: (risk_score, risk_level, confidence)
    """
    if not cell_features or len(cell_features) < 3:
        return 0.0, "INSUFFICIENT_DATA", 0.0
    
    size, ratio, irregularity = cell_features[:3]
    
    # Weighted risk calculation
    risk_score = (size * 0.3 + ratio * 0.4 + irregularity * 0.3)
    
    # Risk classification
    if risk_score > 0.8:
        risk_level = "HIGH_RISK"
    elif risk_score > 0.5:
        risk_level = "MEDIUM_RISK"
    else:
        risk_level = "LOW_RISK"
    
    # Confidence based on data quality
    confidence = min(1.0, len(cell_features) / 10)
    
    return round(risk_score, 3), risk_level, round(confidence, 2)

def main():
    """Test the enhanced cancer detection"""
    # Sample epithelial cell data
    test_cells = [
        [0.9, 0.8, 0.7],  # High risk
        [0.4, 0.3, 0.2],  # Low risk
        [0.6, 0.7, 0.5],  # Medium risk
    ]
    
    print("EPITHILIAL Enhanced Cancer Detection")
    print("=" * 40)
    for i, cell in enumerate(test_cells):
        score, level, conf = calculate_risk_score(cell)
        print(f"Cell {i+1}: Score={score}, Risk={level}, Confidence={conf}")

if __name__ == "__main__":
    main()
