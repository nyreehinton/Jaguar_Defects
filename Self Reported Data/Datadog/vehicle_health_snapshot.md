# Vehicle Health Snapshot

## Charging voltage

- **Status:** ACTION
- **Key metrics:** Median 12.09 V while running
- **Notes:** Expected 13.8–14.4 V with engine running.

## Coolant temperature

- **Status:** OK
- **Key metrics:** Mean 210.2°F (min 210.0, max 212.0)
- **Notes:** Typical operating 180–220°F; >230°F is hot.

## MAF–RPM coupling

- **Status:** ACTION
- **Key metrics:** Pearson r = 0.33
- **Notes:** Strong correlation expected; weak correlation can indicate airflow or sensor issues.

## Fuel rail pressure

- **Status:** INFO
- **Key metrics:** 421–2686 psi (mean 1069)
- **Notes:** Normal varies by engine/system; use spec for precise check.

## Manifold absolute pressure

- **Status:** INFO
- **Key metrics:** 11.0–51.3 (mean 19.0)
- **Notes:** Units may be inHg or kPa depending on logger settings.

## Catalyst B1S1 temp

- **Status:** INFO
- **Key metrics:** 1259–1554 °F
- **Notes:** High under load is expected.

## Catalyst B1S2 temp

- **Status:** INFO
- **Key metrics:** 1327–1402 °F
- **Notes:** Downstream cat temp usually lower/smoother than upstream.

## Accel/Brake

- **Status:** INFO
- **Key metrics:** Peak accel 2.50 m/s², peak brake -2.15 m/s²
- **Notes:** Based on finite differences of speed vs. time.

## Data quality

- **Status:** OK
- **Key metrics:** Missing values ≈ 1.7%
- **Notes:** Rows: 27, Cols: 26
