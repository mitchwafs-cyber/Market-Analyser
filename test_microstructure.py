#!/usr/bin/env python3
"""
Simple test to verify the microstructure analytics functions work correctly
with synthetic data.
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Import the functions we want to test
import sys
sys.path.insert(0, '/home/runner/work/Market-Analyser/Market-Analyser')

# Create synthetic test data
def create_synthetic_data(n_rows=1000):
    """Create synthetic trade data for testing"""
    np.random.seed(42)
    
    start_time = datetime(2025, 12, 3, 0, 0, 0)
    timestamps = [start_time + timedelta(seconds=i*0.5) for i in range(n_rows)]
    
    # Generate price walk
    price_changes = np.random.randn(n_rows) * 0.5
    prices = 100000 + np.cumsum(price_changes)
    
    # Generate volumes
    quantities = np.random.exponential(scale=0.1, size=n_rows)
    
    # Generate buy/sell classification
    is_buyer_maker = np.random.choice([True, False], size=n_rows, p=[0.5, 0.5])
    
    df = pd.DataFrame({
        'timestamp': timestamps,
        'price': prices,
        'quantity': quantities,
        'is_buyer_maker': is_buyer_maker,
        'transact_time': [int(ts.timestamp() * 1000) for ts in timestamps]
    })
    
    # Add derived columns like in prepare_base_data
    df['buy_vol'] = np.where(df['is_buyer_maker'] == False, df['quantity'], 0.0)
    df['sell_vol'] = np.where(df['is_buyer_maker'] == True, df['quantity'], 0.0)
    df['buy_value'] = df['buy_vol'] * df['price']
    df['sell_value'] = df['sell_vol'] * df['price']
    df['time_diff'] = df['timestamp'].diff().dt.total_seconds().fillna(0.0)
    df['price_change'] = df['price'].diff().fillna(0.0)
    df['close'] = df['price']
    df['high'] = df['price']
    df['low'] = df['price']
    df['open'] = df['price']
    df['volume'] = df['quantity']
    
    return df

def test_impact_and_toxicity():
    """Test Impact & Toxicity analysis"""
    print("\n" + "="*60)
    print("Testing: Impact & Toxicity Analysis")
    print("="*60)
    
    from ultra_comprehensive_order_flow_analyzer_v2 import calculate_impact_and_toxicity
    
    df = create_synthetic_data(500)
    result = calculate_impact_and_toxicity(df, window_sizes=[10, 20])
    
    assert result is not None, "Result should not be None"
    assert 'impact_data' in result, "Should have impact_data"
    assert 'impact_summary' in result, "Should have impact_summary"
    
    impact_data = result['impact_data']
    assert 'kyle_lambda_10' in impact_data.columns, "Should have kyle_lambda"
    assert 'amihud_illiq_10' in impact_data.columns, "Should have amihud_illiq"
    assert 'vpin_refined' in impact_data.columns, "Should have vpin_refined"
    
    print("✅ Impact & Toxicity test passed!")
    return True

def test_absorption_vs_rejection():
    """Test Absorption vs Rejection analysis"""
    print("\n" + "="*60)
    print("Testing: Absorption vs Rejection Analysis")
    print("="*60)
    
    from ultra_comprehensive_order_flow_analyzer_v2 import detect_absorption_vs_rejection
    
    df = create_synthetic_data(500)
    result = detect_absorption_vs_rejection(df)
    
    assert result is not None, "Result should not be None"
    assert 'all_bars' in result, "Should have all_bars"
    assert 'absorption_zones' in result, "Should have absorption_zones"
    
    print("✅ Absorption vs Rejection test passed!")
    return True

def test_trapped_traders():
    """Test Trapped Traders detection"""
    print("\n" + "="*60)
    print("Testing: Trapped Traders Detection")
    print("="*60)
    
    from ultra_comprehensive_order_flow_analyzer_v2 import detect_trapped_traders
    
    df = create_synthetic_data(500)
    result = detect_trapped_traders(df, sweep_lookback=10, mfe_mae_bars=5)
    
    assert result is not None, "Result should not be None"
    assert isinstance(result, pd.DataFrame), "Should return DataFrame"
    
    print("✅ Trapped Traders test passed!")
    return True

def test_size_tier_intelligence():
    """Test Size-Tier Intelligence analysis"""
    print("\n" + "="*60)
    print("Testing: Size-Tier Intelligence Analysis")
    print("="*60)
    
    from ultra_comprehensive_order_flow_analyzer_v2 import analyze_size_tier_intelligence
    
    df = create_synthetic_data(500)
    result = analyze_size_tier_intelligence(df, percentiles=[50, 90, 99])
    
    assert result is not None, "Result should not be None"
    assert 'size_stats' in result, "Should have size_stats"
    assert 'large_clusters' in result, "Should have large_clusters"
    
    print("✅ Size-Tier Intelligence test passed!")
    return True

def test_session_microstructure():
    """Test Session Microstructure analysis"""
    print("\n" + "="*60)
    print("Testing: Session Microstructure Analysis")
    print("="*60)
    
    from ultra_comprehensive_order_flow_analyzer_v2 import analyze_session_microstructure
    
    df = create_synthetic_data(1000)
    result = analyze_session_microstructure(df)
    
    assert result is not None, "Result should not be None"
    assert 'session_profiles' in result, "Should have session_profiles"
    assert 'virgin_pocs' in result, "Should have virgin_pocs"
    
    print("✅ Session Microstructure test passed!")
    return True

def test_volume_delta_shape():
    """Test Volume/Delta Shape diagnostics"""
    print("\n" + "="*60)
    print("Testing: Volume/Delta Shape Diagnostics")
    print("="*60)
    
    from ultra_comprehensive_order_flow_analyzer_v2 import analyze_volume_delta_shape
    
    df = create_synthetic_data(500)
    result = analyze_volume_delta_shape(df)
    
    assert result is not None, "Result should not be None"
    assert 'bar_shape_stats' in result, "Should have bar_shape_stats"
    assert 'changepoints' in result, "Should have changepoints"
    
    print("✅ Volume/Delta Shape test passed!")
    return True

def test_liquidity_voids():
    """Test Liquidity Voids detection"""
    print("\n" + "="*60)
    print("Testing: Liquidity Voids Detection")
    print("="*60)
    
    from ultra_comprehensive_order_flow_analyzer_v2 import detect_liquidity_voids
    
    df = create_synthetic_data(500)
    result = detect_liquidity_voids(df)
    
    assert result is not None, "Result should not be None"
    assert 'all_voids' in result, "Should have all_voids"
    assert 'unfilled_voids' in result, "Should have unfilled_voids"
    
    print("✅ Liquidity Voids test passed!")
    return True

def test_time_pace_diagnostics():
    """Test Time/Pace diagnostics"""
    print("\n" + "="*60)
    print("Testing: Time/Pace Diagnostics")
    print("="*60)
    
    from ultra_comprehensive_order_flow_analyzer_v2 import analyze_time_pace_diagnostics
    
    df = create_synthetic_data(500)
    result = analyze_time_pace_diagnostics(df)
    
    assert result is not None, "Result should not be None"
    assert 'pace_data' in result, "Should have pace_data"
    assert 'pulse_events' in result, "Should have pulse_events"
    
    print("✅ Time/Pace Diagnostics test passed!")
    return True

def test_price_impact_asymmetry():
    """Test Price-Impact Asymmetry analysis"""
    print("\n" + "="*60)
    print("Testing: Price-Impact Asymmetry Analysis")
    print("="*60)
    
    from ultra_comprehensive_order_flow_analyzer_v2 import calculate_price_impact_asymmetry
    
    df = create_synthetic_data(500)
    result = calculate_price_impact_asymmetry(df)
    
    assert result is not None, "Result should not be None"
    assert 'impact_data' in result, "Should have impact_data"
    assert 'chase_zones' in result, "Should have chase_zones"
    
    print("✅ Price-Impact Asymmetry test passed!")
    return True

def test_regime_volatility_coupling():
    """Test Regime & Volatility Coupling analysis"""
    print("\n" + "="*60)
    print("Testing: Regime & Volatility Coupling Analysis")
    print("="*60)
    
    from ultra_comprehensive_order_flow_analyzer_v2 import analyze_regime_volatility_coupling
    
    df = create_synthetic_data(500)
    result = analyze_regime_volatility_coupling(df)
    
    assert result is not None, "Result should not be None"
    assert 'regime_data' in result, "Should have regime_data"
    assert 'regime_summary' in result, "Should have regime_summary"
    
    print("✅ Regime & Volatility Coupling test passed!")
    return True

def run_all_tests():
    """Run all tests"""
    print("\n" + "="*60)
    print("RUNNING ALL MICROSTRUCTURE ANALYTICS TESTS")
    print("="*60)
    
    tests = [
        test_impact_and_toxicity,
        test_absorption_vs_rejection,
        test_trapped_traders,
        test_size_tier_intelligence,
        test_session_microstructure,
        test_volume_delta_shape,
        test_liquidity_voids,
        test_time_pace_diagnostics,
        test_price_impact_asymmetry,
        test_regime_volatility_coupling
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            if test():
                passed += 1
        except Exception as e:
            print(f"❌ Test failed: {test.__name__}")
            print(f"   Error: {e}")
            failed += 1
    
    print("\n" + "="*60)
    print(f"TEST SUMMARY: {passed} passed, {failed} failed")
    print("="*60)
    
    return failed == 0

if __name__ == "__main__":
    success = run_all_tests()
    exit(0 if success else 1)
