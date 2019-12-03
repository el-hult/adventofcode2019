from day2_lib import compute_computer_output

INPUT_PATH = 'inputs/day2.txt'

if __name__ == "__main__":
    with open(INPUT_PATH) as f:
        line = f.readline().strip()
        state = line.split(",")
        program = list(map(lambda x: int(x), state))

    ans_a = compute_computer_output(program, 12, 2)
    print(f"The value in position 0 after completion is {ans_a}")  # 3850704 is just right

    generator_for_brute_force_atacking_b = (
        (noun, verb, compute_computer_output(program, noun, verb))
        for noun in range(100)
        for verb in range(100)
    )

    for (noun, verb, output) in generator_for_brute_force_atacking_b:
        if output == 19690720:
            print(noun, verb, output)
            print(f"The answer to B is: {100 * noun + verb}")  # 6718
            break
