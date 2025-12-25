# Technical Communications Related to VVT:VCT Monitor Failure (MID 35)

*The sources identify specific technical communications, campaigns, and bulletins related to the powertrain issues observed in the Mode 6 report, particularly concerning the Variable Valve Timing (VVT) system and the Evaporative Emissions (EVAP)/Purge system. Additionally, related engine communications regarding cooling are included, as they affect the 2.0L Ingenium engine (AJ20P) of the 2020 F-TYPE.*

The issues identified in the Mode 6 report were:

1. **VVT Monitor Bank 1 (MID: 35 / TID: 80)**: Failed test.
2. **Purge Flow Monitor (MID: 3D / TID: 8E)**: Test not complete.

*Here is a list of relevant communications, grouped by technical issue:*

## Technical Communications Related to VVT/VCT Monitor Failure (MID 35)

*The VVT Monitor failures (potentially linked to DTCs P0011, P0014, P000A, P000B, P054A, P0016) are caused by insufficient wear resistance of the Variable Camshaft Timing (VCT) solenoid bush. The required action is to replace the VCT solenoids.*

| Type                             | ID/Code                    | Issue Description & Affected Models                                                                                                                                                                                  | Source Citations |
| :------------------------------- | :------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------------- |
| **Service Action (CSP)**         | **H299**                   | **Variable Camshaft Timing (VCT) Solenoids** replacement program. Affects 2018-2020MY F-TYPE, F-PACE, XE, XF, E-PACE fitted with 4cyl AJ20P engines, to prevent premature wear, MIL, or possible no-start condition. |                  |
| **Technical Bulletin (TSB)**     | **JLRTB02023NAS1**         | Concerns related to MIL illumination and multiple VCT DTCs (e.g., P0011-71, P0014-71, P054A-00) due to VCT solenoid bush wear. Superseded by NAS2.                                                                   |                  |
| **Technical Bulletin (TSB)**     | **JLRTB02023NAS2**         | Reissued bulletin (Mar 2020) detailing VCT solenoid renewal procedure for F-TYPE (2018-2020MY, K45252-K65706 VIN range) and other models equipped with the Ingenium I4 2.0L Petrol engine.                           |                  |
| **Workshop Aftersales Bulletin** | **NAS20.11.001 (Issue 3)** | Update for VCT solenoid replacement procedure (May 2021). Confirms replacement is necessary due to driveability flat spots, MIL, or increased induction noise.                                                       |                  |

### Technical Communications Related to Purge Flow Monitor Incomplete/EVAP DTCs

The Purge Flow Monitor showing "Test not complete" (MID 3D / TID 8E) is related to the EVAP system. This condition is often associated with DTC P2402-00 or P144B-00.

| Type                              | ID/Code            | Issue Description & Affected Models                                                                                                                                                                                                                                   | Source Citations |
| :-------------------------------- | :----------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------------- |
| **Special Service Message (SSM)** | **SSM 74605**      | **Check Engine MIL with DTC P2402-00** stored. Affects 2019-2020 MY gasoline vehicles (including F-TYPE). Recommended repair is inspecting the DMTL circuit and replacing the full carbon canister assembly (which includes the DMTL pump) if no root cause is found. |                  |
| **Technical Topic (Powertrain)**  | **(DTC P144B-00)** | Check Engine MIL (18MY onwards F-TYPE, E-PACE, F-PACE, XE, XF). Caused by a **blocked or disconnected purge line** or insufficient vacuum from the venturi in the intake tube.                                                                                        |                  |

### Related Communications for 2.0L Engine Powertrain

The 2020 F-TYPE 2.0L Ingenium engine is also subject to service actions addressing excessive cooling fan noise, which may be mistaken for another engine issue.

| Type                              | ID/Code            | Issue Description & Affected Models                                                                                                                                                                                                                                                                        | Source Citations |
| :-------------------------------- | :----------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------------- |
| **Service Action (CSP)**          | **H291**           | **Ingenium I4 2.0L Petrol Coolant Pump Operation.** PCM software update to prevent excessive engine cooling fan noise and cooling system degradation (associated with DTCs P2B61-73 and P26CB-72). Affects 2019-2020MY F-TYPE and other Jaguar models.                                                     |                  |
| **Special Service Message (SSM)** | **SSM 74857**      | Issued after H291 suspension (June 2020), providing guidance on updating the PCM software for the coolant pump issue until the full campaign was re-issued (July 2020).                                                                                                                                    |                  |
| **Technical Bulletin (TSB)**      | **JLRTB02030NAS1** | Original TSB (Mar 2020) detailing the renewal of the variable coolant pump due to an internal diversion shroud failure causing loud noise/high speed fan operation (DTCs P2B61-73 and P26CB-72). This TSB was later discussed for revision and removed from publication due to the software issue in H291. |                  |

---

The sources identify several bulletins, campaigns, and communications related to the two primary issues found in the Mode 6 report—Variable Valve Timing (VVT) failure and the incomplete Purge Flow monitor—as well as other relevant powertrain concerns for the 2020 Jaguar F-TYPE 2L L4 (Ingenium I4 2.0L Petrol engine, designated AJ20P).

Here are the specific communications related to these issues:

### 1. Variable Valve Timing (VVT)/VCT Monitor Failure (Related to MID 35 / TID 80)

This failure is tied to known issues involving premature wear of the Variable Camshaft Timing (VCT) solenoids, often resulting in a Malfunction Indicator Lamp (MIL) illumination and Diagnostic Trouble Codes (DTCs) such as P0011-71, P0014-71, P000A-00, P000B-00, or P054A-00.

| Type                     | ID/Code                  | Issue Description & Affected Models                                                                                                                                                                                                                     | Source Citations |
| :----------------------- | :----------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :--------------- |
| **Service Action (CSP)** | **H299**                 | **Variable Camshaft Timing (VCT) Solenoids.** Required replacement of VCT solenoids (both intake and exhaust) to prevent premature wear, MIL, or possible no-start condition. Affects 2018-2020 MY F-TYPE (INGENIUM I4 2.0L Petrol, VIN K51500-K66534). |                  |
| **Technical Bulletin**   | **JLRTB02023NAS1**       | **MIL Illuminated** on the Instrument Panel Cluster (IPC). Applies to 2018-2020 F-TYPE (VIN K45252-K65706) and other Ingenium I4 2.0L Petrol vehicles. Involved VCT solenoid renewal. (Superseded by NAS2).                                             |                  |
| **Technical Bulletin**   | **JLRTB02023NAS2**       | **Supersedes NAS1.** Addresses MIL illumination with potential DTCs (P0011-71, P0014-71, P000A-00, P000B-00) and minor performance/accelerator response loss. Outlines VCT solenoid renewal procedure. Affects 2018-2020 F-TYPE (VIN K45252-K65706).    |                  |
| **Aftersales Bulletin**  | **NAS20.11.001 Issue 3** | Update reinforcing the need to replace VCT solenoids for vehicles exhibiting MIL/VCT DTCs (e.g., P054A-00, P0014-00, P000B-00), driveability flat spots, increased induction noise, or small reduction in performance.                                  |                  |
| **Technical Note**       | **(Friction Washers)**   | Notes that if service work is performed involving VVT removal on 2.0L GTDi Engines, new **friction washers MUST be added**, although they were not installed during initial engine assembly.                                                            |                  |

### 2. Purge Flow Monitor Incomplete (Related to MID 3D / TID 8E)

Issues with the Purge Flow monitor often relate to the EVAP system, diagnosed via DTCs P2402-00 (DMTL system) or P144B-00 (purge line/venturi fault).

| Type                              | ID/Code            | Issue Description & Affected Models                                                                                                                                                                                                                 | Source Citations |
| :-------------------------------- | :----------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------------- |
| **Special Service Message (SSM)** | **SSM 74605**      | **Check Engine MIL with DTC P2402-00** stored. Affects 2019-2020 MY gasoline vehicles, including the F-TYPE (X152). Action: Inspect DMTL circuit; if no root cause is found, **replace the full carbon canister assembly which includes the DMTL**. |                  |
| **Technical Topic**               | **(DTC P144B-00)** | **Check Engine MIL with DTC P144B-00** stored. Affects 18MY onward F-TYPE (AJ20P4 or AJ20P6 engines). Cause: Can be a **blocked or disconnected purge line** or insufficient vacuum generated by the venturi in the intake tube.                    |                  |

### 3. Related Powertrain/Engine Control Communications

These communications address other potential issues specific to the 2019-2020 MY Ingenium I4 2.0L Petrol engine (AJ20P) fitted in the F-TYPE, including cooling and idle concerns.

| Type                              | ID/Code                    | Issue Description & Affected Models                                                                                                                                                                                                                        | Source Citations |
| :-------------------------------- | :------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------------- |
| **Service Action (CSP)**          | **H291**                   | **Ingenium I4 2.0L Petrol Coolant Pump Operation.** Requires PCM software update to prevent excessive engine cooling fan noise and cooling system degradation (associated with DTCs P2B61-73 and P26CB-72). Affects 2019-2021 F-TYPE (VIN K60505-onwards). |                  |
| **Special Service Message (SSM)** | **SSM 74857**              | Guidance issued during the suspension of Campaign H291 (estimated re-issue July 2020), addressing the **Coolant Pump** issue and related DTCs P2B61-73 / P26CB-72.                                                                                         |                  |
| **Technical Bulletin (TSB)**      | **JLRTB02030NAS1**         | Addresses a loud noise from the engine compartment on 2019-2020 F-TYPE (VIN K60736-K68311) and other Ingenium 2.0L models, requiring replacement of the variable coolant pump.                                                                             |                  |
| **Technical Topic**               | **Engine Speed Stability** | Addresses customer complaints of stalling or flashing 'D' when slowing to a stop in 19MY onwards vehicles equipped with AJ20P engines. Status: Revised PCM software (released March 31, 2021, or later) and updated work instructions will be published.   |                  |
