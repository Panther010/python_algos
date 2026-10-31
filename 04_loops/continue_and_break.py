"""
Scenario: 
You are processing a batch of financial transaction amounts. 
Negative amounts or zeros are corrupted data and should be skipped (continue). 
However, if any single transaction exceeds a critical fraud limit (e.g., $1,000,000), 
the security protocol requires you to instantly halt the entire batch processing (break) and 
flag a breach.
"""

# Test data
transactions = [150.0, 500.0, 0.0, -20.0, 2500.0, 1_500_000.0, 400.0]

def process_transections(amounts: list[float]) -> float:
    result = 0.0

    for amount in amounts:
        print(result)
        if amount > 1000000:
            print("There is a breach. Alert")
            break
        elif amount > 0:
            result += amount
        elif amount <= 0:
            continue
    
    return result

print(process_transections(transactions))