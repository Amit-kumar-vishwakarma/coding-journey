# Day 5: Dynamic Credit Risk & Loan Eligibility Engine


def evaluate_applicant(credit_score, annual_income, debt_amount, employment_years):
    # Calculate Debt-to-Income (DTI) ratio percentage
    dti_ratio = (debt_amount / annual_income) * 100

    # Intermediate decision engine using nested & compound conditionals
    if credit_score < 300 or credit_score > 850:
        return "Invalid credit score provided."

    if credit_score >= 750:
        if dti_ratio <= 35:
            if employment_years >= 2:
                tier = "Tier 1: Approved (Prime Rate - 4.5%)"
            else:
                tier = "Tier 2: Approved with condition (Recent job change - 5.5%)"
        elif 35 < dti_ratio <= 50:
            tier = "Tier 3: Conditional Approval (High DTI - 7.0%)"
        else:
            tier = "Rejected: Excessive DTI ratio despite good credit."

    elif 600 <= credit_score < 750:
        if dti_ratio <= 30 and employment_years >= 3:
            tier = "Tier 3: Standard Approval (8.5%)"
        elif dti_ratio <= 45 and employment_years >= 5:
            tier = "Tier 4: Approved with Co-signer (10.0%)"
        else:
            tier = "Rejected: Risk profile too high for standard tier."

    else:
        tier = "Rejected: Credit score below minimum threshold (< 600)."

    return tier


# Test case run
applicant_result = evaluate_applicant(
    credit_score=710,
    annual_income=85000,
    debt_amount=24000,
    employment_years=4,
)

print(f"Risk Evaluation Status: {applicant_result}")