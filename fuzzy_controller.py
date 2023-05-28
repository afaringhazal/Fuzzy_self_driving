from typing import List, Tuple, Set, Dict
class FuzzyController:
    """
    #todo
    write all the fuzzify,inference,defuzzify method in this class
    """

    def __init__(self):
        pass


    def compute_membership_dist(self,left_dist: int):
        close_l = 0
        moderate_l = 0
        far_l = 0
        if 50 >= left_dist >= 0:
            # in this part we in the clos_l part
            close_l = (-(1/50) * left_dist) + 1
        if 50 >= left_dist >= 35:
            moderate_l = (1/18) * left_dist + ((-1) * 32/18)
        if 65 >= left_dist >= 50:
            moderate_l = ((-1) * (1/15) * left_dist) + (65/15)
        if 100 >= left_dist >= 50:
            far_l = (1/50) * left_dist + 1
        vector_membership = [close_l, moderate_l, far_l]  # the elements relate to close_L , moderate_L , far_L
        return vector_membership

    def compute_rule(self,vector_l , vector_r):
        close_l = vector_l[0]
        moderate_l = vector_l[1]
        far_l = vector_l[2]
        close_r = vector_r[0]
        moderate_r = vector_r[1]
        far_r = vector_r[2]

        low_right_Rotate = min(close_l, moderate_r)  #0.4
        high_right_Rotate = min(close_l, far_r)     # 0
        low_left_Rotate = min(moderate_l, close_r)   #0.8
        high_left_Rotate = min(far_l, close_r)
        nothing_Rotate = min(moderate_l, moderate_l)

        return self.find_rotate(low_right_Rotate, high_right_Rotate, low_left_Rotate, high_left_Rotate, nothing_Rotate)

    def line_equation(self, point_1: Tuple[float, float], point_2: Tuple[float, float]):
        a = (point_2[1] - point_1[1]) / (point_2[0] - point_1[0])
        b = point_1[1] - (a * point_1[0])
        return a, b


    # def find_center(self, li_e_1: Tuple[float, float], li_e_2: Tuple[float, float], low_right):
    #     first_hit = (low_right - li_e_1[1]) / li_e_1[0]
    #     second_hit = (low_right - li_e_2[1]) / li_e_2[0]
    #     return (first_hit + second_hit) / 2
    #
    # def find_rotate(self, low_right, high_right, low_left, high_left, nothing):
    #
    #     center_high_right = self.find_center(self.line_equation((-50, 0), (-20, 1)), self.line_equation((-5, 0), (-20, 1)), high_right)
    #     center_low_right = self.find_center(self.line_equation((-10, 1), (-20, 0)), self.line_equation((0, 0), (-10, 1)), low_right)
    #     center_nothing = self.find_center(self.line_equation((0, 1), (-10, 0)), self.line_equation((10, 0), (0, 1)), nothing)
    #     center_low_left = self.find_center(self.line_equation((10, 1), (0, 0)), self.line_equation((20, 0), (10, 1)), low_left)
    #     center_high_left = self.find_center(self.line_equation((20, 1), (5, 0)), self.line_equation((50, 0), (20, 1)), high_left)
    #     return (center_high_right + center_low_right +center_nothing +center_low_left + center_high_left)  / 5
    def integral(self, mini, maxi, a, b):
        step = 0.0001
        i = mini
        n1 = 0
        nn1 = 0.0
        while i < maxi:
            n1 += (i * (a * i + b)) * step
            nn1 += (a * i + b) * step
            i += step
        return n1, nn1

    def calculate_integral(self, hit_points:Dict[str, float], line_equations:Dict[str, Tuple[float,float,float]]): # a,b,y
        points = list(hit_points.values())
        i = 1
        sum = 0
        for str , point in hit_points:
            (a, b, y) = line_equations[str]
            if point < points[i]:
                sum += integral(a,b,first_thersold, last_theeshold)


        pass


    def claculate_derivate(self,line_feature :Tuple[float, float] , first_number, second_number, x):
        if x == 1:
            return ((line_feature[0] * second_number * second_number * second_number / 3) + (line_feature[1] * second_number * second_number /2)) \
                - ((line_feature[0] * first_number * first_number * first_number / 3) + (line_feature[1] * first_number * first_number /2))
        elif x == 0:
            return ((line_feature[0] * second_number * second_number / 2) + (
                        line_feature[1] * second_number)) \
                - ((line_feature[0] * first_number * first_number / 2) + (
                            line_feature[1] * first_number))
        else:
            print("there is some problem")
            return 0

    # def find_hit_point(self, li_e_1: Tuple[float, float], li_e_2: Tuple[float, float], low_right):
    #     first_hit = (low_right - li_e_1[1]) / li_e_1[0]
    #     second_hit = (low_right - li_e_2[1]) / li_e_2[0]
    #     return (first_hit , second_hit)

    def find_hit_point(self, li_e_1: Tuple[float, float], y):
        hit = (y - li_e_1[1]) / li_e_1[0]  # y-a/b
        return hit



    # def find_rotate(self, low_right, high_right, low_left, high_left, nothing):
    #
    #     f_h_high_right , s_h_high_right = self.find_center(self.line_equation((-50, 0), (-20, 1)), self.line_equation((-20, 1), (-5, 0)), high_right)
    #     f_h_low_right ,s_h_low_right = self.find_center(self.line_equation((-20, 0), (-10, 1)), self.line_equation((-10, 1),(0, 0)), low_right)
    #     f_h_nothing, s_h_nothing = self.find_center(self.line_equation((-10, 0), (0, 1)), self.line_equation((0, 1),(10, 0)), nothing)
    #     f_h_low_left, s_h_low_left = self.find_center(self.line_equation((0, 0),(10, 1)), self.line_equation((10, 1),(20, 0)), low_left)
    #     f_h_high_left, s_h_high_left = self.find_center(self.line_equation((5, 0),(20, 1)), self.line_equation((20, 1),(50, 0)), high_left)
    #     v1 = self.claculate_derivate(self.line_equation((-50, 0), (-20, 1)), -50, f_h_high_right, 1)  # change to antegral
    #     v2 = self.claculate_derivate(self.line_equation((-20, 1), (-5, 0)), -20 , s_h_high_right, 1)
    #     v3 = self.claculate_derivate(self.line_equation((-20, 0), (-10, 1)), -20 , f_h_low_right, 1)
    #     v4 = self.claculate_derivate(self.line_equation((-10, 1),(0, 0)), -10 , s_h_low_right, 1)
    #     v5 = self.claculate_derivate(self.line_equation((-10, 0), (0, 1)), -10 , f_h_nothing, 1)
    #     v6 = self.claculate_derivate(self.line_equation((0, 1),(10, 0)), 0 , s_h_nothing, 1)
    #     v7 = self.claculate_derivate(self.line_equation((0, 0),(10, 1)), 0 , f_h_low_left, 1)
    #     v8 = self.claculate_derivate(self.line_equation((10, 1),(20, 0)), 10 , s_h_low_left, 1)
    #     v9 = self.claculate_derivate(self.line_equation((5, 0),(20, 1)), 5 , f_h_high_left, 1)
    #     v10 = self.claculate_derivate(self.line_equation((20, 1),(50, 0)), 20 , s_h_high_left, 1)
    #
    #     m1 = self.claculate_derivate(self.line_equation((-50, 0), (-20, 1)), -50, f_h_high_right, 0)
    #     m2 = self.claculate_derivate(self.line_equation((-20, 1), (-5, 0)), -20, s_h_high_right, 0)
    #     m3 = self.claculate_derivate(self.line_equation((-20, 0), (-10, 1)), -20, f_h_low_right, 0)
    #     m4 = self.claculate_derivate(self.line_equation((-10, 1),(0, 0)), -10, s_h_low_right, 0)
    #     m5 = self.claculate_derivate(self.line_equation((-10, 0), (0, 1)), -10, f_h_nothing, 0)
    #     m6 = self.claculate_derivate(self.line_equation((0, 1),(10, 0)), 0, s_h_nothing, 0)
    #     m7 = self.claculate_derivate(self.line_equation((0, 0),(10, 1)), 0, f_h_low_left, 0)
    #     m8 = self.claculate_derivate(self.line_equation((10, 1),(20, 0)), 10, s_h_low_left, 0)
    #     m9 = self.claculate_derivate(self.line_equation((5, 0),(20, 1)), 5, f_h_high_left, 0)
    #     m10 = self.claculate_derivate(self.line_equation((20, 1), (50, 0)), 20, s_h_high_left, 0)
    #     return (v1+v2+v3+v4+v5+v6+v7+v8+v9+v10) / (m1+m2+m3+m4+m5+m6+m7+m8+m9+m10)
    #     # return (center_high_right + center_low_right +center_nothing +center_low_left + center_high_left)  / 5

    def find_rotate(self, low_right, high_right, low_left, high_left, nothing):
        line_equations : Dict[str, Tuple[float, float, float]] = dict()
        (a,b) = self.line_equation((-50, 0), (-20, 1))
        line_equations["high_right_left"] = (a,b,high_right)
        (a,b) = self.line_equation((-20, 1), (-5, 0))
        line_equations["high_right_right"] = (a,b,high_right)
        (a,b) = self.line_equation((-20, 0), (-10, 1))
        line_equations["low_right_left"] = (a,b,low_right)
        (a,b) = self.line_equation((-10, 1), (0, 0))
        line_equations["low_right_right"] = (a,b,low_right)
        (a,b) = self.line_equation((-10, 0), (0, 1))
        line_equations["nothing_left"] = (a,b, nothing)
        (a,b) = self.line_equation((0, 1), (10, 0))
        line_equations["nothing_right"] = (a,b,nothing)
        (a,b) = self.line_equation((0, 0), (10, 1))
        line_equations["low_left_left"] = (a,b,low_left)
        (a, b) = self.line_equation((10, 1), (20, 0))
        line_equations["low_left_right"] = (a,b,low_left)
        (a,b) = self.line_equation((5, 0), (20, 1))
        line_equations["high_left_left"] = (a,b,high_left)
        (a,b) = self.line_equation((20, 1), (50, 0))
        line_equations["high_left_right"] = (a,b,high_left)

        hit_points : Dict[str, int] = dict()

        for name_fun, (a,b,y) in line_equations.items():
            hit_points[name_fun] = self.find_hit_point((a,b),y)

        return self.calculate_integral(hit_points, line_equations)

    def decide(self, left_dist,right_dist):
        """
        main method for doin all the phases and returning the final answer for rotation
        """
        vector_l = self.compute_membership_dist(left_dist)
        vector_r = self.compute_membership_dist(right_dist)
        return self.compute_rule(vector_l, vector_r)


