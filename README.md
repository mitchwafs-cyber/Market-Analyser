# Market-Analyser

Ultra-Comprehensive Institutional Order Flow Analyzer v2.1 with 90%+ signal coverage for crypto markets.

## Overview

Analysis of the crypto markets to identify volume and major zones for buyers and sellers, featuring advanced microstructure analytics and institutional-grade order flow detection.

## Features

### Tier 2 Microstructure Analytics (NEW - v2.1)
- **Impact & Toxicity Analysis**: Kyle lambda, Amihud illiquidity, refined VPIN with dynamic bucketing
- **Absorption vs Rejection**: Enhanced delta/range efficiency and zone classification
- **Trapped Traders Detection**: Post-sweep MFE/MAE analysis to identify trapped positions
- **Size-Tier Intelligence**: Percentile-based trade bucketing and large-size cluster detection
- **Session Microstructure**: VWAP/POC migration, virgin POCs, poor highs/lows per session
- **Volume/Delta Shape Diagnostics**: Skew/kurtosis analysis with change-point detection
- **Liquidity Voids**: Detection of consecutive low-volume price levels (filled vs unfilled)
- **Time/Pace Diagnostics**: Algo footprints via burstiness and sub-second pulse detection
- **Price-Impact Asymmetry**: Side-specific impact analysis and chase/exhaustion zones
- **Regime & Volatility Coupling**: Fake move detection and thin-liquidity squeeze identification

### Tier 1 Features
- Advanced CVD Analysis with slope/acceleration
- Stacked Imbalances (vertical order flow)
- Relative Volume (RVOL) analysis
- Single Prints & Excess Detection
- VPIN (Volume-Synchronized Probability of Informed Trading)

### Core Features
- Volume Profile (POC, VAH, VAL, HVN, LVN)
- Order Flow Imbalance by Price
- Delta Divergence Detection
- Iceberg Order Detection
- Footprint Charts (Time × Price Matrix)
- Liquidity Sweep Detection (Stop Hunts)
- Price Velocity Analysis
- Participant Classification (Retail vs Institutional)
- Anchored VWAP Analysis
- Volume Anomaly Detection (Whale Trades)
- Trade Clustering (Algo Detection)
- Multi-Timeframe Delta Correlation
- Session Analytics (Asian/London/NY)
- ML-Based Anomaly Detection
- Delta Momentum Oscillator

## Output

The analyzer generates **60+ CSV files** with comprehensive analytics:

- `00_MASTER_TRADING_SIGNALS.csv`: Consolidated signals from all analytics
- `01-34`: Core and Tier 1 analytics
- `35-59`: Tier 2 microstructure analytics
- `99_SCAN_VALIDATION_REPORT.csv`: Data completeness validation

For detailed descriptions of all analytics, see [MICROSTRUCTURE_ANALYTICS.md](MICROSTRUCTURE_ANALYTICS.md).

## Requirements

- Python 3.7+
- pandas
- numpy
- scikit-learn (optional, for ML features)
- scipy (optional, for enhanced calculations)

## Usage

1. Configure data paths in `ultra_comprehensive_order_flow_analyzer_v2.py`:
   ```python
   ZIP_PATH = r"path/to/your/BTCUSDT-aggTrades-YYYY-MM-DD.zip"
   OUTPUT_FOLDER = r"path/to/output/folder"
   ```

2. Run the analyzer:
   ```bash
   python ultra_comprehensive_order_flow_analyzer_v2.py
   ```

3. Review outputs in the specified output folder

## Testing

Run the comprehensive test suite:
```bash
python test_microstructure.py
```

This validates all 10 Tier 2 microstructure analytics modules with synthetic data.

## Signal Usage

- **Entry Signals**: Trapped trader zones + virgin POCs + absorption zones
- **Exit Signals**: Exhaustion zones + fake moves + chase zones  
- **Trend Confirmation**: Strong conviction moves + pulse events + size clusters
- **Reversal Setups**: Trapped traders + poor highs/lows + unfilled voids
- **Scalping**: Algo footprints + thin-liquidity squeezes + impact asymmetry

## License

See repository license file for details.
