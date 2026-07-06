print("🔥 LOADED AGENT FILE:", __file__)
import json
from executor import Executor
from advisor import generate_recommendations


EXPECTED_FIELDS = {
    "name",
    "age",
    "risk",
    "portfolio_value",
    "holdings"
}


def run_agent(client_name):   # ✅ ONLY ONE ARGUMENT

    executor = Executor()
    raw_data = executor.run_tool("client_profile", client_name)

    print("\n[Raw Executor Output]", raw_data)

    # Convert JSON string → dict
    if isinstance(raw_data, str):
        try:
            raw_data = json.loads(raw_data)
        except:
            raw_data = {}

    missing_fields = list(EXPECTED_FIELDS - set(raw_data.keys()))

    return generate_recommendations(raw_data, missing_fields)
   # return generate_recommendations(raw_data)