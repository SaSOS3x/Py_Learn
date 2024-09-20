def check(input_func):

    def output_func(*args):

        try:

            test_list = list(args)

            for idx, y in enumerate(test_list):

                test_list[idx] = float(y)

        except ValueError as e:
            
            print(f"\nВведите число, а не строку\n")
            
            return 0

        args = test_list

        result = input_func(*args)
        return round(result, 3)

    return output_func