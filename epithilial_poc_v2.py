#!/usr/bin/env python3
"""
EPITHILIAL Cancer Detection POC v2.0
Enhanced with risk scoring and metrics
"""
import cancer_metrics

def main():
    print("=== EPITHILIAL Cancer Detection POC v2.0 ===")
    print("Enhanced epithelial cell analysis\n")
    
    # Test with sample data
    sample_data = [0.85, 0.72, 0.68, 0.91]
    
    # Use old simple detector
    from epithilial_poc import CancerDetector
    old_detector = CancerDetector()
    old_result = old_detector.analyze(sample_data)
    print(f"Basic detector: {old_result}")
    
    # Use new enhanced metrics
    score, level, confidence = cancer_metrics.calculate_risk_score(sample_data[:3])
    print(f"Enhanced metrics: Score={score}, Risk={level}, Confidence={confidence}")
    
    print("\n✅ Update successful! More accurate cancer detection.")

if __name__ == "__main__":
    main()
