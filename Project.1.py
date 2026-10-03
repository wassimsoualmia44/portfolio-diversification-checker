portfolio = {}
def add_holding(name,sector,value):
        portfolio[name]={"name":name,"sector": sector, "value": value}

def total_value():
        total = 0
        for holding  in portfolio.values():
            total += holding["value"]
        return total


def sector_weight():
    weight={}
    sectors= {}
    for x in portfolio.values():
        sectors[x['sector']] = sectors.get(x['sector'],0) + x["value"]
    total = total_value()

    for sector,value in sectors.items():
        weight[sector] = (value / total)
    return weight


def diversification_score(weight): 
    running_total = 0
    for y in weight.values():
        running_total += y**2

    score =round((1-running_total)*100)

    return score


while True : 
    name =input("Enter the company name of your holdings ")
    sector=(input(f"Enter the company sector of {name} your holdings ")).lower()
    value =float(input(f"Enter the company  value of {name} your holdings "))
    add_holding(name,sector,value)
    finish = input("type Done when you finish a set")
    if finish.lower() == 'done':
        break

if not portfolio:
    print("No holdings entered.")
else:
    print("--------Report is here --------------- ")
    print(f"The total value is £{total_value():,.2f}")
    weights = sector_weight()
    print("----Sector Breakdown----")
    for sector, weight in weights.items():
        print(f"The sector {sector} has a weight of {weight:.1%}")
        if weight > 0.4:
            print(f"{sector} is over-concentrated")

    biggest = max(portfolio, key=lambda name: portfolio[name]["value"])
    biggest_weight = portfolio[biggest]["value"] / total_value()
    print(f"\nLargest holding: {biggest} ({biggest_weight:.1%})")

    score = diversification_score(weights)
    print(f"Diversification score: {score}/100")

    if score < 40:
        print("Verdict: Poorly diversified.")
    elif score < 70:
        print("Verdict: Moderately diversified.")
    else:
        print("Verdict: Well diversified.")