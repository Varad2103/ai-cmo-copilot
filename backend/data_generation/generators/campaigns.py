from datetime import datetime, timedelta
from pathlib import Path

import numpy as np
import pandas as pd
from faker import Faker


fake = Faker()

RANDOM_SEED = 42
np.random.seed(RANDOM_SEED)

CHANNELS = {
    "Paid Search": ["Google Ads", "Bing Ads"],
    "Paid Social": ["Meta", "LinkedIn"],
    "Organic": ["SEO"],
    "Email": ["Lifecycle Email", "Newsletter"],
    "Referral": ["Partner", "Customer Referral"],
    "Direct": ["Direct"],
}

OBJECTIVES = [
    "Lead Generation",
    "Brand Awareness",
    "Product Consideration",
    "Customer Acquisition",
    "Retargeting",
]

FUNNEL_STAGES = [
    "Awareness",
    "Consideration",
    "Conversion",
]

SEGMENTS = [
    "SMB",
    "Mid-Market",
    "Enterprise",
]

INDUSTRIES = [
    "Technology",
    "Financial Services",
    "Healthcare",
    "Retail",
    "Manufacturing",
    "Education",
    "Professional Services",
]

REGIONS = [
    "North America",
    "Europe",
    "Australia",
]

STATUSES = [
    "Active",
    "Completed",
    "Paused",
]


def generate_campaigns(n_campaigns: int = 100) -> pd.DataFrame:

    rows = []

    start_date = datetime(2025, 1, 1)

    for i in range(1, n_campaigns + 1):

        channel = np.random.choice(list(CHANNELS.keys()))
        sub_channel = np.random.choice(CHANNELS[channel])

        campaign_start = start_date + timedelta(
            days=int(np.random.randint(0, 500))
        )

        duration = int(np.random.randint(30, 120))

        campaign_end = campaign_start + timedelta(days=duration)

        segment = np.random.choice(SEGMENTS)

        rows.append(
            {
                "campaign_id": f"CMP_{i:05d}",
                "campaign_name": (
                    f"{segment} {sub_channel} "
                    f"{campaign_start.strftime('%Y-%m')} Campaign"
                ),
                "campaign_type": channel,
                "channel": channel,
                "sub_channel": sub_channel,
                "objective": np.random.choice(OBJECTIVES),
                "funnel_stage": np.random.choice(FUNNEL_STAGES),
                "target_segment": segment,
                "target_industry": np.random.choice(INDUSTRIES),
                "target_region": np.random.choice(REGIONS),
                "start_date": campaign_start.date(),
                "end_date": campaign_end.date(),
                "budget": round(
                    float(np.random.lognormal(mean=9, sigma=1)),
                    2,
                ),
                "currency": "USD",
                "status": np.random.choice(STATUSES),
                "landing_page": (
                    f"/solutions/{segment.lower().replace('-', '_')}"
                ),
                "utm_campaign": f"cmp_{i:05d}",
                "utm_source": sub_channel.lower().replace(" ", "_"),
                "utm_medium": (
                    "cpc"
                    if channel == "Paid Search"
                    else "paid_social"
                    if channel == "Paid Social"
                    else "organic"
                ),
            }
        )

    return pd.DataFrame(rows)


if __name__ == "__main__":

    output_dir = Path(__file__).resolve().parents[3] / "data" / "sample"

    output_dir.mkdir(parents=True, exist_ok=True)

    df = generate_campaigns(100)

    output_path = output_dir / "campaigns.csv"

    df.to_csv(output_path, index=False)

    print(f"Generated {len(df)} campaigns")
    print(f"Saved to: {output_path}")