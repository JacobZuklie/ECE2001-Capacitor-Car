import numpy
class Series:
    def __init__(self, plate_mass_density, di_const, di_max_min, di_thick_min, needed_capacitance, plate_max_min, di_mass_density):
        self.di_mass_density = di_mass_density
        self.plate_max_min = plate_max_min
        self.needed_capacitance = needed_capacitance
        self.di_thick_min = di_thick_min
        self.di_max_min = di_max_min
        self.di_const = di_const
        self.plate_mass_density = plate_mass_density

    def Calculate(self):
        weight_best = 100000000000000000
        thick_best = 0
        stack_best = 0
        area_best = 0
        name_plate = 0
        name_di = 0

        for y in range(0, len(self.plate_mass_density), 1):
            # print("Testing", plate_names[y])

            for x in range(0, len(self.di_const), 1):
                # print("On dielectric", di_names[x])

                for stack in numpy.arange(1, 101, 1):  # Number of Stacks
                    # print("Stack Number:", stack)
                    step = (self.di_max_min[1] - self.di_thick_min[x])/20

                    for thick in numpy.arange(self.di_thick_min[x], self.di_max_min[1], step):  # Goes through different thickness amounts
                        area = self.needed_capacitance * thick * stack / self.di_const[x]
                        # print("Area:", area)
                        volume_capacitor = (stack + 1) * area * self.plate_max_min[0] + stack * area * thick
                        weight_capacitor = (stack + 1) * area * self.plate_max_min[0] * self.plate_mass_density[y] + stack * area * thick * self.di_mass_density[x]
                        # print("Weight(kg):", weight_capacitor)
                        # print()
                        if(weight_capacitor<weight_best):
                            weight_best = weight_capacitor
                            thick_best = thick
                            stack_best = stack
                            area_best = area
                            name_plate = y
                            name_di = x
        return weight_best, thick_best, stack_best, name_plate, name_di, area_best



class Parallel:
    def __init__(self, plate_mass_density, di_const, di_max_min, di_thick_min, needed_capacitance, plate_max_min, di_mass_density):
        self.di_mass_density = di_mass_density
        self.plate_max_min = plate_max_min
        self.needed_capacitance = needed_capacitance
        self.di_thick_min = di_thick_min
        self.di_max_min = di_max_min
        self.di_const = di_const
        self.plate_mass_density = plate_mass_density

    def Calculate(self):
        weight_best = 100000000000000000
        thick_best = 0
        stack_best = 0
        area_best = 0
        name_plate = 0
        name_di = 0
        width = 2
        di_names = ["SiO2", "H2O", "Hi-K dielectric 1", "Hi-K dielectric 2"]

        for y in range(0, len(self.plate_mass_density), 1):
            # print("Testing", plate_names[y])

            for x in range(0, len(self.di_const), 1):
                # print("On dielectric", di_names[x])

                for stack in numpy.arange(1, 10001, 1):  # Number of Stacks
                    # print("Stack Number:", stack)
                    step = (self.di_max_min[1] - self.di_thick_min[x])/20

                    for thick in numpy.arange(self.di_thick_min[x], self.di_max_min[1], step):  # Goes through different thickness amounts
                        area = self.needed_capacitance * thick / (self.di_const[x] * stack)

                        # print("Area:", area)
                        volume_capacitor = (stack + 1) * area * self.plate_max_min[0] + stack * area * thick
                        height = (stack + 1) * self.plate_max_min[0] + stack * self.di_thick_min[x]
                        weight_capacitor = (stack * width * self.di_thick_min[x] * self.di_mass_density[x] * (self.plate_max_min[0] + (area / width + 2 * self.di_thick_min[x]))) + (self.plate_mass_density[y] * ((stack + 1) * self.plate_max_min[0] * (area + width * self.di_thick_min[x]) + (2* self.plate_max_min[0] * width * height)))
                        # weight_capacitor = (stack + 1) * area * self.plate_max_min[0] * self.plate_mass_density[y] + stack * area * thick * self.di_mass_density[x]
                        # print("Weight(kg):", weight_capacitor)
                        # print()
                        if(weight_capacitor<weight_best):
                            weight_best = weight_capacitor
                            thick_best = thick
                            stack_best = stack
                            area_best = area
                            name_plate = y
                            name_di = x
                            height_best = height
        return weight_best, thick_best, stack_best, name_plate, name_di, area_best, height_best



class Name2:
    def __init__(self, plate_mass_density, di_const, needed_capacitance, plate_max_min, di_mass_density, x, y, thickness, di_thick_min):
        self.di_thick_min = di_thick_min
        self.thickness = thickness
        self.y = y  # plate
        self.x = x  # dielectric
        self.di_mass_density = di_mass_density
        self.plate_max_min = plate_max_min
        self.needed_capacitance = needed_capacitance
        self.di_const = di_const
        self.plate_mass_density = plate_mass_density

    def SeriesGraphDataWvS(self):
        weight_data = []
        stack_data = []
        for stack in numpy.arange(1, 101, 1):  # Number of Stacks
            area = self.needed_capacitance * self.thickness * stack / self.di_const[self.x]
            volume_capacitor = (stack + 1) * area * self.plate_max_min[0] + stack * area * self.thickness
            weight_capacitor = (stack + 1) * area * self.plate_max_min[0] * self.plate_mass_density[self.y] + stack * area * self.thickness * self.di_mass_density[self.x]
            weight_data.append(weight_capacitor)
            stack_data.append(stack)
        return weight_data, stack_data
    def ParallelGraphDataWvS(self):
        weight_data = []
        stack_data = []
        width = 2
        for stack in numpy.arange(1, 101, 1):  # Number of Stacks
            area = self.needed_capacitance * self.thickness / (self.di_const[self.x] * stack)
            volume_capacitor = (stack + 1) * area * self.plate_max_min[0] + stack * area * self.thickness
            height = (stack + 1) * self.plate_max_min[0] + stack * self.di_thick_min[self.x]
            weight_capacitor = (stack * width * self.di_thick_min[self.x] * self.di_mass_density[self.x] * (self.plate_max_min[0] + (area / width + 2 * self.di_thick_min[self.x]))) + (self.plate_mass_density[self.y] * ((stack + 1) * self.plate_max_min[0] * (area + width * self.di_thick_min[self.x]) + (2 * self.plate_max_min[0] * width * height)))
            # weight_capacitor = (stack + 1) * area * self.plate_max_min[0] * self.plate_mass_density[self.y] + stack * area * self.thickness * self.di_mass_density[self.x]
            weight_data.append(weight_capacitor)
            stack_data.append(stack)
        return weight_data, stack_data



class Name3:
    def __init__(self, plate_mass_density, di_const, di_max_min, di_thick_min, needed_capacitance, plate_max_min, di_mass_density, x, y, stack):
        self.stack = stack
        self.y = y  # plate
        self.x = x  # dielectric
        self.di_mass_density = di_mass_density
        self.plate_max_min = plate_max_min
        self.needed_capacitance = needed_capacitance
        self.di_thick_min = di_thick_min
        self.di_max_min = di_max_min
        self.di_const = di_const
        self.plate_mass_density = plate_mass_density

    def SeriesGraphDataWvT(self):
        weight_data = []
        thick_data = []
        step = (self.di_max_min[1] - self.di_thick_min[self.x]) / 20
        for thick in numpy.arange(self.di_thick_min[self.x], self.di_max_min[1], step):  # Goes through different thickness amounts
            area = self.needed_capacitance * thick * self.stack / self.di_const[self.x]
            volume_capacitor = (self.stack + 1) * area * self.plate_max_min[0] + self.stack * area * thick
            weight_capacitor = (self.stack + 1) * area * self.plate_max_min[0] * self.plate_mass_density[self.y] + self.stack * area * thick * self.di_mass_density[self.x]
            weight_data.append(weight_capacitor)
            thick_data.append(thick)
        return weight_data, thick_data
    def ParallelGraphDataWvT(self):
        weight_data = []
        thick_data = []
        step = (self.di_max_min[1] - self.di_thick_min[self.x]) / 20
        for thick in numpy.arange(self.di_thick_min[self.x], self.di_max_min[1], step):  # Goes through different thickness amounts
            area = self.needed_capacitance * thick / (self.di_const[self.x] * self.stack)
            volume_capacitor = (self.stack + 1) * area * self.plate_max_min[0] + self.stack * area * thick
            weight_capacitor = (self.stack + 1) * area * self.plate_max_min[0] * self.plate_mass_density[self.y] + self.stack * area * thick * self.di_mass_density[self.x]
            weight_data.append(weight_capacitor)
            thick_data.append(thick)
        return weight_data, thick_data
