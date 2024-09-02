import av1.cenario_3.LinearAlgebra as la

test = la.LinearAlgebra.times(2, [[1, 2, 3], [4, 5, 6]])

test_01 = la.LinearAlgebra.times([1,2,3], [1, 2, 3])

test_02 = la.LinearAlgebra.times([[1, 2, 3], [4, 5, 6]],[[1, 2, 3], [4, 5, 6]])

test_03 = la.LinearAlgebra.times([[1, 2, 3], [4, 5, 6]],2)

test_04 = la.LinearAlgebra.times(2,2)

test_05 = la.LinearAlgebra.times([1,2], [1, 2, 3])

test_06 = la.LinearAlgebra.times([[1,2,3],[1,2]], [1,2,3])

print(f"Test: {test}")
print(f"Test_01: {test_01}")
print(f"Test_02: {test_02}")
print(f"Test_03: {test_03}")
print(f"Test_04: {test_04}")
print(f"Test_05: {test_05}")
print(f"Test_06: {test_06}")


# def test(a,b):
#     type_a = isinstance(a, (list))
#     type_b = type(b)
#     if isinstance(a, (list)):
#         for i in range(len(a)):
#             print(a[i] * i)
#     print(f"Type a: {type_a}")
#     print(f"Type b: {type_b}")
    
    
# a = [1,2,3]
# b = [[1,2,3],[1,2,3]]

# test(a,b)