# NHTSA API Call Setups

> Last updated: 2025-09-13

This document consolidates the most commonly-used REST endpoints offered by the National Highway Traffic Safety Administration (NHTSA) public APIs, along with required parameters and an example request for each.

---

## 1. Safety Ratings (NCAP)

Base path: `https://api.nhtsa.gov/SafetyRatings`

| Purpose | Verb | Path | Req. Params | Typical Usage |
|---------|------|------|-------------|---------------|
| List available model years | GET | `/` | – | Get the list of model years for which ratings exist |
| List makes for a model year | GET | `/modelyear/{year}` | `{year}` – 4-digit year | |
| List models for a make & year | GET | `/modelyear/{year}/make/{make}` | `{year}`, `{make}` | |
| List vehicle variants | GET | `/modelyear/{year}/make/{make}/model/{model}` | `{year}`, `{make}`, `{model}` | Returns Vehicle IDs |
| Get ratings for a variant | GET | `/VehicleId/{vehicleId}` | `{vehicleId}` – from previous call | |

Example – pull rollover rating for a 2013 Acura RDX variant:

```http
GET https://api.nhtsa.gov/SafetyRatings/modelyear/2013/make/Acura/model/RDX
```

(The JSON result includes a `VehicleId`; pass that to `/VehicleId/{id}`.)

---

## 2. Recalls

Base path: `https://api.nhtsa.gov`

| Purpose | Verb | Path | Query / Path Params | Notes |
|---------|------|------|--------------------|-------|
| Recalls by vehicle | GET | `/recalls/recallsByVehicle` | `make`, `model`, `modelYear` | Query string format |
| Model years (recalls) | GET | `/products/vehicle/modelYears` | `issueType=r` | `r` indicates recall |
| Makes for year | GET | `/products/vehicle/makes` | `modelYear`, `issueType=r` | |
| Models for make & year | GET | `/products/vehicle/models` | `modelYear`, `make`, `issueType=r` | |
| Recalls by campaign # | GET | `/recalls/campaignNumber` | `campaignNumber` | |

Example – 2012 Acura RDX recalls:

```http
GET https://api.nhtsa.gov/recalls/recallsByVehicle?make=acura&model=rdx&modelYear=2012
```

---

## 3. Complaints

Base path: `https://api.nhtsa.gov`

Replace the recall endpoints’ `issueType=r` with `issueType=c`, and paths starting with `/recalls` become `/complaints`.

| Purpose | Verb | Path | Params |
|---------|------|------|--------|
| Complaints by vehicle | GET | `/complaints/complaintsByVehicle` | `make`, `model`, `modelYear` |
| Model years (complaints) | GET | `/products/vehicle/modelYears` | `issueType=c` |
| Makes for year | GET | `/products/vehicle/makes` | `modelYear`, `issueType=c` |
| Models for make & year | GET | `/products/vehicle/models` | `modelYear`, `make`, `issueType=c` |
| Complaints by ODI number | GET | `/complaints/odinumber` | `odinumber` |

Example – all complaints for ODI `11184030`:

```http
GET https://api.nhtsa.gov/complaints/odinumber?odinumber=11184030
```

---

## 4. Car-Seat Inspection Stations (CSSIStation)

Base path: `https://api.nhtsa.gov/CSSIStation`

| Purpose | Verb | Path | Notes |
|---------|------|------|-------|
| By ZIP | GET | `/zip/{zip}` | |
| By State | GET | `/state/{stateAbbr}` | US-state 2-letter code |
| By Lat/Lon radius | GET | ``?lat={lat}&long={lon}&miles={mi}`` | Miles radius search |

Optional filters can be appended:

* `/lang/spanish` – only Spanish-speaking stations
* `/cpsweek` – stations participating in Child Passenger Safety Week

Example – Spanish-speaking stations within ZIP 63640:

```http
GET https://api.nhtsa.gov/CSSIStation/zip/63640/lang/spanish
```

---

## 5. Common Tips

1. All endpoints return JSON by default. No auth or API key is required.
2. Query parameters are **case-sensitive**.
3. Treat spaces within path params (e.g., model names) as URL-encoded (`RAV4` not `RAV 4`).
4. To page or limit results, use standard tools (e.g., `jq`) client-side; the APIs do not expose pagination parameters.

---

### Quick Test with `curl`

```bash
curl -s \
  "https://api.nhtsa.gov/recalls/recallsByVehicle?make=acura&model=rdx&modelYear=2012" \
  | jq '.results[0] | {Campaign: .NHTSACampaignNumber, Component, Summary}'
```

---

## End of document
