# for i in range(3):
#     for j in range(5):
#         print(f"({i},{j})", end=" ")
#         print()

inner=[0,1,2,3,4,5,]

outer=[]
for i in range(3):
    outer.append(inner)

# print(outer)
#
#
# for i in range(len(outer)):
#     print(outer[i])
# print()
#
# for i in outer:
#     print(i)
# print()
# print(outer)

#alle schleifen geben untereinander alle elemente der listen aus

outer=[[1,2,3], [4,5,6], [7,8,9]]
#
# for inner in outer:
#     for element in inner:
#         print(element)
#     print()
#
# #hier können den elementen der inneren Listen neue Werte zugewiesen werden
# for inner in outer:
#     for i_inner in range(len(inner)):
#         print(inner[i_inner])
#     print()
#
# #hier können den elementen der inneren Listen neuen Werte zugewiesen werden
# for i_outer in range(len(outer)):
#     for i_inner in range(len(outer[i_outer])):
#         print(outer[i_outer][i_inner])
#     print()

# for i_outer in range(len(outer)):
#     for i_inner in range(len(outer[i_outer])):
#         print(outer[i_outer][i_inner], f"[{i_outer}], [{i_inner}]", end= " ,")
#     print()

print(outer[0])
outer[0].append(78)
print(outer[0])
print(outer)
