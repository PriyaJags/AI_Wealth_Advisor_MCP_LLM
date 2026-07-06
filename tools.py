from data import clients

def get_client_profile(client_name):
    return clients.get(client_name.lower(), "Client not found")


def get_portfolio(client_name):
    client = clients.get(client_name.lower())

    if client:
        return {
            "portfolio_value": client["portfolio_value"],
            "holdings": client["holdings"]
        }

    return "Client not found"


def get_risk_assessment(client_name):

    client = clients.get(client_name.lower())

    if client:

        return {
            "risk_profile": client["risk"],
            "advisor_note":
                "Portfolio currently aligns with client's stated risk tolerance."
        }

    return "Client not found"