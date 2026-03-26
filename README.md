Mahindra Logistics: Last-Mile Delivery Optimization in Tier 2/3 Cities

Project Overview
This project analyzes supply chain inefficiencies within Mahindra Logistics operations, specifically focusing on the high costs and delivery delays associated with Tier 2 and Tier 3 cities. By leveraging data-driven insights, this study proposes a transition toward a Hub-and-Spoke model and Micro-Warehousing to improve delivery speed and reduce operational overhead.

Tech Stack
Language: Python 3.x
Libraries: Pandas (Data Wrangling), Matplotlib and Seaborn (Data Visualization), NumPy (Numerical Analysis)
Domain: Logistics and Supply Chain Analytics

Key Insights from Data Analysis
Based on the analysis of mahindra_logistics_dataset.csv, the following bottlenecks were identified:

The Regional Efficiency Gap
The Problem Regions: The East and South regions are the least efficient.
Delivery Time: Average delivery time in the East is 5.67 days, significantly higher than the West (5.25 days).
Cost Inefficiency: The cost-to-volume ratio in the East (6.42) and South (6.68) is nearly double that of the North and West regions (approximately 3.87).

Sector-Specific Bottlenecks
FMCG (East): Shows the longest delivery cycles (6.09 days), indicating a need for better localized distribution.
Automotive (North): High shipment volumes but inefficient routing leads to a 6.05-day delivery average.

Proposed Strategic Solutions

A. Hub-and-Spoke Model (Focus: East Region)
By consolidating shipments into a central regional hub (for example, Kolkata) before distributing to Tier 2/3 spokes, we can eliminate redundant long-haul trips.
Projected Impact: 15-20 percent reduction in transportation costs.

B. Micro-Warehousing (Focus: South E-commerce)
Data shows South E-commerce has high delivery times but lower individual shipment volumes. Deploying small-scale warehouses in urban Tier 3 centers will enable:
Reduced Last-Mile Distance: Moving inventory closer to the customer.
Speed: Shift from a 5.79-day average to Same-Day or Next-Day delivery.

C. Route and Mode Optimization
The analysis shows a heavy reliance on Rail for long-distance, which contributes to the 7 plus day delivery times in certain sectors.
Recommendation: Transitioning Last-Mile legs from Rail to optimized Road routes to normalize cost-per-volume across all regions.
