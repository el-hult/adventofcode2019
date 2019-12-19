from util import basic_operation_of_system_test, run_siso_program

prog = basic_operation_of_system_test()
output = run_siso_program(prog, 1)
print(output)
assert output == 2351176124

output = run_siso_program(prog, 2)
print(output)
assert output == 73110
