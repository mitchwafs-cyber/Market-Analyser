# Microstructure Analytics Documentation

## Overview
This document describes the 10 additional microstructure analytics modules added to the Ultra-Comprehensive Order Flow Analyzer v2.1.

## New Analytics Modules

### 1. Impact & Toxicity Analysis (Files: 35-36)

**Purpose**: Measure price impact and order flow toxicity to identify informed trading activity.

**Metrics Calculated**:
- **Kyle Lambda**: Price impact per unit of signed notional volume (measures market impact)
- **Amihud Illiquidity**: Ratio of absolute returns to dollar volume (measures liquidity)
- **Signed-Order Autocorrelation**: Persistence of buy/sell order flow (lag 1, 3, 5)
- **Refined VPIN**: Volume-synchronized probability of informed trading with:
  - Dynamic bucket sizing based on sqrt(recent volume)
  - Z-scored spike detection for toxic flow events

**Output Files**:
- `35_impact_toxicity_full.csv`: Complete time-series data with all metrics
- `36_impact_toxicity_summary.csv`: Summary statistics

**Key Signals**:
- High Kyle lambda → Strong price impact (low liquidity or informed trading)
- High Amihud illiquidity → Difficult to execute without moving price
- VPIN spikes (z-score > 2) → Informed trader activity detected

---

### 2. Absorption vs Rejection Analysis (Files: 37-39)

**Purpose**: Distinguish between price levels where volume is absorbed vs rejected.

**Metrics Calculated**:
- **Absorption Test**: High volume + small range + low delta/volume ratio
- **Delta/Range Efficiency**: Measures whether movement is initiative-driven or absorbed
- **Zone Classification**: Absorption zones (support/resistance) vs rejection zones

**Output Files**:
- `37_absorption_rejection_bars.csv`: Bar-level analysis with classifications
- `38_absorption_zones_enhanced.csv`: Identified absorption levels
- `39_rejection_zones.csv`: Identified rejection zones

**Key Signals**:
- Absorption zones → Strong institutional accumulation/distribution levels
- High initiative bars → Directional conviction moves
- Low absorption bars → Potential reversal zones

---

### 3. Trapped Traders Detection (File: 40)

**Purpose**: Identify traders caught on wrong side after liquidity sweeps.

**Metrics Calculated**:
- **Post-Sweep MFE/MAE**: Maximum Favorable/Adverse Excursion after sweep
- **Trap Strength**: Ratio of MAE to MFE (higher = more trapped)
- **Trap Classification**: Trapped longs (after upside sweep) vs trapped shorts (after downside sweep)

**Output Files**:
- `40_trapped_traders.csv`: All trapped trader zones with MFE/MAE analysis

**Key Signals**:
- Trapped longs → Potential for further downside as stops trigger
- Trapped shorts → Potential for further upside as covering occurs
- High trap strength → Strong directional follow-through expected

---

### 4. Size-Tier Intelligence (Files: 41-42)

**Purpose**: Analyze trade size distribution and large player activity.

**Metrics Calculated**:
- **Size Buckets**: Percentile-based categorization (p0-p50, p50-p90, p90-p99, p99+)
- **Volume Share**: Percentage of volume per size tier
- **Impact Per Bucket**: Price impact efficiency by size tier
- **Large Clusters**: Detection of coordinated large-size aggressive trading

**Output Files**:
- `41_size_tier_stats.csv`: Statistics by size tier
- `42_large_size_clusters.csv`: Clustered large trades (institutional)

**Key Signals**:
- p99+ volume surge → Whale/institutional activity
- Large buy/sell clusters → Coordinated institutional positioning
- High impact in top tier → Smart money moving price

---

### 5. Session Microstructure & Value Migration (Files: 43-44)

**Purpose**: Track key levels and value area changes across trading sessions.

**Metrics Calculated**:
- **Session Profiles**: VWAP, POC, VAH, VAL per Asian/London/NY session
- **POC Migration**: How point of control shifts between sessions
- **Virgin POCs**: POC levels not yet revisited (magnetic price targets)
- **Poor Highs/Lows**: Session extremes with weak volume (likely to be revisited)

**Output Files**:
- `43_session_microstructure.csv`: Complete session statistics
- `44_virgin_pocs.csv`: Unvisited POC levels

**Key Signals**:
- Virgin POCs → Potential price magnets for future revisit
- POC migration → Shows which session controls value
- Poor high/low → Weak extreme likely to be tested again

---

### 6. Volume/Delta Shape Diagnostics (Files: 45-47)

**Purpose**: Analyze distribution characteristics and detect regime changes.

**Metrics Calculated**:
- **Skewness**: Volume and delta distribution asymmetry
- **Kurtosis**: Tail heaviness (extreme event frequency)
- **Change-Point Detection**: Identifies shifts in cumulative delta slope
- **Slope Sign Changes**: First-derivative transitions

**Output Files**:
- `45_volume_delta_shape_bars.csv`: Bar-level shape statistics
- `46_volume_delta_shape_prices.csv`: Price-level shape statistics
- `47_delta_changepoints.csv`: Detected regime changes

**Key Signals**:
- High positive skew → Dominated by large buy/sell prints
- Change-points → Shift in order flow regime
- High kurtosis → Fat tails (expect more extreme moves)

---

### 7. Liquidity Voids Detection (Files: 48-49)

**Purpose**: Find price ranges with minimal volume (fast movement zones).

**Metrics Calculated**:
- **Void Detection**: Consecutive price levels with near-zero volume
- **Void Width**: Size of the liquidity gap
- **Fill Status**: Whether void has been filled (price revisited)

**Output Files**:
- `48_liquidity_voids_all.csv`: All detected voids
- `49_liquidity_voids_unfilled.csv`: Unfilled voids (likely fill targets)

**Key Signals**:
- Unfilled voids above → Price likely to move quickly if breached
- Unfilled voids below → Support levels with fast rejection potential
- Recent void fills → Confirms move validity

---

### 8. Time/Pace Diagnostics - Algo Footprints (Files: 50-51)

**Purpose**: Detect algorithmic trading activity through timing patterns.

**Metrics Calculated**:
- **Run-Length**: Consecutive aggressive prints (HFT signatures)
- **Burstiness**: Coefficient of variation of inter-trade times
- **Pulse Detection**: 1-second windows with:
  - Trade count spikes
  - Signed volume surges
  - Price change acceleration

**Output Files**:
- `50_aggressive_print_runs.csv`: Sustained aggressive activity
- `51_pulse_events.csv`: Buy/sell pulse detections

**Key Signals**:
- Buy pulses → Algorithmic buying aggression
- Sell pulses → Algorithmic selling aggression
- High burstiness → Algo war (multiple algos competing)
- Long aggressive runs → Sustained directional algo execution

---

### 9. Price-Impact Asymmetry (Files: 52-55)

**Purpose**: Measure how price impact differs by side and distance from key levels.

**Metrics Calculated**:
- **Side-Specific Impact**: Buy impact vs sell impact by distance buckets
- **VWAP Distance Impact**: How impact changes away from VWAP
- **POC Distance Impact**: How impact changes away from POC
- **Chase Zones**: High impact far from value (chasing moves)
- **Exhaustion Zones**: Low impact at extremes (running out of steam)

**Output Files**:
- `52_chase_zones.csv`: Upside/downside chase activity
- `53_exhaustion_zones_impact.csv`: Exhaustion at extremes
- `54_buy_impact_by_distance.csv`: Buy-side impact profile
- `55_sell_impact_by_distance.csv`: Sell-side impact profile

**Key Signals**:
- Chase zones → FOMO trading, potential reversal setup
- Exhaustion zones → Trend running out of steam
- Asymmetric impact → One side more desperate (informative)

---

### 10. Regime & Volatility Coupling (Files: 56-59)

**Purpose**: Identify regime shifts through volatility-volume-delta relationships.

**Metrics Calculated**:
- **Volatility × Volume**: Co-movement of volatility and volume
- **Delta × Volatility**: Co-movement of order flow and volatility
- **Fake Moves**: High volatility + low delta (noise, not conviction)
- **Thin-Liquidity Squeezes**: High delta + low volume + low volatility
- **Strong Conviction**: High volatility + high delta + high volume

**Output Files**:
- `56_regime_summary.csv`: Regime classification counts
- `57_fake_moves.csv`: Noise moves to fade
- `58_thin_liquidity_squeezes.csv`: Squeeze events to follow
- `59_strong_conviction_moves.csv`: High-conviction trends to ride

**Key Signals**:
- Fake moves → Fade the move (no real conviction)
- Thin-liquidity squeeze → Follow the move (forced position changes)
- Strong conviction → Trend continuation likely
- Decoupling (correlation breakdown) → Regime change imminent

---

## Integration with Master Signals

All 10 analytics modules feed into the master signal generation (`00_MASTER_TRADING_SIGNALS.csv`):

**Critical Priority Signals**:
- Trapped trader zones
- Virgin POCs
- Exhaustion zones
- Fake move detection
- Strong conviction moves
- Stacked buy/sell layers (from Tier 1)

**High Priority Signals**:
- Absorption zones
- VPIN refined spikes
- Size-tier clusters
- Unfilled voids
- Pulse events
- Chase zones
- Poor highs/lows

**Medium Priority Signals**:
- Delta change-points
- Volume/delta shape anomalies

## Usage Tips

1. **For Entry Signals**: Combine trapped trader zones + virgin POCs + absorption zones
2. **For Exit Signals**: Watch for exhaustion zones + fake moves + chase zones
3. **For Trend Confirmation**: Strong conviction moves + pulse events + size-tier clusters
4. **For Reversal Setups**: Trapped traders + poor highs/lows + unfilled voids
5. **For Scalping**: Algo footprints + thin-liquidity squeezes + impact asymmetry

## Performance Notes

- All computations use only tick data columns (no order book required)
- Dynamic VPIN calculation uses a loop (acceptable for adaptive bucketing)
- Shape diagnostics use scipy when available for efficiency
- Impact asymmetry uses quantile binning for robustness

## Dependencies

- pandas (required)
- numpy (required)
- scikit-learn (optional, for ML anomaly detection)
- scipy (optional, for efficient skew/kurtosis calculations)

---

*For questions or issues, please refer to the main README or open a GitHub issue.*
