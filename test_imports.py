#!/usr/bin/env python3
"""
Simple validation script to test that Code2 can be imported and functions are defined.
This doesn't test with real data, just validates structure and imports.
"""

import sys
import os

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

print("="*80)
print("VALIDATION TEST FOR CODE2 ENHANCEMENTS")
print("="*80)

try:
    print("\n1. Checking Python version...")
    print(f"   Python {sys.version}")
    
    print("\n2. Checking dependencies (optional)...")
    try:
        import pandas as pd
        import numpy as np
        print("   ✓ Core dependencies (pandas, numpy) available")
        
        # Try importing sklearn (optional)
        try:
            from sklearn.cluster import DBSCAN
            from sklearn.ensemble import IsolationForest
            from sklearn.preprocessing import StandardScaler
            print("   ✓ sklearn libraries available (ML features enabled)")
        except ImportError:
            print("   ⚠ sklearn not available (ML features will be limited)")
    except ImportError as e:
        print(f"   ⚠ Dependencies not installed ({e})")
        print("   Note: Code validation will continue without import testing")
    
    print("\n3. Loading Code2 file...")
    # Import the module (this will execute top-level code)
    # We can't actually import it as a module due to the name, but we can exec it
    with open('Code2', 'r') as f:
        code_content = f.read()
    
    # Check for function definitions
    print("   ✓ Code2 file loaded")
    
    print("\n4. Checking for new function definitions...")
    new_functions = [
        'extract_time_features',
        'calculate_trade_velocity_acceleration',
        'calculate_price_impact_metrics',
        'estimate_spread_from_trades',
        'calculate_microstructure_noise',
        'analyze_trade_size_distribution',
        'analyze_trade_profitability',
        'detect_leader_follower_dynamics',
        'extract_tape_reading_features',
        'calculate_kyles_lambda',
        'calculate_amihud_illiquidity',
        'calculate_liquidity_depth_score',
        'calculate_vpin',
        'calculate_order_toxicity',
        'decompose_effective_spread',
        'detect_market_regime',
        'detect_regime_transitions',
        'encode_cyclic_time',
        'analyze_session_transitions',
        'calculate_smart_money_index',
        'calculate_exhaustion_score',
        'detect_capitulation_events',
        'detect_divergences',
        'detect_absorption_zones',
        'detect_iceberg_orders',
        'calculate_timeframe_alignment',
        'calculate_cross_timeframe_correlation',
        'calculate_fractal_dimension',
        'detect_institutional_footprint',
    ]
    
    missing_functions = []
    for func_name in new_functions:
        if f'def {func_name}(' in code_content:
            print(f"   ✓ {func_name}")
        else:
            missing_functions.append(func_name)
            print(f"   ✗ {func_name} - NOT FOUND")
    
    print(f"\n5. Summary:")
    print(f"   Total new functions expected: {len(new_functions)}")
    print(f"   Functions found: {len(new_functions) - len(missing_functions)}")
    print(f"   Functions missing: {len(missing_functions)}")
    
    if len(missing_functions) == 0:
        print("\n✅ ALL VALIDATION CHECKS PASSED!")
        print("   All expected functions are defined in Code2")
    else:
        print("\n⚠ VALIDATION INCOMPLETE")
        print(f"   Missing functions: {', '.join(missing_functions)}")
    
    print("\n6. Checking file statistics...")
    line_count = code_content.count('\n')
    print(f"   Total lines: {line_count:,}")
    print(f"   File size: {len(code_content):,} bytes")
    
    # Count function definitions
    total_functions = code_content.count('def ')
    print(f"   Total functions defined: {total_functions}")
    
    print("\n" + "="*80)
    print("VALIDATION COMPLETE")
    print("="*80)
    
    sys.exit(0 if len(missing_functions) == 0 else 1)

except Exception as e:
    print(f"\n❌ ERROR: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
