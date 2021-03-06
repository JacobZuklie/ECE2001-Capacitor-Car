import matplotlib.pyplot as plt
import SubCalc as sc


# Units: Ferad/meter
e0 = 8.85*10**(-12)
# [SiO2, H2O,Hi-K dielectric 1, Hi-K dielectric 2]  Units: Ferad/meter
di_const = [4*e0, 80*e0, 200*e0, 300*e0]
di_names = ["SiO2", "H2O", "Hi-K dielectric 1", "Hi-K dielectric 2"]

# [SiO2, H2O,Hi-K dielectric 1, Hi-K dielectric 2]  Units: Ferad/meter
breakdown_field = [1/10**(-9), 0.03/10**(-9), 0.2/10**(-9), 0.1/10**(-9)]

# [SiO2, H2O,Hi-K dielectric 1, Hi-K dielectric 2]  Units: kilogram/meter^3
di_mass_density = [2500, 1000, 1250, 3000]

# [aluminum, graphite]  Units: kilogram/meter^3
plate_mass_density = [2700, 2100]
plate_names = ["aluminum", "graphite"]

# Units: meter
di_max_min = [10*10**(-9), 500*10**(-6)]
plate_max_min = [1*10**(-6), 1*10**(-2)]

# Units: Volts
max_voltage = 10000

# Units: Joules
needed_energy = 805356000

# Units: Ferads
needed_capacitance = 2 * needed_energy / max_voltage**2
print(needed_capacitance)

# Variables
factor_safety = 1
# Variables For Storage
di_thick_min = []


# generates a list that contains the minimum dielectric thickness
# this is different than manufacturing minimum, this is for the safety of the dielectric material
# makes sure the capacitor does not shot through the dielectric
for x in range(0, len(breakdown_field), 1):
    di_thick_min.append((breakdown_field[x] / max_voltage)**(-1) * factor_safety)
print(di_thick_min)
print(di_names)

# saves all information needed to display critrical data on the best capacitor design
weight_best_series, thick_best_series, stack_best_series, name_plate_series, name_di_series, area_series, height_series, volume_series = sc.Series(plate_mass_density, di_const, di_max_min, di_thick_min, needed_capacitance, plate_max_min, di_mass_density).Calculate()
weight_best_parallel, thick_best_parallel, stack_best_parallel, name_plate_parallel, name_di_parallel, area_parallel, height_parallel, volume_parallel = sc.Parallel(plate_mass_density, di_const, di_max_min, di_thick_min, needed_capacitance, plate_max_min, di_mass_density).Calculate()

# Saves series data used to graph
weight_data_series, stack_data_series = sc.WvS(plate_mass_density, di_const, needed_capacitance, plate_max_min, di_mass_density, name_di_series, name_plate_series, thick_best_series, 0).SeriesGraphDataWvS()
weight_data_series2, thick_data_series = sc.WvT(plate_mass_density, di_const, di_max_min, di_thick_min, needed_capacitance, plate_max_min, di_mass_density, name_di_series, name_plate_series, stack_best_series).SeriesGraphDataWvT()

# Saves parallel data used to graph
weight_data_parallel, stack_data_parallel = sc.WvS(plate_mass_density, di_const, needed_capacitance, plate_max_min, di_mass_density, name_di_parallel, name_plate_parallel, thick_best_parallel, di_thick_min).ParallelGraphDataWvS()
weight_data_parallel2, thick_data_parallel = sc.WvT(plate_mass_density, di_const, di_max_min, di_thick_min, needed_capacitance, plate_max_min, di_mass_density, name_di_parallel, name_plate_parallel, stack_best_parallel).ParallelGraphDataWvT()

# If the series weight is less then the parrallel weight then it prints information regarding the series circuit
if (weight_best_series < weight_best_parallel):
    print()
    print("Best Material")
    print("Plate:", plate_names[name_plate_series])
    print("Dielectric:", di_names[name_di_series])
    print("Mass(kg):", weight_best_series)
    print("Thickness(m):", thick_best_series)
    print("Stack Height:", stack_best_series)
    print("Area", area_series)
    print("Height", height_series)
    print("Volume", volume_series)
    print("Circuit Type: Series")
    print("Time to 60Mph", ((weight_best_series + 1500) * (26.8223 ** 2) / (2 * 74570)), 'seconds')

# If the parallel weight is less then the series weight then it prints information regarding the parallel circuit
elif(weight_best_parallel < weight_best_series):
    print()
    print("Best Material")
    print("Plate:", plate_names[name_plate_parallel])
    print("Dielectric:", di_names[name_di_parallel])
    print("Mass(kg):", weight_best_parallel)
    print("Thickness(m):", thick_best_parallel)
    print("Stack Height:", stack_best_parallel)
    print("Area", area_parallel)
    print("Height", height_parallel)
    print("Volume", volume_parallel)
    print("Circuit Type: Parallel")
    print("Time to 60Mph", ((weight_best_parallel + 1500) * (26.8223**2) / (2 * 74570)), 'seconds')

# the rest of the code is in reference to printing graphs for the weight vs thickness and weight vs stack amount

plt.figure('Series WvS')
plt.plot(weight_data_series, stack_data_series)
plt.suptitle('Weight of Capacitor vs. Number of Stacked Capacitors (Series)')
plt.xlabel('Weight (kg)')
plt.ylabel('Number Stacked')
plt.grid(True)

plt.figure('Series WvT')
plt.plot(weight_data_series2, thick_data_series)
plt.suptitle('Weight of Capacitor vs. Thickness of Dielectric Material')
plt.xlabel('Weight (kg)')
plt.ylabel('Thickness of Dielectric (m)')
plt.grid(True)

plt.figure('Parallel WvS')
plt.plot(weight_data_parallel, stack_data_parallel)
plt.suptitle('Weight of Capacitor vs. Number of Stacked Capacitors (Parallel)')
plt.xlabel('Weight (kg)')
plt.ylabel('Number Stacked')
plt.grid(True)

plt.figure('Parallel WvT')
plt.plot(weight_data_parallel2, thick_data_parallel)
plt.suptitle('Weight of Capacitor vs. Thickness of Dielectric Material')
plt.xlabel('Weight (kg)')
plt.ylabel('Thickness of Dielectric (m)')
plt.grid(True)
plt.show()


