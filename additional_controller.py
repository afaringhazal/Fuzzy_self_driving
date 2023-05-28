from typing import Tuple,List, Dict, Set
class FuzzyGasController:
    """
    # emtiazi todo
    write all the fuzzify,inference,defuzzify method in this class
    """

    def __init__(self):
        pass

    def compute_membership_dist(self, center_dist):
        close = 0
        moderate = 0
        far = 0
        if 50 >= center_dist >= 0:
            close = ((-1)* (1/50) * center_dist) + 1
        if 50 >= center_dist >= 40:
            moderate = ((1/10) * (center_dist)) - 4
        if 100 >= center_dist >= 50 :
            moderate = (-1)*(1/50)*center_dist + 2
        if 200>= center_dist >=90:
            far = ((1/110) * center_dist) - (90/110)
        if center_dist >= 200:
            far = ((1 / 110) * center_dist) - (90 / 110)
        vector_membership = [close, moderate, far]
        return vector_membership

    def line_equation(self, point_1: Tuple[float, float], point_2: Tuple[float, float]):
        a = (point_2[1] - point_1[1]) / (point_2[0] - point_1[0])
        b = point_1[1] - (a * point_1[0])
        return a, b

    def find_line_equations(self):
        line_equations: List[Tuple[str, Tuple[float, float], int]] = list()
        line_equations.append(("low", self.line_equation((0, 0), (5, 1)), 1))
        line_equations.append(("low", self.line_equation((5, 1), (10, 0)), -1))
        line_equations.append(("medium", self.line_equation((0, 0), (15, 1)), 1))
        line_equations.append(("medium", self.line_equation((15, 1), (30, 0)), -1))
        line_equations.append(("high", self.line_equation((25, 0), (30, 1)), 1))
        line_equations.append(("high", self.line_equation((30, 1), (90, 0)), -1))
        return line_equations
    def find_y(self,rules: List[Tuple[str, float]], name_):
        for name, y in rules:
            if name == name_:
                return y
    def calculate_range_number_and_maximum_effective(self,rules: List[Tuple[str, float]],line_equations:List[Tuple[str, Tuple[float, float], int]]):
        rang_number : List[Tuple[float, float, Tuple[float, float],str]] = list()
        name = list()
        a = list()
        b = list()
        validation = list()
        for i in range(len(line_equations)):
            name_, (a_, b_), validation_ = line_equations[i]
            name.append(name_)
            a.append(a_)
            b.append(b_)
            validation.append(validation_)
        ##############
        if self.find_y(rules, name[0]) < self.find_y(rules,name[2]):
            rang_number.append((0, 5, (a[2], b[2]),name[2]))
        else:
            rang_number.append((0, 5, (a[0], b[0]),name[0]))
        ##################################3
        if self.find_y(rules, name[1]) < self.find_y(rules, name[2]):
            rang_number.append((5, 10, (a[2], b[2]), name[2]))
        else:
            rang_number.append((5, 10, (a[1], b[1]), name[1]))
        ##############################
        rang_number.append((10, 15, (a[2], b[2]),name[2]))
        ######################
        rang_number.append((15, 25, (a[3], b[3]),name[3]))
        #########################
        if self.find_y(rules, name[3]) < self.find_y(rules, name[4]):
            rang_number.append((25, 30, (a[4], b[4]), name[4]))
        else:
            rang_number.append((25, 30, (a[3], b[3]), name[3]))
        #####################33
        rang_number.append((30, 90, (a[5], b[5]),name[5]))
        return rang_number

    def integeral_final(self, min_num, max_num, line, rules: List[Tuple[str, float]]):
        name, (a, b) = line
        i = min_num
        sigma = 0.0
        sigma_m = 0.0
        delta = 0.01
        while i < max_num:
            y = self.find_y(rules, name)
            y_prime = a * i + b
            if y_prime > y:
                sigma += y * delta * i
                sigma_m += y * delta
            else:
                sigma += y_prime * delta * i
                sigma_m += y_prime * delta
            i += delta

        return sigma, sigma_m

    def find_center_of_gravity(self,line_equations:List[Tuple[str, Tuple[float, float], int]], rules: List[Tuple[str, float]]):
        range_number = self.calculate_range_number_and_maximum_effective(rules, line_equations)
        sigma_tot = 0
        sigma_m_tot = 0
        for min_num, max_num, (a, b), name in range_number:
            s, s_ = self.integeral_final(min_num, max_num, (name, (a, b)), rules)
            sigma_tot += s
            sigma_m_tot += s_
        if sigma_m_tot != 0:
            result = float(sigma_tot) / float(sigma_m_tot)
        else:
            return 0
        print(f'result {result}')
        if result < 0:
            print("negative")
        return result

    def find_rotate(self,rules: List[Tuple[str, float]]):
        line_equations = self.find_line_equations()
        return self.find_center_of_gravity(line_equations, rules)

    def compute_rules(self,vector):
        close = vector[0]
        moderate = vector[1]
        far = vector[2]
        rules: List[Tuple[str, float]] = list()
        rules.append(("low", close))
        rules.append(("medium", moderate))
        rules.append(("high", far))
        return self.find_rotate(rules)

    def decide(self, center_dist):
        """
        main method for doin all the phases and returning the final answer for gas
        """
        vectore_center = self.compute_membership_dist(center_dist)
        return self.compute_rules(vectore_center)
        # return 30
    