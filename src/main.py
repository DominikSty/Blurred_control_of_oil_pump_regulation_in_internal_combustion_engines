import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

high_speed_motor = False
scope_of_operation_pumps = [0.8, 4]

# Input variables
oil_temperature = ctrl.Antecedent(np.arange(-40, 180), 'oil_temperature')  # Oil temperature (*C)
engine_temperature = ctrl.Antecedent(np.arange(-40, 180), 'engine_temperature')  # Engine temperature (*C)
if (high_speed_motor):
    engine_speed = ctrl.Antecedent(np.arange(0, 9000), 'engine_speed')  # Engine speed (rmp)
else:
    engine_speed = ctrl.Antecedent(np.arange(0, 7000), 'engine_speed')  # Engine speed (rmp)
engine_load_state = ctrl.Antecedent(np.arange(0, 100), 'engine_load_state')  # Engine load state (%)

# Input Variable Affiliation Functions
# Oil temperature
oil_temperature['low']   = fuzz.trapmf(oil_temperature.universe, [-40, -40, -10, 10])
oil_temperature['average'] = fuzz.trimf(oil_temperature.universe,  [0, 45, 90])
oil_temperature['high']  = fuzz.trapmf(oil_temperature.universe, [75, 110, 180, 180])
# oil_temperature.view()
# Engine temperature
engine_temperature['low']   = fuzz.trapmf(engine_temperature.universe, [-40, -40, 0, 25])
engine_temperature['average'] = fuzz.trimf(engine_temperature.universe,  [-10, 55, 100])
engine_temperature['high']  = fuzz.trapmf(engine_temperature.universe, [65, 90, 180, 180])
# engine_temperature.view()
# Engine speed
if (high_speed_motor):
    engine_speed['sterile']  = fuzz.trapmf(engine_speed.universe, [0, 0, 650, 850])
    engine_speed['low']   = fuzz.trimf(engine_speed.universe,  [500, 2000, 3000])
    engine_speed['average'] = fuzz.trimf(engine_speed.universe,  [2000, 3500, 5000])
    engine_speed['high']  = fuzz.trapmf(engine_speed.universe, [4000, 5500, 9000, 9000])
    # engine_speed.view()
else:
    engine_speed['sterile']  = fuzz.trapmf(engine_speed.universe, [0, 0, 650, 850])
    engine_speed['low']   = fuzz.trimf(engine_speed.universe,  [500, 1200, 2500])
    engine_speed['average'] = fuzz.trimf(engine_speed.universe,  [2000, 3000, 4000])
    engine_speed['high']  = fuzz.trapmf(engine_speed.universe, [3000, 5000, 7000, 7000])
    # engine_speed.view()
# Engine Load Condition
engine_load_state['none']    = fuzz.trapmf(engine_load_state.universe, [0, 0, 5, 10])
engine_load_state['low']   = fuzz.trimf(engine_load_state.universe,  [5, 15, 25])
engine_load_state['average'] = fuzz.trimf(engine_load_state.universe,  [20, 40, 60])
engine_load_state['high']  = fuzz.trapmf(engine_load_state.universe, [50, 75, 100, 100])
# engine_load_state.view()

# Output Variable
pump_pressure = ctrl.Consequent(np.arange(0, 100), 'pump_pressure')  # Oil pump pressure

# Output Variable Affiliation Functions
pump_pressure['small'] = fuzz.trapmf(pump_pressure.universe, [0, 0, 20, 40])
pump_pressure['medium'] = fuzz.trimf(pump_pressure.universe, [20, 50, 80])
pump_pressure['large'] = fuzz.trapmf(pump_pressure.universe, [70, 90, 100, 100])
# pump_pressure.view()

# Fuzzy rules
rule_1 = ctrl.Rule(oil_temperature['low'] & engine_temperature['low'] & engine_speed['sterile'] & engine_load_state['none'],    pump_pressure['small'])
rule_2 = ctrl.Rule(oil_temperature['low'] & engine_temperature['low'] & engine_speed['sterile'] & engine_load_state['low'],   pump_pressure['small'])
rule_3 = ctrl.Rule(oil_temperature['low'] & engine_temperature['low'] & engine_speed['sterile'] & engine_load_state['average'], pump_pressure['small'])
rule_4 = ctrl.Rule(oil_temperature['low'] & engine_temperature['low'] & engine_speed['sterile'] & engine_load_state['high'],  pump_pressure['medium'])

rule_5 = ctrl.Rule(oil_temperature['low'] & engine_temperature['low'] & engine_speed['low'] & engine_load_state['none'],    pump_pressure['small'])
rule_6 = ctrl.Rule(oil_temperature['low'] & engine_temperature['low'] & engine_speed['low'] & engine_load_state['low'],   pump_pressure['small'])
rule_7 = ctrl.Rule(oil_temperature['low'] & engine_temperature['low'] & engine_speed['low'] & engine_load_state['average'], pump_pressure['medium'])
rule_8 = ctrl.Rule(oil_temperature['low'] & engine_temperature['low'] & engine_speed['low'] & engine_load_state['high'],  pump_pressure['medium'])

rule_9 = ctrl.Rule(oil_temperature['low'] & engine_temperature['low'] & engine_speed['average'] & engine_load_state['none'],     pump_pressure['small'])
rule_10 = ctrl.Rule(oil_temperature['low'] & engine_temperature['low'] & engine_speed['average'] & engine_load_state['low'],   pump_pressure['small'])
rule_11 = ctrl.Rule(oil_temperature['low'] & engine_temperature['low'] & engine_speed['average'] & engine_load_state['average'], pump_pressure['small'])
rule_12 = ctrl.Rule(oil_temperature['low'] & engine_temperature['low'] & engine_speed['average'] & engine_load_state['high'],  pump_pressure['medium'])

rule_13 = ctrl.Rule(oil_temperature['low'] & engine_temperature['low'] & engine_speed['high'] & engine_load_state['none'],    pump_pressure['small'])
rule_14 = ctrl.Rule(oil_temperature['low'] & engine_temperature['low'] & engine_speed['high'] & engine_load_state['low'],   pump_pressure['small'])
rule_15 = ctrl.Rule(oil_temperature['low'] & engine_temperature['low'] & engine_speed['high'] & engine_load_state['average'], pump_pressure['medium'])
rule_16 = ctrl.Rule(oil_temperature['low'] & engine_temperature['low'] & engine_speed['high'] & engine_load_state['high'],  pump_pressure['medium'])


rule_17 = ctrl.Rule(oil_temperature['low'] & engine_temperature['average'] & engine_speed['sterile'] & engine_load_state['none'],    pump_pressure['small'])
rule_18 = ctrl.Rule(oil_temperature['low'] & engine_temperature['average'] & engine_speed['sterile'] & engine_load_state['low'],   pump_pressure['medium'])
rule_19 = ctrl.Rule(oil_temperature['low'] & engine_temperature['average'] & engine_speed['sterile'] & engine_load_state['average'], pump_pressure['medium'])
rule_20 = ctrl.Rule(oil_temperature['low'] & engine_temperature['average'] & engine_speed['sterile'] & engine_load_state['high'],  pump_pressure['medium'])

rule_21 = ctrl.Rule(oil_temperature['low'] & engine_temperature['average'] & engine_speed['low'] & engine_load_state['none'],    pump_pressure['small'])
rule_22 = ctrl.Rule(oil_temperature['low'] & engine_temperature['average'] & engine_speed['low'] & engine_load_state['low'],   pump_pressure['medium'])
rule_23 = ctrl.Rule(oil_temperature['low'] & engine_temperature['average'] & engine_speed['low'] & engine_load_state['average'], pump_pressure['medium'])
rule_24 = ctrl.Rule(oil_temperature['low'] & engine_temperature['average'] & engine_speed['low'] & engine_load_state['high'],  pump_pressure['medium'])

rule_25 = ctrl.Rule(oil_temperature['low'] & engine_temperature['average'] & engine_speed['average'] & engine_load_state['none'],    pump_pressure['small'])
rule_26 = ctrl.Rule(oil_temperature['low'] & engine_temperature['average'] & engine_speed['average'] & engine_load_state['low'],   pump_pressure['small'])
rule_27 = ctrl.Rule(oil_temperature['low'] & engine_temperature['average'] & engine_speed['average'] & engine_load_state['average'], pump_pressure['medium'])
rule_28 = ctrl.Rule(oil_temperature['low'] & engine_temperature['average'] & engine_speed['average'] & engine_load_state['high'],  pump_pressure['medium'])

rule_29 = ctrl.Rule(oil_temperature['low'] & engine_temperature['average'] & engine_speed['high'] & engine_load_state['none'],    pump_pressure['small'])
rule_30 = ctrl.Rule(oil_temperature['low'] & engine_temperature['average'] & engine_speed['high'] & engine_load_state['low'],   pump_pressure['small'])
rule_31 = ctrl.Rule(oil_temperature['low'] & engine_temperature['average'] & engine_speed['high'] & engine_load_state['average'], pump_pressure['medium'])
rule_32 = ctrl.Rule(oil_temperature['low'] & engine_temperature['average'] & engine_speed['high'] & engine_load_state['high'],  pump_pressure['medium'])


rule_33 = ctrl.Rule(oil_temperature['low'] & engine_temperature['high'] & engine_speed['sterile'] & engine_load_state['none'],    pump_pressure['small'])
rule_34 = ctrl.Rule(oil_temperature['low'] & engine_temperature['high'] & engine_speed['sterile'] & engine_load_state['low'],   pump_pressure['medium'])
rule_35 = ctrl.Rule(oil_temperature['low'] & engine_temperature['high'] & engine_speed['sterile'] & engine_load_state['average'], pump_pressure['medium'])
rule_36 = ctrl.Rule(oil_temperature['low'] & engine_temperature['high'] & engine_speed['sterile'] & engine_load_state['high'],  pump_pressure['medium'])

rule_37 = ctrl.Rule(oil_temperature['low'] & engine_temperature['high'] & engine_speed['low'] & engine_load_state['none'],    pump_pressure['small'])
rule_38 = ctrl.Rule(oil_temperature['low'] & engine_temperature['high'] & engine_speed['low'] & engine_load_state['low'],   pump_pressure['medium'])
rule_39 = ctrl.Rule(oil_temperature['low'] & engine_temperature['high'] & engine_speed['low'] & engine_load_state['average'], pump_pressure['medium'])
rule_40 = ctrl.Rule(oil_temperature['low'] & engine_temperature['high'] & engine_speed['low'] & engine_load_state['high'],  pump_pressure['medium'])

rule_41 = ctrl.Rule(oil_temperature['low'] & engine_temperature['high'] & engine_speed['average'] & engine_load_state['none'],    pump_pressure['small'])
rule_42 = ctrl.Rule(oil_temperature['low'] & engine_temperature['high'] & engine_speed['average'] & engine_load_state['low'],   pump_pressure['medium'])
rule_43 = ctrl.Rule(oil_temperature['low'] & engine_temperature['high'] & engine_speed['average'] & engine_load_state['average'], pump_pressure['medium'])
rule_44 = ctrl.Rule(oil_temperature['low'] & engine_temperature['high'] & engine_speed['average'] & engine_load_state['high'],  pump_pressure['medium'])

rule_45 = ctrl.Rule(oil_temperature['low'] & engine_temperature['high'] & engine_speed['high'] & engine_load_state['none'],    pump_pressure['small'])
rule_46 = ctrl.Rule(oil_temperature['low'] & engine_temperature['high'] & engine_speed['high'] & engine_load_state['low'],   pump_pressure['medium'])
rule_47 = ctrl.Rule(oil_temperature['low'] & engine_temperature['high'] & engine_speed['high'] & engine_load_state['average'], pump_pressure['medium'])
rule_48 = ctrl.Rule(oil_temperature['low'] & engine_temperature['high'] & engine_speed['high'] & engine_load_state['high'],  pump_pressure['medium'])



rule_49 = ctrl.Rule(oil_temperature['average'] & engine_temperature['low'] & engine_speed['sterile'] & engine_load_state['none'],    pump_pressure['small'])
rule_50 = ctrl.Rule(oil_temperature['average'] & engine_temperature['low'] & engine_speed['sterile'] & engine_load_state['low'],   pump_pressure['medium'])
rule_51 = ctrl.Rule(oil_temperature['average'] & engine_temperature['low'] & engine_speed['sterile'] & engine_load_state['average'], pump_pressure['medium'])
rule_52 = ctrl.Rule(oil_temperature['average'] & engine_temperature['low'] & engine_speed['sterile'] & engine_load_state['high'],  pump_pressure['medium'])

rule_53 = ctrl.Rule(oil_temperature['average'] & engine_temperature['low'] & engine_speed['low'] & engine_load_state['none'],    pump_pressure['medium'])
rule_54 = ctrl.Rule(oil_temperature['average'] & engine_temperature['low'] & engine_speed['low'] & engine_load_state['low'],   pump_pressure['medium'])
rule_55 = ctrl.Rule(oil_temperature['average'] & engine_temperature['low'] & engine_speed['low'] & engine_load_state['average'], pump_pressure['medium'])
rule_56 = ctrl.Rule(oil_temperature['average'] & engine_temperature['low'] & engine_speed['low'] & engine_load_state['high'],  pump_pressure['medium'])

rule_57 = ctrl.Rule(oil_temperature['average'] & engine_temperature['low'] & engine_speed['average'] & engine_load_state['none'],    pump_pressure['small'])
rule_58 = ctrl.Rule(oil_temperature['average'] & engine_temperature['low'] & engine_speed['average'] & engine_load_state['low'],   pump_pressure['medium'])
rule_59 = ctrl.Rule(oil_temperature['average'] & engine_temperature['low'] & engine_speed['average'] & engine_load_state['average'], pump_pressure['medium'])
rule_60 = ctrl.Rule(oil_temperature['average'] & engine_temperature['low'] & engine_speed['average'] & engine_load_state['high'],  pump_pressure['medium'])

rule_61 = ctrl.Rule(oil_temperature['average'] & engine_temperature['low'] & engine_speed['high'] & engine_load_state['none'],    pump_pressure['medium'])
rule_62 = ctrl.Rule(oil_temperature['average'] & engine_temperature['low'] & engine_speed['high'] & engine_load_state['low'],   pump_pressure['medium'])
rule_63 = ctrl.Rule(oil_temperature['average'] & engine_temperature['low'] & engine_speed['high'] & engine_load_state['average'], pump_pressure['medium'])
rule_64 = ctrl.Rule(oil_temperature['average'] & engine_temperature['low'] & engine_speed['high'] & engine_load_state['high'],  pump_pressure['large'])


rule_65 = ctrl.Rule(oil_temperature['average'] & engine_temperature['average'] & engine_speed['sterile'] & engine_load_state['none'],    pump_pressure['medium'])
rule_66 = ctrl.Rule(oil_temperature['average'] & engine_temperature['average'] & engine_speed['sterile'] & engine_load_state['low'],   pump_pressure['medium'])
rule_67 = ctrl.Rule(oil_temperature['average'] & engine_temperature['average'] & engine_speed['sterile'] & engine_load_state['average'], pump_pressure['medium'])
rule_68 = ctrl.Rule(oil_temperature['average'] & engine_temperature['average'] & engine_speed['sterile'] & engine_load_state['high'],  pump_pressure['medium'])

rule_69 = ctrl.Rule(oil_temperature['average'] & engine_temperature['average'] & engine_speed['low'] & engine_load_state['none'],    pump_pressure['small'])
rule_70 = ctrl.Rule(oil_temperature['average'] & engine_temperature['average'] & engine_speed['low'] & engine_load_state['low'],   pump_pressure['medium'])
rule_71 = ctrl.Rule(oil_temperature['average'] & engine_temperature['average'] & engine_speed['low'] & engine_load_state['average'], pump_pressure['medium'])
rule_72 = ctrl.Rule(oil_temperature['average'] & engine_temperature['average'] & engine_speed['low'] & engine_load_state['high'],  pump_pressure['medium'])

rule_73 = ctrl.Rule(oil_temperature['average'] & engine_temperature['average'] & engine_speed['average'] & engine_load_state['none'],    pump_pressure['medium'])
rule_74 = ctrl.Rule(oil_temperature['average'] & engine_temperature['average'] & engine_speed['average'] & engine_load_state['low'],   pump_pressure['medium'])
rule_75 = ctrl.Rule(oil_temperature['average'] & engine_temperature['average'] & engine_speed['average'] & engine_load_state['average'], pump_pressure['medium'])
rule_76 = ctrl.Rule(oil_temperature['average'] & engine_temperature['average'] & engine_speed['average'] & engine_load_state['high'],  pump_pressure['medium'])

rule_77 = ctrl.Rule(oil_temperature['average'] & engine_temperature['average'] & engine_speed['high'] & engine_load_state['none'],    pump_pressure['small'])
rule_78 = ctrl.Rule(oil_temperature['average'] & engine_temperature['average'] & engine_speed['high'] & engine_load_state['low'],   pump_pressure['medium'])
rule_79 = ctrl.Rule(oil_temperature['average'] & engine_temperature['average'] & engine_speed['high'] & engine_load_state['average'], pump_pressure['medium'])
rule_80 = ctrl.Rule(oil_temperature['average'] & engine_temperature['average'] & engine_speed['high'] & engine_load_state['high'],  pump_pressure['large'])


rule_81 = ctrl.Rule(oil_temperature['average'] & engine_temperature['high'] & engine_speed['sterile'] & engine_load_state['none'],    pump_pressure['small'])
rule_82 = ctrl.Rule(oil_temperature['average'] & engine_temperature['high'] & engine_speed['sterile'] & engine_load_state['low'],   pump_pressure['medium'])
rule_83 = ctrl.Rule(oil_temperature['average'] & engine_temperature['high'] & engine_speed['sterile'] & engine_load_state['average'], pump_pressure['medium'])
rule_84 = ctrl.Rule(oil_temperature['average'] & engine_temperature['high'] & engine_speed['sterile'] & engine_load_state['high'],  pump_pressure['medium'])

rule_85 = ctrl.Rule(oil_temperature['average'] & engine_temperature['high'] & engine_speed['low'] & engine_load_state['none'],    pump_pressure['medium'])
rule_86 = ctrl.Rule(oil_temperature['average'] & engine_temperature['high'] & engine_speed['low'] & engine_load_state['low'],   pump_pressure['medium'])
rule_87 = ctrl.Rule(oil_temperature['average'] & engine_temperature['high'] & engine_speed['low'] & engine_load_state['average'], pump_pressure['medium'])
rule_88 = ctrl.Rule(oil_temperature['average'] & engine_temperature['high'] & engine_speed['low'] & engine_load_state['high'],  pump_pressure['medium'])

rule_89 = ctrl.Rule(oil_temperature['average'] & engine_temperature['high'] & engine_speed['average'] & engine_load_state['none'],    pump_pressure['medium'])
rule_90 = ctrl.Rule(oil_temperature['average'] & engine_temperature['high'] & engine_speed['average'] & engine_load_state['low'],   pump_pressure['medium'])
rule_91 = ctrl.Rule(oil_temperature['average'] & engine_temperature['high'] & engine_speed['average'] & engine_load_state['average'], pump_pressure['medium'])
rule_92 = ctrl.Rule(oil_temperature['average'] & engine_temperature['high'] & engine_speed['average'] & engine_load_state['high'],  pump_pressure['medium'])

rule_93 = ctrl.Rule(oil_temperature['average'] & engine_temperature['high'] & engine_speed['high'] & engine_load_state['none'],    pump_pressure['medium'])
rule_94 = ctrl.Rule(oil_temperature['average'] & engine_temperature['high'] & engine_speed['high'] & engine_load_state['low'],   pump_pressure['medium'])
rule_95 = ctrl.Rule(oil_temperature['average'] & engine_temperature['high'] & engine_speed['high'] & engine_load_state['average'], pump_pressure['medium'])
rule_96 = ctrl.Rule(oil_temperature['average'] & engine_temperature['high'] & engine_speed['high'] & engine_load_state['high'],  pump_pressure['large'])



rule_97 = ctrl.Rule(oil_temperature['high'] & engine_temperature['low'] & engine_speed['sterile'] & engine_load_state['none'],     pump_pressure['small'])
rule_98 = ctrl.Rule(oil_temperature['high'] & engine_temperature['low'] & engine_speed['sterile'] & engine_load_state['low'],    pump_pressure['medium'])
rule_99 = ctrl.Rule(oil_temperature['high'] & engine_temperature['low'] & engine_speed['sterile'] & engine_load_state['average'],  pump_pressure['large'])
rule_100 = ctrl.Rule(oil_temperature['high'] & engine_temperature['low'] & engine_speed['sterile'] & engine_load_state['high'],  pump_pressure['large'])

rule_101 = ctrl.Rule(oil_temperature['high'] & engine_temperature['low'] & engine_speed['low'] & engine_load_state['none'],    pump_pressure['small'])
rule_102 = ctrl.Rule(oil_temperature['high'] & engine_temperature['low'] & engine_speed['low'] & engine_load_state['low'],   pump_pressure['medium'])
rule_103 = ctrl.Rule(oil_temperature['high'] & engine_temperature['low'] & engine_speed['low'] & engine_load_state['average'], pump_pressure['large'])
rule_104 = ctrl.Rule(oil_temperature['high'] & engine_temperature['low'] & engine_speed['low'] & engine_load_state['high'],  pump_pressure['large'])

rule_105 = ctrl.Rule(oil_temperature['high'] & engine_temperature['low'] & engine_speed['average'] & engine_load_state['none'],    pump_pressure['small'])
rule_106 = ctrl.Rule(oil_temperature['high'] & engine_temperature['low'] & engine_speed['average'] & engine_load_state['low'],   pump_pressure['medium'])
rule_107 = ctrl.Rule(oil_temperature['high'] & engine_temperature['low'] & engine_speed['average'] & engine_load_state['average'], pump_pressure['large'])
rule_108 = ctrl.Rule(oil_temperature['high'] & engine_temperature['low'] & engine_speed['average'] & engine_load_state['high'],  pump_pressure['large'])

rule_109 = ctrl.Rule(oil_temperature['high'] & engine_temperature['low'] & engine_speed['high'] & engine_load_state['none'],    pump_pressure['small'])
rule_110 = ctrl.Rule(oil_temperature['high'] & engine_temperature['low'] & engine_speed['high'] & engine_load_state['low'],   pump_pressure['medium'])
rule_111 = ctrl.Rule(oil_temperature['high'] & engine_temperature['low'] & engine_speed['high'] & engine_load_state['average'], pump_pressure['large'])
rule_112 = ctrl.Rule(oil_temperature['high'] & engine_temperature['low'] & engine_speed['high'] & engine_load_state['high'],  pump_pressure['large'])


rule_113 = ctrl.Rule(oil_temperature['high'] & engine_temperature['average'] & engine_speed['sterile'] & engine_load_state['none'],    pump_pressure['medium'])
rule_114 = ctrl.Rule(oil_temperature['high'] & engine_temperature['average'] & engine_speed['sterile'] & engine_load_state['low'],   pump_pressure['medium'])
rule_115 = ctrl.Rule(oil_temperature['high'] & engine_temperature['average'] & engine_speed['sterile'] & engine_load_state['average'], pump_pressure['large'])
rule_116 = ctrl.Rule(oil_temperature['high'] & engine_temperature['average'] & engine_speed['sterile'] & engine_load_state['high'],  pump_pressure['large'])

rule_117 = ctrl.Rule(oil_temperature['high'] & engine_temperature['average'] & engine_speed['low'] & engine_load_state['none'],    pump_pressure['small'])
rule_118 = ctrl.Rule(oil_temperature['high'] & engine_temperature['average'] & engine_speed['low'] & engine_load_state['low'],   pump_pressure['medium'])
rule_119 = ctrl.Rule(oil_temperature['high'] & engine_temperature['average'] & engine_speed['low'] & engine_load_state['average'], pump_pressure['large'])
rule_120 = ctrl.Rule(oil_temperature['high'] & engine_temperature['average'] & engine_speed['low'] & engine_load_state['high'],  pump_pressure['large'])

rule_121 = ctrl.Rule(oil_temperature['high'] & engine_temperature['average'] & engine_speed['average'] & engine_load_state['none'],    pump_pressure['small'])
rule_122 = ctrl.Rule(oil_temperature['high'] & engine_temperature['average'] & engine_speed['average'] & engine_load_state['low'],   pump_pressure['medium'])
rule_123 = ctrl.Rule(oil_temperature['high'] & engine_temperature['average'] & engine_speed['average'] & engine_load_state['average'], pump_pressure['large'])
rule_124 = ctrl.Rule(oil_temperature['high'] & engine_temperature['average'] & engine_speed['average'] & engine_load_state['high'],  pump_pressure['large'])

rule_125 = ctrl.Rule(oil_temperature['high'] & engine_temperature['average'] & engine_speed['high'] & engine_load_state['none'],    pump_pressure['medium'])
rule_126 = ctrl.Rule(oil_temperature['high'] & engine_temperature['average'] & engine_speed['high'] & engine_load_state['low'],   pump_pressure['medium'])
rule_127 = ctrl.Rule(oil_temperature['high'] & engine_temperature['average'] & engine_speed['high'] & engine_load_state['average'], pump_pressure['large'])
rule_128 = ctrl.Rule(oil_temperature['high'] & engine_temperature['average'] & engine_speed['high'] & engine_load_state['high'],  pump_pressure['large'])


rule_129 = ctrl.Rule(oil_temperature['high'] & engine_temperature['high'] & engine_speed['sterile'] & engine_load_state['none'],    pump_pressure['small'])
rule_130 = ctrl.Rule(oil_temperature['high'] & engine_temperature['high'] & engine_speed['sterile'] & engine_load_state['low'],   pump_pressure['medium'])
rule_131 = ctrl.Rule(oil_temperature['high'] & engine_temperature['high'] & engine_speed['sterile'] & engine_load_state['average'], pump_pressure['large'])
rule_132 = ctrl.Rule(oil_temperature['high'] & engine_temperature['high'] & engine_speed['sterile'] & engine_load_state['high'],  pump_pressure['large'])

rule_133 = ctrl.Rule(oil_temperature['high'] & engine_temperature['high'] & engine_speed['low'] & engine_load_state['none'],    pump_pressure['small'])
rule_134 = ctrl.Rule(oil_temperature['high'] & engine_temperature['high'] & engine_speed['low'] & engine_load_state['low'],   pump_pressure['medium'])
rule_135 = ctrl.Rule(oil_temperature['high'] & engine_temperature['high'] & engine_speed['low'] & engine_load_state['average'], pump_pressure['large'])
rule_136 = ctrl.Rule(oil_temperature['high'] & engine_temperature['high'] & engine_speed['low'] & engine_load_state['high'],  pump_pressure['large'])

rule_137 = ctrl.Rule(oil_temperature['high'] & engine_temperature['high'] & engine_speed['average'] & engine_load_state['none'],    pump_pressure['medium'])
rule_138 = ctrl.Rule(oil_temperature['high'] & engine_temperature['high'] & engine_speed['average'] & engine_load_state['low'],   pump_pressure['medium'])
rule_139 = ctrl.Rule(oil_temperature['high'] & engine_temperature['high'] & engine_speed['average'] & engine_load_state['average'], pump_pressure['large'])
rule_140 = ctrl.Rule(oil_temperature['high'] & engine_temperature['high'] & engine_speed['average'] & engine_load_state['high'],  pump_pressure['large'])

rule_141 = ctrl.Rule(oil_temperature['high'] & engine_temperature['high'] & engine_speed['high'] & engine_load_state['none'],    pump_pressure['medium'])
rule_142 = ctrl.Rule(oil_temperature['high'] & engine_temperature['high'] & engine_speed['high'] & engine_load_state['low'],   pump_pressure['medium'])
rule_143 = ctrl.Rule(oil_temperature['high'] & engine_temperature['high'] & engine_speed['high'] & engine_load_state['average'], pump_pressure['large'])
rule_144 = ctrl.Rule(oil_temperature['high'] & engine_temperature['high'] & engine_speed['high'] & engine_load_state['high'],  pump_pressure['large'])

# Driver blurred
pump_pressure_ctrl = ctrl.ControlSystem([rule_1, rule_2, rule_3, rule_4, rule_5, rule_6, rule_7, rule_8, rule_9,
                                           rule_10, rule_11, rule_12, rule_13, rule_14, rule_15, rule_16, rule_17, rule_18, rule_19,
                                           rule_20, rule_21, rule_22, rule_23, rule_24, rule_25, rule_26, rule_27, rule_28, rule_29,
                                           rule_30, rule_31, rule_32, rule_33, rule_34, rule_35, rule_36, rule_37, rule_38, rule_39,
                                           rule_40, rule_41, rule_42, rule_43, rule_44, rule_45, rule_46, rule_47, rule_48, rule_49,
                                           rule_50, rule_51, rule_52, rule_53, rule_54, rule_55, rule_56, rule_57, rule_58, rule_59,
                                           rule_60, rule_61, rule_62, rule_63, rule_64, rule_65, rule_66, rule_67, rule_68, rule_69,
                                           rule_70, rule_71, rule_72, rule_73, rule_74, rule_75, rule_76, rule_77, rule_78, rule_79,
                                           rule_80, rule_81, rule_82, rule_83, rule_84, rule_85, rule_86, rule_87, rule_88, rule_89,
                                           rule_90, rule_91, rule_92, rule_93, rule_94, rule_95, rule_96, rule_97, rule_98, rule_99,
                                           rule_100, rule_101, rule_102, rule_103, rule_104, rule_105, rule_106, rule_107, rule_108, rule_109,
                                           rule_110, rule_111, rule_112, rule_113, rule_114, rule_115, rule_116, rule_117, rule_118, rule_119,
                                           rule_120, rule_121, rule_122, rule_123, rule_124, rule_125, rule_126, rule_127, rule_128, rule_129,
                                           rule_130, rule_131, rule_132, rule_133, rule_134, rule_135, rule_136, rule_137, rule_138, rule_139,
                                           rule_140, rule_141, rule_142, rule_143, rule_144])

# Simulation of the controller operation
pump_pressure_simulation = ctrl.ControlSystemSimulation(pump_pressure_ctrl)

# Input sharp (crisp)
pump_pressure_simulation.input['oil_temperature'] = 5
pump_pressure_simulation.input['engine_temperature'] = 20
pump_pressure_simulation.input['engine_speed'] = 3743
pump_pressure_simulation.input['engine_load_state'] = 54
pump_pressure_simulation.compute()

oil_temperature.view(sim=pump_pressure_simulation)
engine_temperature.view(sim=pump_pressure_simulation)
engine_speed.view(sim=pump_pressure_simulation)
engine_load_state.view(sim=pump_pressure_simulation)

pump_pressure.view(sim=pump_pressure_simulation)

percentage_of_oil_pump_operation = pump_pressure_simulation.output['pump_pressure']
print('Operation of oil pump: ' + str((((scope_of_operation_pumps[1]-scope_of_operation_pumps[0]) * percentage_of_oil_pump_operation)/100)+scope_of_operation_pumps[0]) + ' bar.')

print('Percentage of oil pump operation: ' + str(pump_pressure_simulation.output['pump_pressure']) + '%')
pump_pressure_ctrl.view()

plt.show()
