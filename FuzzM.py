import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Input variables
temperature = ctrl.Antecedent(np.arange(0, 101, 1), 'temperature')
humidity = ctrl.Antecedent(np.arange(0, 101, 1), 'humidity')

# Output variable
forecast = ctrl.Consequent(np.arange(0, 101, 1), 'forecast')

# Membership functions
temperature['low'] = fuzz.trimf(temperature.universe, [0, 0, 50])
temperature['medium'] = fuzz.trimf(temperature.universe, [20, 50, 80])
temperature['high'] = fuzz.trimf(temperature.universe, [50, 100, 100])

humidity['low'] = fuzz.trimf(humidity.universe, [0, 0, 50])
humidity['medium'] = fuzz.trimf(humidity.universe, [20, 50, 80])
humidity['high'] = fuzz.trimf(humidity.universe, [50, 100, 100])

forecast['low'] = fuzz.trimf(forecast.universe, [0, 0, 50])
forecast['medium'] = fuzz.trimf(forecast.universe, [20, 50, 80])
forecast['high'] = fuzz.trimf(forecast.universe, [50, 100, 100])

# Rules
rule1 = ctrl.Rule(temperature['low'] & humidity['low'], forecast['low'])
rule2 = ctrl.Rule(temperature['medium'] & humidity['medium'], forecast['medium'])
rule3 = ctrl.Rule(temperature['high'] & humidity['high'], forecast['high'])

# Control system
forecast_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
forecasting = ctrl.ControlSystemSimulation(forecast_ctrl)

# Set inputs
forecasting.input['temperature'] = 75
forecasting.input['humidity'] = 60

# Compute
forecasting.compute()

# Get output
print("Forecast:", forecasting.output['forecast'])
