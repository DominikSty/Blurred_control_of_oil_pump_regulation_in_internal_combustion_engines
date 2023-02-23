# Blurred control of oil pump regulation in internal combustion engines
## Project assumptions
The aim of the project was to create a fuzzy controller based on decision rules for the oil pump control device in combustion engines – high and low speed. The right adjustment of the oil flow rate to the lubrication points in the engines primarily results in fuel savings and reduced exhaust emissions. Another advantage is the lower consumption of individual lubricable elements due to the ideal oil dosage, which results in longer trouble-free operation of the engine. The level with which the fuel pump should pump oil depends on several main factors, they are:
- Oil and engine temperature,
- Engine speed,
- Engine load condition.

Thanks to these three rules, the controller with the right calibration is able to select the right oil throughput to achieve the perfect dosage. On the market there are motors with built-in all the necessary sensors. But in the absence, it is possible to add individual elements.
The most important thing that can contribute to the desynchronization of the used fuzzy controller is the division of engines into low-speed and high-speed ones, therefore, during the implementation this dependency has been taken into account.

## Input
Input data, otherwise variable, is data from sensors located in the engine.
- oil_temperature – information about the oil temperature in its main tank, the sensor returns the temperature specified in degrees Celsius, its operating range is from -40 to 180 degrees.
- engine_temperature – information very similar to the oil temperature, except that the sensor is located at the most sensitive place near the oil-lubricated elements. Its operating range is the same, i. e. from -40 to 180 degrees Celsius.
- engine_speed – this is the information returned by the main computer of the engine displaying on the clocks its speed given in revolutions per minute. The range of such a sensor is from 0 to 9000 revolutions.
- engine_load_state – this is the information derived from the characteristics of throttled power. It consists of two rules: determining the throttle opening angle and the fuel dose calculated by the host computer. The range is given as a percentage and ranges from 0 to 100.

## Output
The premise for the project is the appropriate adjustment of the pressure of the pressed oil to the lubricable components by means of an oil pump in the engine compartment. The result of the controller should be a percentage of the operating range of the respective pump. The standard pressure in such a system is in the range of 0.8 – 4 bar. The fuzzy controller should select the appropriate dose by analyzing the individual input data taken from the sensors. Below is the implementation code of the output variable with its membership functions. The result is given as a percentage of engine operation, as the bar quantity is set at the beginning and depends on the type of pump used.

## Conclusion
The created project presents an example of the application of fuzzy systems in a real situation. This is an approximate simulation based on real sensors depicting the operation of an internal combustion engine oil pump to determine the correct dosage of lubricable specificity for the engine part. The rules system is not 100% correct, as it requires physical testing of the component and adjustment of the rules to achieve the intended results of lower exhaust emissions and less fuel burned. The project allows for an approximate understanding of the operation of fuzzy systems under theoretical conditions using real data.

## Description of technologies used
The application was created using the Python v3.7 programming language with the following libraries:
- numpy,
- skfuzzy,
- matplotlib.pyplot.
