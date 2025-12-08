# AI-Ready Analysis Prompts for Order Flow Data

This document contains AI-ready prompts for analyzing each of the 59+ CSV output files. Copy these prompts to ChatGPT, Claude, or any AI assistant along with your CSV data for automated trading zone analysis.

## Quick Start Guide

1. **Choose your file** from the list below
2. **Copy the entire prompt** for that file
3. **Paste into your AI assistant**
4. **Upload or paste your CSV data**
5. **Review the AI's analysis** for actionable trading insights

---

## Table of Contents
- [Master Files](#master-files)
- [Volume Profile & Market Structure](#volume-profile--market-structure)
- [Order Flow & Imbalances](#order-flow--imbalances)
- [Institutional & Smart Money](#institutional--smart-money)
- [Advanced Microstructure](#advanced-microstructure)
- [Multi-File Analysis](#multi-file-analysis)

---

## Master Files

### File 00: MASTER_TRADING_SIGNALS.csv

**COPY THIS PROMPT:**
```
Analyze this consolidated trading signals file containing all key signals from the order flow analysis.

FILE STRUCTURE:
- signal_type: BUY_SIGNAL, SELL_SIGNAL, NEUTRAL
- price: exact price level
- strength: 1-10 scale (higher = stronger)
- timestamp: when signal occurred
- zone_type: ACCUMULATION, DISTRIBUTION, REVERSAL, CONTINUATION
- confidence: 0-1 probability score
- volume: associated volume
- delta: cumulative delta at signal

ANALYSIS TASKS:
1. Identify strongest buy signals (strength >= 8, confidence >= 0.75)
2. Identify strongest sell signals (strength >= 8, confidence >= 0.75)
3. Find price levels with signal clusters (multiple signals at same price)
4. Check for conflicting signals at same price (warning sign)
5. Calculate net signal bias (BUY vs SELL signal count)
6. Note time distribution (are signals concentrated in specific periods?)

OUTPUT FORMAT:
📈 BUYER ZONES: [List price levels with strong buy signals, include strength & confidence]
📉 SELLER ZONES: [List price levels with strong sell signals, include strength & confidence]
⚠️ CONFLICTING ZONES: [Prices with both buy and sell signals]
📊 NET BIAS: [BUY/SELL/NEUTRAL with X% conviction]
⏰ TIME PATTERNS: [When most signals occurred]
🎯 TOP 3 TRADE SETUPS: [Highest conviction opportunities with exact entry prices]
```

---

## Volume Profile & Market Structure

### File 01: volume_profile_complete.csv

**COPY THIS PROMPT:**
```
Analyze this complete volume profile showing all price levels and their traded volume.

FILE STRUCTURE:
- price: price level
- volume: total volume traded
- buy_volume: volume from aggressive buyers
- sell_volume: volume from aggressive sellers
- delta: buy_volume - sell_volume
- trades: number of trades

ANALYSIS TASKS:
1. Calculate Point of Control (POC): price with highest volume
2. Identify Value Area High (VAH) and Low (VAL): 70% volume distribution
3. Find High Volume Nodes (HVN): prices with volume > 80th percentile
4. Find Low Volume Nodes (LVN): prices with volume < 20th percentile
5. Analyze delta at HVNs (positive = buyer dominance, negative = seller dominance)
6. Identify volume gaps between HVNs (potential fast-move zones)

OUTPUT FORMAT:
🎯 POC: [price] with [volume] - [BUYER/SELLER dominated based on delta]
📊 VALUE AREA: VAH [price] | VAL [price] | Width: [difference]
💪 BUYER ZONES (HVN + Positive Delta): [list 3-5 strongest prices]
🔻 SELLER ZONES (HVN + Negative Delta): [list 3-5 strongest prices]
⚡ LIQUIDITY VOIDS (LVNs): [price ranges with thin volume]
🛡️ KEY SUPPORT: [strongest HVNs below current price]
🚧 KEY RESISTANCE: [strongest HVNs above current price]
```

### File 02: volume_profile_hvn.csv

**COPY THIS PROMPT:**
```
Analyze High Volume Nodes showing institutional accumulation/distribution levels.

FILE STRUCTURE:
- price: HVN price level
- volume: total volume at this HVN
- buy_volume, sell_volume: volume breakdown
- delta: net buying/selling pressure
- node_type: SUPPORT_HVN or RESISTANCE_HVN

ANALYSIS TASKS:
1. Rank HVNs by volume (highest volume = strongest level)
2. Classify each HVN: buyer-dominated (delta > 0) or seller-dominated (delta < 0)
3. Find HVN clusters (multiple HVNs close together = super-strong zone)
4. Calculate distance from current price to each HVN
5. Determine if HVNs are support (below price) or resistance (above price)

OUTPUT FORMAT:
🏆 STRONGEST BUYER ZONE: [price] - [volume] with delta: [value]
🎯 STRONGEST SELLER ZONE: [price] - [volume] with delta: [value]
📍 HVN CLUSTERS: [price ranges with multiple close HVNs]
⬇️ NEAREST SUPPORT: [HVN price] at [distance] below
⬆️ NEAREST RESISTANCE: [HVN price] at [distance] above
💡 TRADE RECOMMENDATION: [direction based on HVN structure]
```

### File 03: volume_profile_lvn.csv

**COPY THIS PROMPT:**
```
Analyze Low Volume Nodes showing thin liquidity and potential fast-move zones.

FILE STRUCTURE:
- price: LVN price level
- volume: very low volume traded
- void_size: magnitude of liquidity gap
- nearest_hvn_above, nearest_hvn_below: surrounding HVNs

ANALYSIS TASKS:
1. Identify largest liquidity voids (smallest volume)
2. Calculate gap sizes between HVNs surrounding each LVN
3. Determine if price is near an LVN (breakout/breakdown imminent?)
4. Assess slippage risk if trading in LVN zones
5. Find LVNs between current price and next major HVN

OUTPUT FORMAT:
⚡ LARGEST LIQUIDITY VOIDS: [top 3 price ranges with thinnest volume]
🔼 VOID ABOVE PRICE: [range] - resistance gap to [HVN price]
🔽 VOID BELOW PRICE: [range] - support gap to [HVN price]
🎯 BREAKOUT/BREAKDOWN TARGETS: [HVN prices beyond voids]
⚠️ SLIPPAGE RISK ZONES: [LVNs to avoid for limit orders]
🚀 FAST MOVE POTENTIAL: [LVNs price must cross for next major level]
```

---

## Order Flow & Imbalances

### File 05: orderflow_imbalance_by_price.csv

**COPY THIS PROMPT:**
```
Analyze order flow imbalances showing aggressive buying vs selling at each price.

FILE STRUCTURE:
- price: price level
- bid_volume: volume hitting the bid (aggressive selling)
- ask_volume: volume hitting the ask (aggressive buying)
- imbalance_ratio: ask_volume / bid_volume
- imbalance_type: BUY_IMBALANCE, SELL_IMBALANCE, BALANCED

ANALYSIS TASKS:
1. Find extreme buy imbalances (ratio > 2.0) = strong demand zones
2. Find extreme sell imbalances (ratio < 0.5) = strong supply zones
3. Identify imbalance clusters (consecutive prices, same direction)
4. Note imbalance reversals (where type flipped)
5. Calculate net imbalance pressure across all prices

OUTPUT FORMAT:
🟢 EXTREME BUY ZONES: [prices with ratio > 2.0]
🔴 EXTREME SELL ZONES: [prices with ratio < 0.5]
📊 IMBALANCE CLUSTERS: [price ranges with sustained one-sided flow]
🔄 REVERSAL POINTS: [where imbalance flipped direction]
⚖️ NET PRESSURE: [BUY/SELL] affecting [X]% of prices
🎯 ENTRY ZONES: [best prices based on imbalance strength]
```

### File 12: liquidity_sweeps.csv

**COPY THIS PROMPT:**
```
Analyze liquidity sweeps showing stop-hunt events and potential reversal setups.

FILE STRUCTURE:
- timestamp: when sweep occurred
- sweep_price: price level swept
- direction: SWEEP_HIGH or SWEEP_LOW
- reversal_price: where price reversed after sweep
- volume_spike: volume multiple vs average
- success: TRUE if reversal occurred

ANALYSIS TASKS:
1. Identify successful sweeps (reversed after stop hunt)
2. Note sweep direction (low sweeps = bullish, high sweeps = bearish)
3. Calculate sweep success rate in this dataset
4. Find sweep clusters (same level swept multiple times)
5. Check volume_spike magnitude (larger = more stops triggered)

OUTPUT FORMAT:
✅ SUCCESSFUL LOW SWEEPS (buy after): [prices and times]
✅ SUCCESSFUL HIGH SWEEPS (sell after): [prices and times]
📊 SUCCESS RATE: [X]% of sweeps led to reversals
💥 MOST VIOLENT SWEEP: [price] with [X]x volume spike
🎯 SWEEP CLUSTERS: [multiply-swept prices = very strong levels]
💡 TRADING STRATEGY: [how to trade sweeps at these levels]
```

---

## Institutional & Smart Money

### File 15: institutional_flow.csv

**COPY THIS PROMPT:**
```
Analyze institutional flow showing smart money activity.

FILE STRUCTURE:
- timestamp: when flow occurred
- price: transaction price
- size_tier: LARGE, XLARGE, WHALE
- flow_direction: INSTITUTIONAL_BUY or INSTITUTIONAL_SELL
- volume: trade size
- price_impact: how much trade moved price

ANALYSIS TASKS:
1. Identify institutional buying periods (accumulation)
2. Identify institutional selling periods (distribution)
3. Check price_impact (low impact with large size = skillful execution)
4. Note institutional flow clusters at specific prices
5. Compare institutional vs retail direction (often opposite)

OUTPUT FORMAT:
🏦 INSTITUTIONAL BUY ZONES: [prices/times with smart money buying]
📤 INSTITUTIONAL SELL ZONES: [prices/times with smart money selling]
🐋 WHALE ACTIVITY: [largest trades and locations]
🎯 STEALTH EXECUTION: [large volume, minimal impact - very significant]
⚖️ SMART MONEY VS RETAIL: [aligned or opposed?]
💡 FOLLOW THE MONEY: [recommended direction]
```

### File 18: whale_trades.csv

**COPY THIS PROMPT:**
```
Analyze whale trades showing massive institutional orders.

FILE STRUCTURE:
- timestamp: when whale traded
- price: execution price
- size: trade size (extremely large)
- side: BUY or SELL
- price_impact: price movement from trade
- stealth_score: 0-1 (higher = more hidden)

ANALYSIS TASKS:
1. Identify whale buy zones (massive accumulation)
2. Identify whale sell zones (massive distribution)
3. Check price_impact (low despite huge size = very bullish/bearish)
4. Note stealth_score (high = sophisticated institution)
5. Find whale clusters (multiple whales at same price)

OUTPUT FORMAT:
🐋 WHALE BUY ZONES: [prices with massive buy orders]
🐳 WHALE SELL ZONES: [prices with massive sell orders]
👑 LARGEST WHALE: [size] at [price], side: [BUY/SELL]
🥷 STEALTH WHALES: [high stealth scores - most significant]
🎯 WHALE CLUSTERS: [prices with multiple whale trades]
💡 FOLLOW THE WHALE: [recommended trade direction]
```

---

## Advanced Microstructure

### File 33: vpin_analysis.csv

**COPY THIS PROMPT:**
```
Analyze VPIN (Volume-Synchronized Probability of Informed Trading) toxicity data.

FILE STRUCTURE:
- bucket: data bucket number
- timestamp: time period
- vpin: 0-1 toxicity score (>0.7 = HIGH, <0.3 = LOW)
- total_volume: volume in bucket
- price_low, price_high, price_avg: price range
- toxicity_level: HIGH, MEDIUM, LOW

ANALYSIS TASKS:
1. Identify HIGH toxicity zones (VPIN > 0.7) - avoid or trade cautiously
2. Identify LOW toxicity zones (VPIN < 0.3) - safe to trade
3. Note VPIN spikes (sudden increases = informed traders active)
4. Check price behavior during high VPIN (often precedes big moves)
5. Find low VPIN at key levels (safest entry zones)

OUTPUT FORMAT:
🚨 HIGH TOXICITY ZONES (AVOID): [price ranges with VPIN > 0.7]
✅ LOW TOXICITY ZONES (SAFE): [price ranges with VPIN < 0.3]
📈 VPIN SPIKES: [sudden informed trading activity]
⚠️ DANGER PRICES: [specific toxic levels to avoid]
🟢 SAFE ENTRY ZONES: [low VPIN at support/resistance]
📊 TOXICITY TREND: [increasing/decreasing/stable]
🚦 TRADE SAFETY RATING: [GREEN/YELLOW/RED LIGHT]
```

### File 35: kyle_lambda_amihud.csv

**COPY THIS PROMPT:**
```
Analyze Kyle's Lambda and Amihud illiquidity showing price impact risk.

FILE STRUCTURE:
- window: time window
- kyle_lambda: price impact per unit volume
- amihud_illiq: price move per volume
- price_avg, price_low, price_high: price context

ANALYSIS TASKS:
1. Find high kyle_lambda zones (trades easily move price = thin)
2. Find low kyle_lambda zones (trades don't move price = thick)
3. Check amihud_illiq for overall liquidity health
4. Identify high-impact price ranges (dangerous for large orders)
5. Find low-impact zones (safe for size execution)

OUTPUT FORMAT:
⚠️ HIGH IMPACT ZONES: [prices with high lambda - thin liquidity]
✅ LOW IMPACT ZONES: [prices with low lambda - thick liquidity]
🚨 MOST ILLIQUID: [highest amihud - avoid]
💧 MOST LIQUID: [lowest amihud - safe for size]
📊 SLIPPAGE RISK: [HIGH/MEDIUM/LOW]
💡 LARGE ORDER STRATEGY: [where to execute without moving price]
```

### File 40: trapped_traders.csv

**COPY THIS PROMPT:**
```
Analyze trapped traders showing failed positions after sweeps.

FILE STRUCTURE:
- timestamp: when traders got trapped
- price: trap price
- direction: TRAPPED_LONGS or TRAPPED_SHORTS
- volume: size of trapped position
- max_pain: how far price moved against them
- escape_occurred: did they escape profitably?

ANALYSIS TASKS:
1. Identify trapped long zones (bought breakout that failed)
2. Identify trapped short zones (sold breakdown that failed)
3. Check max_pain (larger = more trapped = stronger reversal)
4. Note if escapes occurred (or still trapped = continued pressure)
5. Find trap clusters (many traders trapped at same level)

OUTPUT FORMAT:
🪤 TRAPPED LONG ZONES: [prices where long traps occurred]
⬇️ TRAPPED SHORT ZONES: [prices where short traps occurred]
💥 MAXIMUM PAIN TRAP: [price] with [max_pain] against position
🏃 ESCAPED TRAPS: [traps that resolved]
🔒 STILL TRAPPED: [ongoing trapped positions = continued pressure]
🎯 REVERSAL ZONES: [trap locations = likely reversal points]
```

### File 42: large_size_clusters.csv

**COPY THIS PROMPT:**
```
Analyze large size clusters showing whale institutional activity.

FILE STRUCTURE:
- cluster_id: unique cluster identifier
- start_time, end_time: cluster duration
- price_low, price_high, price_avg: price range
- total_volume: aggregate large trade volume
- trade_count: number of large trades
- dominant_side: BUY or SELL
- cluster_type: ACCUMULATION or DISTRIBUTION

ANALYSIS TASKS:
1. Identify BUY clusters (institutional accumulation zones)
2. Identify SELL clusters (institutional distribution zones)
3. Rank by total_volume (largest = most significant)
4. Check trade_count (more trades = sustained interest)
5. Note clusters near support/resistance (high conviction levels)

OUTPUT FORMAT:
🟢 WHALE BUY CLUSTERS: [price ranges with accumulation]
🔴 WHALE SELL CLUSTERS: [price ranges with distribution]
👑 LARGEST CLUSTER: [price range] with [volume], side: [BUY/SELL]
📊 SUSTAINED INTEREST: [clusters with most trades]
🎯 KEY INSTITUTIONAL LEVELS: [cluster prices at technical levels]
💡 FOLLOW SMART MONEY: [recommended direction]
```

### File 43: session_microstructure.csv

**COPY THIS PROMPT:**
```
Analyze session microstructure showing VWAP, POC, and value area by session.

FILE STRUCTURE:
- session: ASIAN, LONDON, NY
- vwap: volume-weighted average price
- poc: point of control (highest volume price)
- vah, val: value area high and low
- value_area_width: VAH - VAL
- session_high, session_low: price range
- poor_high, poor_low: unfilled auction tails
- total_volume: session volume
- poc_migration: POC movement vs previous session

ANALYSIS TASKS:
1. Compare session VWAPs (trending or mean-reverting?)
2. Identify virgin POCs (untested = likely revisit)
3. Check poor highs/lows (unfilled levels = targets)
4. Note value area width (tight = balanced, wide = trending)
5. Track POC migration (directional shift = trend)

OUTPUT FORMAT:
📊 SESSION VWAPS: Asian: [price] | London: [price] | NY: [price]
🎯 VIRGIN POCs: [session] POC at [price] - likely revisit
⚡ POOR HIGHS (unfilled): [prices] - upside targets
📉 POOR LOWS (unfilled): [prices] - downside targets
📏 VALUE AREAS: [session with tightest/widest value area]
📈 POC MIGRATION: [direction and magnitude]
💡 SESSION BIAS: [which session was most bullish/bearish]
```

### File 47: delta_changepoints.csv

**COPY THIS PROMPT:**
```
Analyze delta changepoints showing order flow momentum shifts.

FILE STRUCTURE:
- time_bin: time period
- cum_delta: cumulative delta value
- slope_change: delta slope shift
- price_low, price_high, price_open, price_close, price_avg: price data

ANALYSIS TASKS:
1. Identify positive slope changes (delta improving = bullish shift)
2. Identify negative slope changes (delta weakening = bearish shift)
3. Check magnitude of slope changes (larger = stronger shift)
4. Note price behavior at changepoints (did price follow delta?)
5. Find changepoint clusters (multiple shifts = major inflection)

OUTPUT FORMAT:
📈 BULLISH CHANGEPOINTS: [times/prices where delta improved]
📉 BEARISH CHANGEPOINTS: [times/prices where delta weakened]
💥 LARGEST SHIFT: [time] at [price] with [slope_change]
🎯 INFLECTION ZONES: [prices with multiple changepoints]
✅ CONFIRMED SHIFTS: [changepoints followed by price moves]
⚠️ FALSE SIGNALS: [changepoints without price follow-through]
💡 MOMENTUM STATUS: [current delta trend]
```

### File 50: aggressive_print_runs.csv

**COPY THIS PROMPT:**
```
Analyze aggressive print runs showing rapid-fire order execution.

FILE STRUCTURE:
- run_id: unique run identifier
- run_length: number of consecutive aggressive prints
- start_time, end_time: run duration
- duration_seconds: how long run lasted
- dominant_side: BUY or SELL
- total_volume, buy_volume, sell_volume: volume breakdown
- price_start, price_end, price_low, price_high, price_range: price action
- avg_time_between_trades: trade velocity

ANALYSIS TASKS:
1. Identify longest runs (sustained aggressive activity)
2. Classify as buy runs (accumulation) or sell runs (distribution)
3. Check duration and velocity (fast = more aggressive)
4. Note price_range during run (large range = strong momentum)
5. Find runs near key levels (breakout/breakdown signals)

OUTPUT FORMAT:
🟢 AGGRESSIVE BUY RUNS: [times/prices with buy-side runs]
🔴 AGGRESSIVE SELL RUNS: [times/prices with sell-side runs]
⚡ LONGEST RUN: [run_length] prints over [duration]s, side: [BUY/SELL]
🚀 FASTEST VELOCITY: [avg_time_between_trades], price moved: [range]
🎯 RUNS AT KEY LEVELS: [runs at support/resistance]
💡 ALGO ACTIVITY: [likely automated execution patterns]
```

---

## Multi-File Analysis

### CONFLUENCE ANALYSIS PROMPT

**COPY THIS PROMPT:**
```
I have multiple order flow analysis files. Help me find high-confidence trading zones using confluence.

FILES PROVIDED:
[List which files you're uploading, e.g., "volume_profile_hvn.csv, absorption_zones.csv, whale_trades.csv"]

CONFLUENCE RULES:
- Need 4+ signals at same price level for high confidence
- Buy signals: HVN + positive delta, whale buys, absorption, low VPIN, buy imbalance
- Sell signals: HVN + negative delta, whale sells, rejection, high VPIN, sell imbalance

ANALYSIS TASKS:
1. Find price levels appearing in multiple files
2. Check signal agreement (all bullish or all bearish?)
3. Rank zones by number of confluent signals
4. Note any conflicting signals (red flag)
5. Assess toxicity (VPIN) at confluence zones
6. Calculate distance to nearest confluence zones

OUTPUT FORMAT:
🎯 HIGHEST CONFLUENCE BUY ZONE: [price] with [X] signals
   - Signals: [list all supporting signals]
   - Confidence: [HIGH/MEDIUM based on signal count]
   
🎯 HIGHEST CONFLUENCE SELL ZONE: [price] with [X] signals
   - Signals: [list all supporting signals]
   - Confidence: [HIGH/MEDIUM based on signal count]

⚠️ CONFLICTING ZONES: [prices with mixed signals - avoid]

📊 ZONE RANKING:
1. [price] - [X] signals - [BUY/SELL]
2. [price] - [X] signals - [BUY/SELL]
3. [price] - [X] signals - [BUY/SELL]

🚦 TOXICITY CHECK: [safe/caution/avoid for top zones]

🎯 NEAREST TRADEABLE ZONE: [price] at [distance] from current
```

### RISK ASSESSMENT PROMPT

**COPY THIS PROMPT:**
```
Analyze the following files for risk factors and warning signs.

FILES PROVIDED:
[List files, should include: vpin_analysis, trapped_traders, liquidity_voids, fake_moves]

RISK FACTORS TO CHECK:
1. High VPIN (>0.7) = informed traders active, avoid
2. Trapped traders = positions under pressure
3. Liquidity voids = slippage risk
4. Fake moves = trap zones
5. Thin liquidity = execution risk

ANALYSIS TASKS:
1. Identify high-risk price levels (multiple risk factors)
2. Find safe zones (low toxicity, good liquidity)
3. Note ongoing traps (continued pressure expected)
4. Check for fake-move zones (avoid these)
5. Assess overall market safety

OUTPUT FORMAT:
🚨 HIGH-RISK ZONES (AVOID):
- [price]: [list risk factors present]

✅ SAFE ZONES (GREEN LIGHT):
- [price]: [why it's safe to trade]

⚠️ CAUTION ZONES (REDUCE SIZE):
- [price]: [moderate risk factors]

🔍 ACTIVE RISKS:
- Trapped traders at [prices]
- High VPIN at [prices]
- Liquidity voids at [ranges]
- Fake move zones at [prices]

🚦 OVERALL MARKET SAFETY: [GREEN/YELLOW/RED]

�� TRADING RECOMMENDATIONS:
- Safe to trade: [YES/NO/WITH CAUTION]
- Position sizing: [FULL/REDUCED/MINIMAL]
- Best zones: [list safest entry points]
```

---

## Usage Tips

1. **Start with Master File (00)** for overview
2. **Check VPIN (33) first** for safety - never trade high-toxicity zones
3. **Use confluence** - combine 4+ files for high-confidence setups
4. **Verify with volume profile** - ensure zones have institutional participation
5. **Check for traps** - avoid zones with trapped traders or fake moves
6. **Layer your analysis** - volume → order flow → smart money → microstructure

## Example Workflow

1. Upload `00_MASTER_TRADING_SIGNALS.csv` - get signal overview
2. Upload `01_volume_profile_complete.csv` - find POC, VAH, VAL
3. Upload `33_vpin_analysis.csv` - check toxicity
4. Upload `42_large_size_clusters.csv` - find whale zones
5. Use confluence prompt with all files together
6. Use risk assessment prompt before trading

---

**Remember:** AI analysis is a tool, not a guarantee. Always verify signals with your own analysis and risk management.

