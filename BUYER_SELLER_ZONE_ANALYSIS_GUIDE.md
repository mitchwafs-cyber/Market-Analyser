# Buyer & Seller Zone Analysis Guide
## How to Identify Trading Zones from Each Output File

This guide provides specific analysis prompts for each of the 59 output files to help you identify precise buyer and seller zones for trading decisions.

---

## 📊 TIER 1: Core Market Structure Analysis (Files 1-34)

### **Files 01-11: Volume Profile Analysis**
**Columns:** price, volume, cumulative_volume, percentage, POC, VAH, VAL

**Analysis Prompts:**
- **BUYER ZONES**: Look for price levels with high volume BELOW current price where cumulative_volume shows accumulation. Focus on VAL (Value Area Low) as support.
- **SELLER ZONES**: Look for price levels with high volume ABOVE current price where distribution occurred. Focus on VAH (Value Area High) as resistance.
- **KEY LEVELS**: POC (Point of Control) = strongest acceptance zone. Price tends to return here.

**Interpretation:**
```
If price > POC → Buyers in control, POC becomes support
If price < POC → Sellers in control, POC becomes resistance
High volume at specific price = strong acceptance = likely support/resistance
```

---

### **Files 12-16: Delta Profile Analysis**
**Columns:** price, buy_volume, sell_volume, delta, cumulative_delta

**Analysis Prompts:**
- **BUYER ZONES**: Positive delta (buy_volume > sell_volume) at price levels = aggressive buying. High cumulative_delta = sustained buying pressure.
- **SELLER ZONES**: Negative delta (sell_volume > buy_volume) at price levels = aggressive selling. Low/negative cumulative_delta = sustained selling pressure.

**Interpretation:**
```
Positive delta clusters below current price = buyer support zones
Negative delta clusters above current price = seller resistance zones
Delta divergence (price up, delta down) = weakness, potential reversal
```

---

### **Files 17-22: Auction Analysis (Initial Balance, Failures, Excess)**
**Columns:** session, ib_high, ib_low, ib_range, auction_type, rotation_count, acceptance

**Analysis Prompts:**
- **BUYER ZONES**: Failed auction lows (price rejected below ib_low) = buyers defended. Excess lows with high volume = absorption.
- **SELLER ZONES**: Failed auction highs (price rejected above ib_high) = sellers defended. Excess highs with high volume = distribution.

**Interpretation:**
```
Acceptance above IB = buyers in control (long above ib_high)
Acceptance below IB = sellers in control (short below ib_low)
Excess = one-timeframe behavior, expect continuation until absorbed
```

---

### **Files 23-27: Stacked Imbalances & Unfilled Orders**
**Columns:** price_level, imbalance_count, consecutive_levels, side, volume_imbalance

**Analysis Prompts:**
- **BUYER ZONES**: 3+ consecutive BUY imbalances = strong demand area. Unfilled buy orders = potential support magnet.
- **SELLER ZONES**: 3+ consecutive SELL imbalances = strong supply area. Unfilled sell orders = potential resistance magnet.

**Interpretation:**
```
Stacked buy imbalances below price = support zones (buyers waiting)
Stacked sell imbalances above price = resistance zones (sellers waiting)
Unfilled orders = unfinished business, price likely to revisit
```

---

### **Files 28-34: CVD, Delta Waves, VWAP**
**Columns:** timestamp, cvd, delta_wave, vwap, price

**Analysis Prompts:**
- **BUYER ZONES**: Rising CVD + price near/below VWAP = buyers accumulating at value. Positive delta waves = buying momentum.
- **SELLER ZONES**: Falling CVD + price near/above VWAP = sellers distributing at premium. Negative delta waves = selling momentum.

**Interpretation:**
```
Price < VWAP = undervalued (buyer zone if CVD rising)
Price > VWAP = overvalued (seller zone if CVD falling)
VWAP crossovers = momentum shifts (buyers/sellers taking control)
```

---

## 🚀 TIER 2: Advanced Microstructure Analysis (Files 35-59)

### **GROUP A: Institutional Money Flow** 🐋

#### **File 35: Kyle Lambda & Amihud Illiquidity**
**Columns:** timestamp, kyle_lambda, amihud_illiquidity, price_avg, price_low, price_high

**Analysis Prompts:**
- **BUYER ZONES**: High kyle_lambda (high price impact) at low prices = large buyers stepping in. Look for price_low where illiquidity spiked.
- **SELLER ZONES**: High kyle_lambda at high prices = large sellers distributing. Look for price_high where illiquidity spiked.

**Interpretation:**
```
High illiquidity + price_low = institutional buying (accumulation zone)
High illiquidity + price_high = institutional selling (distribution zone)
Lambda spikes = informed traders (follow their direction)
```

---

#### **File 36: Impact Summary**
**Columns:** metric, value, interpretation

**Analysis Prompts:**
- **BUYER ZONES**: "High Impact Buy Pressure" or "Toxic Buy Flow" = institutional accumulation zones.
- **SELLER ZONES**: "High Impact Sell Pressure" or "Toxic Sell Flow" = institutional distribution zones.

**Interpretation:**
```
Use this as confirmation for zones identified in other files
Toxic flow = informed traders, fade against retail at these levels
```

---

#### **File 41: Size-Tier Statistics**
**Columns:** size_tier, trade_count, volume_share, price_low, price_high, price_avg, imbalance

**Analysis Prompts:**
- **BUYER ZONES**: p99+ tier (whales) with positive imbalance at price_low = institutional buy zone.
- **SELLER ZONES**: p99+ tier (whales) with negative imbalance at price_high = institutional sell zone.
- **FADE ZONES**: p0-p50 tier (retail) heavy zones = fade retail (trade opposite).

**Interpretation:**
```
Follow p99+ tier (institutions), fade p0-p50 tier (retail)
Whale buy clusters at lows = support zones
Whale sell clusters at highs = resistance zones
```

---

#### **File 42: Large Size Clusters**
**Columns:** cluster_id, trade_count, cluster_type, price_low, price_high, price_avg, price_range

**Analysis Prompts:**
- **BUYER ZONES**: LARGE_BUY_CLUSTER at price_low values = institutional support. Expect bounces here.
- **SELLER ZONES**: LARGE_SELL_CLUSTER at price_high values = institutional resistance. Expect rejections here.

**Interpretation:**
```
Clusters = institutional conviction levels
BUY clusters below price = support (enter long)
SELL clusters above price = resistance (enter short)
Clusters at S/R confluence = high-probability zones
```

---

### **GROUP B: Liquidity & Value Magnets** 🧲

#### **File 43: Session Microstructure**
**Columns:** session, vwap, poc, vah, val, session_high, session_low, poor_high, poor_low

**Analysis Prompts:**
- **BUYER ZONES**: Poor lows (single prints) = weak low, expect fill. VAL = session support. Price < VWAP = undervalued.
- **SELLER ZONES**: Poor highs (single prints) = weak high, expect fill. VAH = session resistance. Price > VWAP = overvalued.

**Interpretation:**
```
Trade toward unfilled poor highs/lows (magnets)
VAL/VAH = session acceptance boundaries (support/resistance)
Virgin POCs from old sessions = strong magnets (price will revisit)
```

---

#### **File 44: Virgin POCs**
**Columns:** session, POC, virgin_status, distance_from_current

**Analysis Prompts:**
- **BUYER ZONES**: Virgin POCs below current price = magnets pulling price down (enter short to POC, then reverse long).
- **SELLER ZONES**: Virgin POCs above current price = magnets pulling price up (enter long to POC, then reverse short).

**Interpretation:**
```
Virgin POCs = unfinished business, price WILL revisit
Trade TO the virgin POC (momentum trade)
Trade FROM the virgin POC once tested (reversal trade)
Closest virgin POC = highest probability target
```

---

#### **Files 48-49: Liquidity Voids**
**Columns:** void_start, void_end, price_mid, current_price, distance_from_current, volume_in_void

**Analysis Prompts:**
- **BUYER ZONES**: Voids below current price = air pockets. If price enters, expect fast drop through void to opposite edge (sell zone → buy zone).
- **SELLER ZONES**: Voids above current price = air pockets. If price enters, expect fast rise through void to opposite edge (buy zone → sell zone).

**Interpretation:**
```
Voids = low volume areas, price moves fast through them
Enter trades at void EDGES, not inside voids
Bottom of void below price = support target
Top of void above price = resistance target
```

---

### **GROUP C: Reversal & Trap Zones** ⚠️

#### **File 37: Absorption/Rejection Bars**
**Columns:** timestamp, open, high, low, close, volume, type

**Analysis Prompts:**
- **BUYER ZONES**: ABSORPTION bars at lows (close > open, high volume) = buyers absorbed sell pressure. Support zone.
- **SELLER ZONES**: REJECTION bars at highs (close < high, volume spike) = sellers rejected buyers. Resistance zone.

**Interpretation:**
```
Absorption at lows = buyers defended (enter long)
Rejection at highs = sellers defended (enter short)
Absorption + sweep low = high-conviction buy zone
Rejection + sweep high = high-conviction sell zone
```

---

#### **Files 38-39: Enhanced Absorption/Rejection Zones**
**Columns:** zone_id, open, high, low, close, volume, zone_type, support_resistance

**Analysis Prompts:**
- **BUYER ZONES**: absorption_zone with support_resistance = "SUPPORT" at low prices = enter long.
- **SELLER ZONES**: rejection_zone with support_resistance = "RESISTANCE" at high prices = enter short.

**Interpretation:**
```
Absorption zones = demand areas (buyers present)
Rejection zones = supply areas (sellers present)
Zone retests = high-probability entries (enter on second touch)
```

---

#### **File 40: Trapped Traders**
**Columns:** sweep_price, mfe, mae, efficiency, outcome, price

**Analysis Prompts:**
- **BUYER ZONES**: Sweep lows with positive MFE (maximum favorable excursion) = failed trap, buyers win. Enter long above sweep_price.
- **SELLER ZONES**: Sweep highs with negative MAE (maximum adverse excursion) = failed trap, sellers win. Enter short below sweep_price.

**Interpretation:**
```
Sweeps with high efficiency = successful traps (fade the sweep)
Failed sweeps (low efficiency) = strong conviction (trade with the reversal)
Trapped sellers at highs = resistance zones
Trapped buyers at lows = support zones
```

---

#### **Files 57-59: Fake Moves, Squeezes, Conviction Moves**
**Columns:** timestamp, price, volume, move_type, efficiency

**Analysis Prompts:**
- **BUYER ZONES**: 
  - Fake sell moves (false breakdowns) = buy zones
  - Thin liquidity squeezes downward = buy at squeeze bottom
  - Strong conviction buy moves = support at origin
  
- **SELLER ZONES**: 
  - Fake buy moves (false breakouts) = sell zones
  - Thin liquidity squeezes upward = sell at squeeze top
  - Strong conviction sell moves = resistance at origin

**Interpretation:**
```
Fake moves = traps, fade them (enter opposite direction)
Squeezes = forced moves, enter at ends (reversal zones)
Conviction moves = genuine, support/resist at start of move
```

---

### **GROUP D: High-Toxicity Risk Zones** ☠️

#### **File 33: VPIN Analysis**
**Columns:** bucket, vpin, total_volume, price_low, price_high, toxicity_level

**Analysis Prompts:**
- **AVOID ZONES**: High VPIN (>0.7) + HIGH toxicity = informed traders active. Price is toxic, avoid trading or trade WITH toxicity direction.
- **SAFE ZONES**: Low VPIN (<0.3) + LOW toxicity = fair price, safe to trade mean reversion.

**Interpretation:**
```
HIGH toxicity at price_low = informed sellers exiting (don't buy)
HIGH toxicity at price_high = informed buyers exiting (don't sell)
Trade WITH toxicity direction, not against it
Wait for toxicity to clear before entering counter-trend
```

---

#### **File 50: Aggressive Print Runs**
**Columns:** run_id, start_time, end_time, dominant_side, price_start, price_end, price_low, price_high

**Analysis Prompts:**
- **BUYER ZONES**: BUY-dominated runs ending at price_end = buyers exhausted. Expect pullback to price_start (sell zone).
- **SELLER ZONES**: SELL-dominated runs ending at price_end = sellers exhausted. Expect bounce to price_start (buy zone).

**Interpretation:**
```
Aggressive runs = algo activity, expect exhaustion
Enter AGAINST the run at price_end (reversal zones)
Enter WITH the run on pullbacks to price_start (continuation zones)
High frequency = algo accumulation/distribution
```

---

### **GROUP E: Timing & Pace** ⏱️

#### **File 51: Pulse Events**
**Columns:** window_start, pulse_intensity, price_low, price_high, price_avg, price_range

**Analysis Prompts:**
- **BUYER ZONES**: High pulse intensity at price_low = surge of buying. Expect support at price_low.
- **SELLER ZONES**: High pulse intensity at price_high = surge of selling. Expect resistance at price_high.

**Interpretation:**
```
Pulses = sudden order flow surges
Buy pulses at lows = support (enter long)
Sell pulses at highs = resistance (enter short)
Pulse clusters = institutional activity zones
```

---

### **GROUP F: Delta Flow Dynamics** 📈📉

#### **File 47: Delta Changepoints**
**Columns:** time_bin, cum_delta, slope_change, price_low, price_high, price_open, price_close

**Analysis Prompts:**
- **BUYER ZONES**: Positive slope_change (cum_delta turning up) at price_low = buyers taking control. Enter long.
- **SELLER ZONES**: Negative slope_change (cum_delta turning down) at price_high = sellers taking control. Enter short.

**Interpretation:**
```
Slope changes = momentum shifts (follow the new direction)
Positive change at lows = reversal to upside (buy zone)
Negative change at highs = reversal to downside (sell zone)
Price_open to price_close shows directional conviction
```

---

### **GROUP G: Price Impact Asymmetry** ⚖️

#### **Files 54-55: Buy/Sell Impact by Distance**
**Columns:** distance_bucket, avg_impact, price_low, price_high, price_avg, trade_count

**Analysis Prompts:**
- **BUYER ZONES**: High buy impact at specific distance_bucket = strong buying at that price range. Look at price_low for support.
- **SELLER ZONES**: High sell impact at specific distance_bucket = strong selling at that price range. Look at price_high for resistance.

**Interpretation:**
```
High impact = significant trader activity
Buy impact above average = demand zone (support)
Sell impact above average = supply zone (resistance)
Distance from VWAP/POC shows value perception
```

---

### **GROUP H: Regime Detection** 🔄

#### **File 56: Regime Summary**
**Columns:** regime, count, price_low, price_high, price_avg, volatility

**Analysis Prompts:**
- **BUYER ZONES**: "STRONG_CONVICTION" or "BULLISH" regimes at price_low = sustained buying. Support zone.
- **SELLER ZONES**: "STRONG_CONVICTION" or "BEARISH" regimes at price_high = sustained selling. Resistance zone.
- **AVOID**: "THIN_LIQUIDITY" or "FAKE_MOVE" regimes = unreliable zones.

**Interpretation:**
```
Strong conviction regimes = reliable zones (enter here)
Fake move regimes = trap zones (fade these)
High volatility regimes = wider stops needed
Trade WITH the dominant regime, not against it
```

---

### **GROUP I: Volume Shape Analysis** 📊

#### **Files 45-46: Volume/Delta Shape Stats**
**Columns:** time_bin/price_bin, skew, kurtosis, open, high, low, close, avg

**Analysis Prompts:**
- **BUYER ZONES**: Positive skew (right tail) + high kurtosis at low prices = explosive buying. Enter long at price_low.
- **SELLER ZONES**: Negative skew (left tail) + high kurtosis at high prices = explosive selling. Enter short at price_high.

**Interpretation:**
```
Positive skew = buying pressure building (buyer zone forming)
Negative skew = selling pressure building (seller zone forming)
High kurtosis = concentrated activity (strong conviction)
Use with price OHLC to identify exact entry levels
```

---

## 🎯 PRACTICAL WORKFLOW: How to Use These Files Together

### **Step 1: Identify Key Levels (Foundation)**
1. **File 01-11** (Volume Profile): Find POC, VAH, VAL
2. **File 43** (Session Microstructure): Find VWAP, session POC
3. **File 44** (Virgin POCs): Find untested POC magnets

### **Step 2: Confirm with Institutional Activity**
4. **File 42** (Large Size Clusters): Where are whales buying/selling?
5. **File 41** (Size-Tier Stats): What's the p99+ tier doing?
6. **File 35** (Kyle Lambda): Where is high-impact flow?

### **Step 3: Check for Absorption/Rejection**
7. **Files 37-39** (Absorption/Rejection): Are zones defended?
8. **File 40** (Trapped Traders): Are there failed sweeps?

### **Step 4: Identify Liquidity Conditions**
9. **Files 48-49** (Liquidity Voids): Where are the air pockets?
10. **File 33** (VPIN): Is the flow toxic?

### **Step 5: Time Your Entry**
11. **File 47** (Delta Changepoints): Momentum shift confirmation
12. **File 50** (Aggressive Runs): Wait for exhaustion
13. **File 51** (Pulse Events): Enter on pulse clusters

### **Step 6: Validate with Regime**
14. **File 56** (Regime Summary): Are we in a tradeable regime?
15. **Files 57-59** (Fake/Conviction Moves): Is this move genuine?

---

## 📋 ZONE CONFLUENCE CHECKLIST

**HIGH-PROBABILITY BUY ZONE** (Need 4+ signals):
- [ ] Volume Profile POC/VAL at this price
- [ ] Positive delta cluster (File 12-16)
- [ ] Large buy cluster (File 42)
- [ ] Absorption bar (File 37)
- [ ] Failed sweep low (File 40)
- [ ] Virgin POC below (File 44)
- [ ] VWAP support (File 43)
- [ ] Positive delta changepoint (File 47)
- [ ] Low toxicity (File 33)
- [ ] Strong conviction regime (File 56)

**HIGH-PROBABILITY SELL ZONE** (Need 4+ signals):
- [ ] Volume Profile POC/VAH at this price
- [ ] Negative delta cluster (File 12-16)
- [ ] Large sell cluster (File 42)
- [ ] Rejection bar (File 37)
- [ ] Failed sweep high (File 40)
- [ ] Virgin POC above (File 44)
- [ ] VWAP resistance (File 43)
- [ ] Negative delta changepoint (File 47)
- [ ] High toxicity indicating exit (File 33)
- [ ] Strong conviction regime (File 56)

---

## ⚠️ WARNING SIGNS: When NOT to Trade

**AVOID TRADING WHEN:**
1. **File 33** shows HIGH toxicity (VPIN > 0.7) = informed traders active
2. **File 57** shows "FAKE_MOVE" at your zone = trap setup
3. **File 58** shows "THIN_LIQUIDITY_SQUEEZE" = forced move, not organic
4. **File 50** shows aggressive runs without exhaustion = algo still active
5. **File 56** shows regime as "CHOPPY" or "UNCERTAIN" = no edge
6. **Files 48-49** show you're inside a liquidity void = no support/resistance
7. **File 40** shows recent traps at your zone = other traders already trapped

---

## 🚀 QUICK REFERENCE: File-to-Zone Type Mapping

| File # | Primary Use | Buyer Zone Signal | Seller Zone Signal |
|--------|-------------|-------------------|-------------------|
| 01-11 | Key Levels | High volume at lows, VAL | High volume at highs, VAH |
| 12-16 | Delta Flow | Positive delta clusters | Negative delta clusters |
| 33 | Risk Assessment | Low VPIN at lows | High VPIN (avoid longs) |
| 35-36 | Institutional | High impact buys at lows | High impact sells at highs |
| 37-39 | Absorption | Absorption bars at lows | Rejection bars at highs |
| 40 | Sweep Analysis | Failed low sweeps | Failed high sweeps |
| 41-42 | Whale Activity | p99+ buy clusters at lows | p99+ sell clusters at highs |
| 43-44 | Value Areas | Price < VWAP, virgin POCs below | Price > VWAP, virgin POCs above |
| 47 | Momentum Shifts | Positive slope change at lows | Negative slope change at highs |
| 48-49 | Liquidity | Void edges below (targets) | Void edges above (targets) |
| 50-51 | Timing | BUY run exhaustion, pulses | SELL run exhaustion, pulses |
| 54-55 | Impact Zones | High buy impact at distance | High sell impact at distance |
| 56 | Regime Filter | Bullish/conviction regime | Bearish/conviction regime |
| 57-59 | Move Quality | Fake sell moves, squeezes | Fake buy moves, squeezes |

---

## 💡 PRO TIPS

1. **Start with File 01 (Volume Profile)**: This is your foundation. All other analyses confirm or refine these levels.

2. **Confluence is King**: A zone with 5+ signals from different file types is significantly more reliable than a single indicator.

3. **Follow the Whales (Files 41-42)**: When institutional size-tier (p99+) aligns with your zone, conviction increases dramatically.

4. **Respect Toxicity (File 33)**: High VPIN means informed traders know something you don't. Don't fight toxic flow.

5. **Virgin POCs (File 44) are Magnets**: Treat these as high-probability targets, not just support/resistance.

6. **Failed Sweeps (File 40) are Gold**: When a sweep fails immediately, it's one of the highest-conviction signals.

7. **Delta Changepoints (File 47) Confirm Reversals**: Don't enter a reversal trade until delta momentum shifts.

8. **Voids (Files 48-49) Accelerate**: Price moves FAST through voids. Enter at edges, not in the middle.

9. **Fake Moves (File 57) are Traps**: If a move is classified as fake, fade it immediately.

10. **Regime Matters (File 56)**: Don't trade mean reversion in trending regimes. Don't trade trends in ranging regimes.

---

## 📞 DECISION TREE

```
Is there a Virgin POC nearby? (File 44)
├─ YES → Price will likely trade there (high-probability target)
└─ NO → Continue...

Is VPIN HIGH (>0.7)? (File 33)
├─ YES → Toxic flow, wait or trade WITH toxicity
└─ NO → Continue...

Are there Whale Clusters? (File 42)
├─ BUY clusters at lows → BUYER ZONE (enter long)
├─ SELL clusters at highs → SELLER ZONE (enter short)
└─ NO clusters → Continue...

Is there Absorption/Rejection? (Files 37-39)
├─ Absorption at lows → BUYER ZONE (enter long)
├─ Rejection at highs → SELLER ZONE (enter short)
└─ NO absorption → Continue...

Did a Sweep Fail? (File 40)
├─ Failed low sweep → BUYER ZONE (strong long)
├─ Failed high sweep → SELLER ZONE (strong short)
└─ NO failed sweep → Continue...

Is Delta Changing? (File 47)
├─ Positive change at lows → BUYER ZONE (momentum long)
├─ Negative change at highs → SELLER ZONE (momentum short)
└─ NO delta change → Wait for setup
```

---

## 🎓 LEARNING PATH

**Beginner**: Focus on Files 01-11, 37-39, 42-44
- Master volume profile, absorption/rejection, whale activity, value areas

**Intermediate**: Add Files 12-16, 40, 47, 56
- Understand delta flow, trapped traders, momentum shifts, regimes

**Advanced**: Incorporate Files 33, 35-36, 48-51, 54-55, 57-59
- Toxicity assessment, institutional flow, liquidity dynamics, move quality

---

**Remember**: No single file gives you all the answers. The power is in combining multiple analyses to find high-confluence zones where buyers and sellers have previously shown conviction. These zones are where the next battle will likely occur.

Good luck trading! 🚀
