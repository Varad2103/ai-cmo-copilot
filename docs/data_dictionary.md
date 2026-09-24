# AI CMO Copilot — Data Dictionary

## Core Design Principles

All tables must have:

- A clearly defined grain
- A primary key
- Foreign keys where applicable
- Consistent timestamps
- Consistent customer/campaign identifiers
- Realistic business relationships

---

## campaigns

### Grain
One row per marketing campaign.

### Primary Key
campaign_id

### Important Columns

campaign_id
campaign_name
campaign_type
channel
sub_channel
objective
funnel_stage
target_segment
target_industry
target_region
start_date
end_date
budget
currency
status
landing_page
utm_campaign
utm_source
utm_medium

---

## ad_performance

### Grain
One row per date × campaign × platform × geography × device.

### Primary Key
ad_performance_id

### Foreign Keys
campaign_id

### Important Columns

date
platform
campaign_id
ad_group_id
ad_id
country
region
city
device
audience_segment
impressions
reach
clicks
engagements
spend
conversions
conversion_value
landing_page_views
leads
mqls

---

## website_sessions

### Grain
One row per website session.

### Primary Key
session_id

### Important Columns

session_id
user_id
session_start
session_end
source
medium
campaign
channel
landing_page
exit_page
device_category
country
region
city
new_user
pages_viewed
session_duration_seconds
engaged_session
bounce_flag
form_start
form_submit
conversion
conversion_type
conversion_value

---

## leads

### Grain
One row per lead.

### Primary Key
lead_id

### Important Columns

lead_id
created_at
company_id
company_name
job_title
seniority
industry
company_size
country
state
city
lead_source
lead_source_detail
first_touch_channel
first_touch_campaign
last_touch_channel
last_touch_campaign
lifecycle_stage
lead_score
intent_score
mql_date
sql_date
sales_owner
status

---

## opportunities

### Grain
One row per sales opportunity.

### Primary Key
opportunity_id

### Foreign Keys
lead_id
campaign_id

### Important Columns

opportunity_id
lead_id
account_id
created_at
close_date
stage
opportunity_type
product
amount
currency
probability
forecast_category
lead_source
campaign_id
sales_owner
sales_region
competitor
closed_won
closed_lost
loss_reason

---

## customers

### Grain
One row per customer account.

### Primary Key
customer_id

### Important Columns

customer_id
account_id
company_name
industry
company_size
country
region
acquisition_date
acquisition_channel
acquisition_campaign
plan
contract_type
annual_contract_value
monthly_recurring_revenue
customer_status
customer_segment

---

## orders_revenue

### Grain
One row per revenue transaction.

### Primary Key
order_id

### Foreign Keys
customer_id
opportunity_id

### Important Columns

order_id
customer_id
opportunity_id
order_date
product_id
product_name
quantity
gross_revenue
discount
net_revenue
currency
subscription_term
new_or_renewal
refund_amount
recognized_revenue

---

## campaign_members

### Grain
One row per lead × campaign relationship.

### Primary Key
campaign_member_id

### Foreign Keys
campaign_id
lead_id

### Important Columns

campaign_member_id
campaign_id
lead_id
member_status
first_responded_at
last_responded_at
converted
conversion_date
influence_weight